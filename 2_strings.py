str = '''Can't do this thing'''
print(str)

name = "Asraful Naim"
print(name[8:12])
print(name[0:-3])
print(name[-4:-2])
print(len(name))

print(name.upper())
print(name.lower())

str1 = "Naim???"
print(str1.rstrip("?"))
print(str1.replace("Naim???","Naim"))
print(name.split(" "))
str3 = "bangladesh"
print(str3.capitalize())
print(name.count("Naim"))
print(name.endswith("Naim"))
print(name.find("Naim"))
print(name.index("Naim"))
print(name.islower())
print(name.isupper())
print(name.isspace())
print(name.swapcase())