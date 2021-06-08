import random
import math

def HP(Base):
    Level, IV, EV = 50, 31, 250
    hp = (((((Base+IV)*2)+((math.sqrt(EV))/4))*Level)/100) + Level + 10
    return hp

def OtherStat(Base):
    Level, IV, EV = 50, 31, 250
    otherstat = 0
    return otherstat

def Modifier(Type,STAB):
    rando= random.uniform(0.85,1)
    mofifier= Type * STAB * rando * 1
    return round(mofifier,2)


def Damage(Power):
    Level=50
    modificar= Modifier(1,2)
    A= 5
    D= 4
