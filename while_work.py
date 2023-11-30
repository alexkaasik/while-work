'''
word0 = 'ajdspawngengowh'

for q in word0:
    print(q)

word0 = str(input)


for x in range(10):
    radius = float(input(f"{x+1} Radius: "))
    if radius > 0:
        s=3.14*radius**2
    else:
        s="R peab > kui 0 olema"
    
    print(f"{x+1} s={s}")

x=0
while True:
    radius = float(input(f"{x+1} Radius: "))
    if radius > 0:
        s=3.14*radius**2
       
    else:
        s="R peab > kui 0 olema"
    
    print(f"{x+1} s={s}")
    x+=1
    if x == 10:
        break

x=0
while (x < 10):
    radius = float(input(f"{x+1} Radius: "))
    if radius > 0:
        s=3.14*radius**2
       
    else:
        s="R peab > kui 0 olema"
    
    print(f"{x+1} s={s}")
    x+=1
 '''

x=0
while True:
    radius = float(input(f"Radius: "))
    if radius > 0:
        s=3.14*radius**2
        x+=1
    else:
        s="R peab > kui 0 olema"
    print(f"s={s}")
   
    if x == 10:
        break