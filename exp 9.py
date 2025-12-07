import numpy as np

a = np.array([[1, 2, 3], 
                [4, 5, 6]])

b = np.array([[7, 8, 9],  
                [10, 11, 12]])

print("Array Creation:")
print("Array a:", a)
print("Array b:", b)




print("Multiplication of array :")
multy_result = a * b
multy_result




print("Addition of array :")
add_result = a + b
add_result



print("subtraction of array :")
sub_result = a - b
sub_result


print("transpose of array a :")
transpose_a = a.T
transpose_a



print("reshaping array b")
result = b.reshape(3,2)
result
