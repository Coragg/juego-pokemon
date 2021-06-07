import random

def suma(sumando1: eval, sumando2: eval):
    return sumando1 + sumando2

def modificar(Type,STAB):
    rando= random.uniform(0.85,1)
    mofifier= Type * STAB * rando * 1
    return round(mofifier,2)

hola= modificar(5,2)
print(hola)
