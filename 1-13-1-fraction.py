#!/usr/bin/python3
class Fraction:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self) -> str:
        return "{}/{}".format(self.num,self.denom)
    
    def __gcd(self,m,n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

    def __add__(self,other):
       resNum = self.num*other.denom + self.denom*other.num
       resDenom = self.denom*other.denom
       commonDiv = self.__gcd(resNum, resDenom)
       return Fraction(resNum//commonDiv, resDenom//commonDiv)
    
    def __sub__(self, other):
        resNum = self.num*other.denom - self.denom*other.num
        resDenom = self.denom*other.denom
        commonDiv = self.__gcd(resNum, resDenom)
        return Fraction(resNum//commonDiv, resDenom//commonDiv)
    
    def __floordiv__(self, other):
        resNum = self.num / other.num
        resDenom = self.denom / other.denom
        commonDiv = self.__gcd(resNum, resDenom)
        return Fraction(resNum//commonDiv, resDenom//commonDiv)
    
    def __mul__(self, other):
        resNum = self.num * other.num
        resDenom = self.denom * other.denom
        commonDiv = self.__gcd(resNum, resDenom)
        return Fraction(resNum//commonDiv, resDenom//commonDiv)
    
    def __eq__(self, other):
        firstNum = self.num * other.denom
        secondNum = other.num * self.denom
        return firstNum == secondNum
    
print(Fraction(1,2) * Fraction(1,4))
print(Fraction(1,2) == Fraction(1,4))