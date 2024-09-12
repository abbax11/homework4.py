
immutable_var = (1, 2, 3, "lalala", True)
print(immutable_var)
print(immutable_var)
mutable_list = ([1,2,3], 0 )
print(mutable_list)
mutable_list[0][1]= 5
print(mutable_list)
immutable_var[0] = 10            #кортеж не изменяемый список

