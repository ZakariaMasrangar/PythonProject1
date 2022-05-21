import random
import math
num=int(input("Enter a number between 0 && 50 : "))
num_1=float(input("Enter amount : "+"$ "))
if num%2==0:
    print("Even numbers are black")
else:
    print("Odd numbers are red") 
i=1
while i<50:
    print(random.randrange(0, 49), "is the winner number!")
    break
if num_1%3:
    n=num_1%3
    print(math.ceil(n))
    print("le numéro misé par le joueur est de la même couleur que le numéro gagnant est",math.ceil(n),"$")
else:
    print("le joueur perd la somme misée de",math.ceil(n),"$")


           
