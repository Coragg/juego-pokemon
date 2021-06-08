import random
import math

def HP(Base):
    Level, IV, EV = 50, 31, 250
    hp=(((((Base+IV)*2)+((math.sqrt(EV))/4))*Level)/100) + Level + 10
    return hp

def modificar(Type,STAB):
    rando= random.uniform(0.85,1)
    mofifier= Type * STAB * rando * 1
    return round(mofifier,2)

