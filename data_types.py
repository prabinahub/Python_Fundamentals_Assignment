#initialization of variable
i = int
i1 = int
f = float
f1 = float
s = str
s1 = str
b = bool
b1 = bool


# Operators on the variables
i= 10
i1= 3
print(f"The sum of {i} and {i1} = {i+i1}")

f=3.04
f1=2.67
print(f"The sum of {f} and {f1} is {f+f1}")

s=" Hey"
s1=" You"
print(s+s1)

b = True
b1 = False

and_opt= b and b1
or_opt= b or b1


#Dictionary to store the variables by basedon their types as keys  e.g., float[20,50]

dict={
    "int":[i, i1],
    "float":[f,f1],
    "str":[s,s1],
    "bool":[b,b1,and_opt,or_opt]
}

print("\nThe data in the dictionary are:")
for data_types, values in dict.items():
    print(f"{data_types}: {values}")