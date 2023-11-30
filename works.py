from math import *
import random

print("\n-------1--------\n")

t=0
for x in range(1):
    q1 = float(input("number: "))
    if q1.is_integer():
        t+=1
print(t)

print("\n-------2--------\n")

a = int(input("NUmber: "))

for x in range(a):
    print(x+1)

print("\n-------3--------\n")

t=0
while (t<8):
    number = int(input("number int: "))
    if number > 0:
        print(number, "positive")
        t+=1

print("\n-------4--------\n")

for x in range(10,21):
    print(x,"**2 = ",x**2)

print("\n-------5--------\n")

t=0

n=int(input("how many cycles?: "))

while (t<n):
    number = int(input("number int: "))
    if number < 0:
        print(number, "negative")
        t+=1

print("\n-------6--------\n")

n = float(input("Number: "))

if n < 0:
    print(n, " negative")
elif n > 0:
    print(n," positive")

print("\n-------7--------\n")



print("\n-------8--------\n")

for x in range(20):
    print(f"{x+1} inch = {2.5*(x+1)}cm")

print("\n-------9--------\n")

s = float(input("Euro: "))
y = int(input("year: "))
for x in range(y):
    s*=1.03
    print(f"{x+1}y = {round(s,2)}euro")

print("\n-------10--------\n")

for x in range(10):
    a=int(input("a int: "))
    b=int(input("b int: "))
    if a > b:
        print("a bigger")
    elif a < b:
        print("b bigger")
    else:
        print("a==b")

print("\n-------11--------\n")



print("\n-------12--------\n")

nTeam = int(input("how many workers: "))
Time = int(input("how did the worked for?[h]:"))
mTimeH = Time
mTimeM = 0

for x in range(nTeam):
    mTimeH+=Time
    mTimeM+=10

print(f"total work: {mTimeH+(int(mTimeM/60))}h")

print("\n-------13--------\n")
t=0
for x in range(100, 1001):
    if x%7==0:
        print(t+1,x)
        t+=1
print("\nfound",t)

print("\n-------14--------\n")

N = random.randint(1, 100)

for x in range(1, N):
    print(x)

print("\n-------15--------\n")

line = 10
for x in range(line):
    for y in range(line):
        print(y, end=' ', flush=True)
    print()

print("\n-------16--------\n")

line = 9
for x in range(line):
    for y in range(line):
        if x == y:
            z="x"
        else:
            z=0
        print(z, end=' ', flush=True)
    print()

print("\n-------17--------\n")
for x in range(1,10):
    print(f"2*{x}={2*x}")

print("\n-------18--------\n")

for x in range(20,50):
    if x%3 == 0 and x%5 != 0:
        print(x)

print("\n-------19--------\n")

for x in range(35,87):
    if x%7 == 1 or x%7 == 2 or x%7 == 5:
        print(x)

print("\n-------20--------\n")

for x in range(1,51):
    if x%7 == 0 or x%5 == 0:
        print(x)

print("\n-------21--------\n")

t=0
while (t<10):
    number = int(input("number int: "))
    if number > 0:
        print(number)
        t+=1

print("\n-------22--------\n")

for x in range(100, 201):
    if x%17==0:
        print(x)

print("\n-------23--------\n")



print("\n-------24--------\n")

n = int(input("student: "))
h = 0
for x in range(n):
    h+=int(input("student h(cm): "))

print("avg h:", h/n)

print("\n-------25--------\n")
N = int(input("number: "))
t = 0
for x in range(1,N):
    if (x%2 != 0) or (x%3 != 0) or (x%5 != 0):
        print(x)
    

print("\n-------26--------\n")



print("\n-------27--------\n")



print("\n-------28--------\n")

answer = random.randint(1,100)

while True:
    guess = int(input("you can guess 1 to 100"))
    if guess == answer:
        print("you win")
        break

print("\n-------29--------\n")

line = 10
for x in range(line):
    for y in range(line):
        if x == y or y == 0:
            z="x"
        else:
            z=0
        print(z, end=' ', flush=True)
    print()

print("\n-------30--------\n")

n = random.randint(50,100)
m = random.randint(1,50)

for x in range(m, n):
    print(x)

print("\n")

for y in reversed(range(m, n)):
    print(y)

print("\n-------31--------\n")

K = int (input("total cutlets int: "))
M = int (input("total cutlets in pan int: "))
pansfull = int(K/M)
pansmore = int(K%M)

print(f"Total full pans:{pansfull} and no cooked cutlets:{pansmore}")
