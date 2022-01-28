# Arithmetic in Phyton; additions, subtractions, multiplyings and divisions. + - * / 

x = 28 # int
y = 28.0 # float

3.14 #float
print(int(3.14))

# ints are narrower than floats
# floats are wider than ints

a = 2 # int
b = 6.0 # float
c = 12 + 0j # complex number

# Rule: Widen numbers so they are the same type

# Addition

a + b # int + float

print(a + b) # result is 8.0 as a float

# Subtraction

b - a # float - int
print(b - a) # result is 4.0 as a float

# Multiplying

a * b # int * float

print(a*b) # Result is 12.0 as a float

# Division

b / a # float / by int
print(b/a) # result is 3.0 as a float

# multiplying int by int

a * 6
print(a*6) #result is 12 as an int. Because int * int will result as int***

# dividing complex number to float

c / b # C is a complex number and b is a float

print(c/b) # Result is 2+oj because 

### exercises

print(16/5) # result is 3.2 as a float

print(20/5) # Result is 4.0 even there is no remainder result is still float

print(16%5) #!!! Result is 1 because py returns the remainder of the long devision if you want the quotion you use 16//5

print(16//5) #Result is 3! so there are 3*5=15 there is a remainder of 1¬!

# You can not divide by 0 it will give a zero error!