class matrix_multiplication_table:
    def add_ops_range(self):
        for i in range(len(self.table)):
            for j in range(len(self.table)):
                if i<j:
                    self.table[i+1][j+1] = {"range": (i+1, j+1)}

    def  calculate_one_multiplication_cost(self):
        for i in range(len(self.table)-1):
            self.table[i+1][i+2]["cost"] = self.dimensions[i]*self.dimensions[i+1]*self.dimensions[i+2]
            self.table[i+1][i+2]["optimized_parenthesization"] = F"A{i+1}xA{i+2}"

    def cost_multiplication_calculate(self, num_multiplications):
        for i in range(len(self.table) - num_multiplications):
            j = i + num_multiplications
            row, col = i + 1, j + 1
            min_cost = float('inf')
            best_expr = ""
            for k in range(row, col):
                left_cost = self.table[row][k]["cost"] if row < k else 0
                right_cost = self.table[k+1][col]["cost"] if k+1 < col else 0
                left_expr = self.table[row][k]["optimized_parenthesization"] if row < k else f"A{row}"
                right_expr = self.table[k+1][col]["optimized_parenthesization"] if k+1 < col else f"A{col}"
                current_cost = left_cost + right_cost + (self.dimensions[row-1] * self.dimensions[k] * self.dimensions[col])
                if current_cost < min_cost:
                    min_cost = current_cost
                    best_expr = f"({left_expr}x{right_expr})"
            if self.table[row][col] is None:
                self.table[row][col] = {"range": (row, col)}
            self.table[row][col]["cost"] = min_cost
            self.table[row][col]["optimized_parenthesization"] = best_expr

    def __init__(self,dimensions):
        self.dimensions = dimensions
        self.titles = {}
        for i in range(len(dimensions)-1):
            self.titles[i+1] = F"A{i+1}: {dimensions[i]} x {dimensions[i+1]}" # exercise: fill in the dimensions of the matrices
        
        self.table = {}
        for i in range(1, len(dimensions)):
            self.table[i] = {}
            for j in range(1, len(dimensions)):
                self.table[i][j] = None

    def cell_to_html(self, cell):
        if cell is None:
            return ""
        if type(cell) is not dict:
            return ""
        # else, cell is a dict
        ret = ""
        i,j = cell["range"]
        if j == i+1:
            ret += F"ops: A{i} x A{j}"
        else:
            ret += F"ops: A{i} .. A{j}"

        if "cost" in cell:
            ret += F"<br>cost: {cell['cost']}"
        if "optimized_parenthesization" in cell:
            ret += F"<br>optimized: {cell['optimized_parenthesization']}"
        return ret

    def print_to_html(self):
        html = "<table border='1' style='border-collapse: collapse'>\n"
        html += "<tr><th></th>"
        for j in range(1, len(self.dimensions)):
            html += F"<th>{self.titles[j]}</th>"
        html += "</tr>\n"
        for i in range(1, len(self.dimensions)):
            html += F"<tr><th>{self.titles[i]}</th>"
            for j in range(1, len(self.dimensions)):
                cell = self.table[i][j]
                html += F"<td>{self.cell_to_html(cell)}</td>"
            html += "</tr>\n"
        html += "</table>"
        return html

def main():
    dimensions=[50, 10, 25, 45, 8]
    t = matrix_multiplication_table(dimensions)

    t.add_ops_range()
    t.calculate_one_multiplication_cost()
    for i in range(2, len(dimensions)):
        t.cost_multiplication_calculate(i)

    output_file = "matrix_multiplication_table.html"
    with open(output_file, "w") as f:
        f.write(t.print_to_html())

if __name__ == "__main__":
    main()