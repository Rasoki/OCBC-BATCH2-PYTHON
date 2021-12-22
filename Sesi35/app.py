# f = open("test.txt")
# f = open("test.txt", 'w') # write
# f = open("test.txt", 'a') # oppend
# f = open("test.txt", 'r') # read


# file = open('Hack8_Sample_Text.txt')
# print(file.read(4))
# print(file.read(6))
# print(file.tell())
# file.close()

# files = open('Hack8_Sample_Text.txt')
# files.seek(0)
# for line in files:
#     print(line, end = '')

# #Should be Lesser
# x = 10
# if x > 5:
#     raise Exception ('x should not exceed 5. The value of x was: {}'.format(x))

# #Should be greater
# x = 10
# if x < 5:
#     raise Exception ('x should  exceed 5. The value of x was: {}'.format(x))



# import sys
# assert ('linux' in sys.platform), "This code runs on Linux only."
# assert ('windows' in sys.platform), "This code runs on Windows only."

# x = 22
# # assert x == 20
# assert x == 20, "x harus 20"

# def perkalian_dengan_0(num1):
#     # return 0 * num1
#     return 0 * num1 + 1
# a = 0

# # sepuluh_kali_0 = perkalian_dengan_0(10)
# sepuluh_kali_0 = perkalian_dengan_0(10)
# assert sepuluh_kali_0 == 0, "fungsi masih salah"

# with open('file.log') as file:
#     read_data = file.read()
# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Could not open file.log')
#     print('fle.log is not find in this directory')

import sys
print(sys.platform)
def os_interaction():
    # assert ('linux' in sys.platform), "Function can only run on linux systems."
    assert('win32' in sys.platform), "This code runs on Windows only."
    print('Doing something.')
try: 
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)