# Test for equality
car = 'bmw'
car == 'bmw'
print("True")

print("\n")
car = 'audi'
car == 'bmw'
print("False")

# Test inequality with strings
car = 'supercar'
if car != 'supercar':
    print(" I need a Lamborghini! ")

# Test using the lower() method
car = 'Toyota'
car.lower()== 'toyota'
print('True')
print(car)

# Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
answer = 10
if answer != 30:
    print("That is not the correct answer.")

age = 19
age < 21
print('True')
age = 19
age <= 21
print('False')
age = 19
age > 21
print('False')
age = 19
age >= 21
print('False') 

# Tests using the and keyword and the or keyword

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
print('False') 
age_1 = 22
age_0 >= 21 and age_1 >= 21
print('True') 

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
print('True')
age_0 = 18
age_0 >= 21 or age_1 >= 21
print('False') 

# Test whether an item is in a list

fruits = ['apple', 'banane', 'pineapple']
if 'apple' in fruits
    print('True')
if 'orange' in fruits
    print('False')

# Test whether an item is not in a list

players = ['neymar', 'carlos', 'cafu']
player = 'ronaldo'
if player not in players:
    print(f"{player.title()}, is not on this list.")