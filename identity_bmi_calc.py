name=input("what is your name:\n")
age=input("how old are you:\n")
hight=input("how tall are you:\n"+"metter")
weight=input("how much do you weight:\n"+"kg")
year=input("what is the year now:\n")
number_of_letters=print(f"your name has {len(name)} letters")
brith_year=year-age
print(f"your brith yer is {brith_year}")
bmi=weight/hight*hight
print(f"your bmi is {bmi}")
if bmi>=25:
    print("status=overweight")
else:
    print("status=healthy")
if age>0 or <120:
    print("invailed age entere")
if number_of_letters<3:
    print("name is too short")
