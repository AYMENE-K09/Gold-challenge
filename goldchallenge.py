print("enter your birthdate:")
day = int(input("day: "))
month = int(input("mont: "))
year = int(input("year: "))

calcule = 2025 - year
calcule_index = list(str(calcule))
print(f"you are {calcule} years old")
user_candles = int(calcule_index[1])
c = ""
for i in range(user_candles):
    c += "i"

print("    ___",c,"___")
print("   |:H:a:p:p:y:|")
print(" __|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")
