#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

# prediction: 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# prediction: 19
# number 2 won't run as it gives an error that the function is undefined, however it is defined after this call occurs. I believe the answer should be 19 though.


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# prediction: 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# prediction: 5


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# #prediction: print will be 5. x will be null.


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# prediction: Print inside the function will 3 then 5. Print that called the function will be error as you can't add Null to Null

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# prediction: 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# predictions: Print inside the function will be 100. Print that called the functions will be 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# predictions: First print is 7, second print is 14 and final print is 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# predictions: 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

# prediction: First print for "b" is 500. Second print for "b" is 500. Third print for "b" from inside function is 300. Final print for "b" is 500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# prediction: First print for "b" is 500. Second print for "b" is 500. Third print for "b" from inside function is 300. Final print for "b" is 500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# prediction: First print for "b" is 500. Second print for "b" is 500. Third print for "b" from inside function is 300. Final print for "b" is 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# prediction: first print 1. Second print 3. third print 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# prediction: 1 then 3, then 5, then 10