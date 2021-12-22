def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)
    return p * l

def penjumlahan(num1, num2, num3): 
    return num1+num2+num3

def printme(str_input):
    '''This prints a passed string into this function'''
    print(str_input)

my_function(9, 2)
print(my_function.__doc__)

print(100)
print(printme.__doc__)

printme("I'm first call to user defined function!")
printme("Again seccond call to the same function")

luas = my_function(10, 3)
print(f"Luas persegi panjang adalah {luas}")
hasil_penjumlahan = penjumlahan(50, 60, 4)
# hasil_penjumlahan = num1 + num2 + num3
#                   = 50 + 60 +4
#                   = 114
print(f"Hasil penjumlahan = {hasil_penjumlahan}")

# def save_data(name, age):
#     print(f"Nama : {name}")
#     print(f"Age + 10 = {age + 10}")

# save_data('Adi', 20)
# save_data(20, 'Adi')
# keyword args
# save_data(age=20, name='Adi')
# def printinfo(name, age = 26):
#     '''This prints a passed info into this function'''
#     print("Name : ", name)
#     print("Age : ", age)
#     print("")

#     printinfo( age=50, name='hacktiv*')
#     printinfo( name = 'hacktiv8')

# # Function definition is here
# def printinfo( arg1, *vartuple ):
# # def printinfo(arg1, arg2, arg3, arg4):
#    '''This prints a variable passed arguments'''
#    print('arg1     : ', arg1)
#    print('vartuple : ', vartuple)
#    print('')
   
#    for var in vartuple:
#       print('isi vartuple : ', var) 

# # Now you can call printinfo function
# printinfo( 10 )
# printinfo( 70, 60, 50, "a" )
# printinfo( 70, 60, "a" )

# def penjumlahan_pengurangan(num1, num2):
#     sum = num1 + num2
#     subt = num1 - num2

#     print(f"subt = {subt}")
#     print(f"num1 = {num1}")
#     # return num1 + num2 + num3
#     return sum, subt

# # print(penjumlahan_pengurangan(10, 1))

# penjumlahan_pengurangan(10, 1)

# print(dir())
# # import person2

# import brand
# print(brand.brands)