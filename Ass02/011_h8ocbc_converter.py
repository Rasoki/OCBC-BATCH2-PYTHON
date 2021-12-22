def konversi (celcius):
    '''Function to conversion celcius to kelvin and otherwise'''
    kelvin = celcius + 273.15
    celcius = kelvin  - 273.15 

    print(f"{kelvin} Kelvin")
    print(f"{celcius} Celcius")
    return   kelvin, celcius 

konversi (100)
print(konversi.__doc__)
print('')

def fahrenheit_konversi(kelvin, celcius):
    '''Function to conversion celcius and kelvin to fahrenheit'''
    fahrenheit =  9/5 * (kelvin - 273.15) + 32
    fahrenheit2 = 9/5 * celcius + 32 
    
    print(f"{fahrenheit} Fahrenheit")
    print(f"{fahrenheit2} Fahrenheit")
    return fahrenheit, fahrenheit2

fahrenheit_konversi(kelvin=373.15, celcius=100.0)
print(fahrenheit_konversi.__doc__)
print('')

def konversi_fahrenheit(fahrenheit):
    '''Function to conversion fahrenheit to kelvin and celcius'''
    kelvin = 5/9 * (fahrenheit - 32) + 273.15
    celcius = 5/9 * (fahrenheit - 32) 
    print(f"{kelvin} Kelvin")
    print(f"{celcius} Celcius")
    return kelvin, celcius

konversi_fahrenheit(212.0)
print(konversi_fahrenheit.__doc__)