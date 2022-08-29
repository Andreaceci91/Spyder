import turtle
from turtle import Turtle, done

bob = turtle.Turtle()
# print(bob)

'''
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)

turtle.done()
'''

'''
for i in range(4):
    bob.fd(100)
    bob.lt(90)
    
turtle.done()
'''


def quadrato(t, l):
    for i in range(4):
        t.fd(l)
        t.lt(90)
        
        done()
    
#quadrato(bob, 100)


def poligono(t, l, n):
    for i in range(n):
        t.fd(l)
        t.lt(360/n)
        
    done()



def cerchio(t, r):
    circonferenza = 2 * 3.14 * r
    n = 50
    l = circonferenza / n
    
    poligono(t, l, n)
    
    
#cerchio(bob, 150)



def arco(t,r,angolo):
    circonferenza = 2 * 3.14 * r
    n = 50
    l = circonferenza/n
    
    tot = round(n * (angolo/360))+1
    
    for item in range(tot):
        t.fd(l)
        t.lt(360/n)
    turtle.done()

print("******************************")

arco(bob, 50, 180)

n = 3
angolo = 360
    
tot = n * (angolo/360)
print(tot)

    











