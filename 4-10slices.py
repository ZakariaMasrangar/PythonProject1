pizzas =['sicilian pizza','greek pizza','sushi pizza','meatball pizza','hawaiian pizza']
print("the first three items in the list are:")
for pizza in pizzas[:-2]:
    print(pizza.title())

print("\n")
pizzas =['sicilian pizza','greek pizza','sushi pizza','meatball pizza','hawaiian pizza']
print("Three items from the middle of the list are:")
for pizza in pizzas[2:]:
    print(pizza.title())

print("\n")
pizzas =['sicilian pizza','greek pizza','sushi pizza','meatball pizza','hawaiian pizza']
print("The last three items in the list are:")
for pizza in pizzas[-3:]:
    print(pizza.title())