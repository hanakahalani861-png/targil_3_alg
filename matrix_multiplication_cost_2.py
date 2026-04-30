def matrix_multiplication_cost_2(dimensions):
    if(len(dimensions)!=3):
        return False
    return dimensions[0]*dimensions[1]*dimensions[2]