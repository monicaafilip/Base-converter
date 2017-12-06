
'''
Created on Nov 16, 2017

@author: Monica
'''
from domain.number import  Number
from service.operations import operations
class validationExceptions(Exception):
    pass

class validation:
    def validateNumber(self,nr):
        errors=[]
        self.validateBase(nr.get_base())
        self.validateNr(nr.get_number(),nr.get_base(),errors)

        
    def validateBase(self,base):
        '''
        validates the base 
        '''
        errors=[]
        if type(base)!=int:
                try:
                    base=int(base)
                    if base>16 or base<2:
                        errors.append("The base must be between 2 and 16!")
                except ValueError:
                    errors.append("The base can't be string!\n")
        elif base>16 or base<2:
            errors.append("The base must be between 2 and 16!")
        if len(errors):
            raise validationExceptions(errors)
    
    def validateDigitB(self,digit,base):
        '''
        validates a digit to be the digit of a specified base
        digit,base string numbers
        '''
        errors=[]
        need=Number("",10)
        if need.stringToInt(digit)>need.stringToInt(base):
            errors.append("Invalid number!The digits must be between 0 and base-1!\n")
        if digit< '0':
            errors.append("The digit can't be negative!\n")
        
        if len(errors):
            raise validationExceptions(errors)
        
    def validateNr(self,nr,base,errors):
        '''
        validate a number and its digits
        '''
        op=operations()
        need=Number("",10)
        a=need.digits(nr)
        base=int(base)
        for i in range(len(a)):
            self.validateDigitB(a[i],op.intToString(base))
        if len(errors):
            raise validationExceptions(errors)

    def validateDigit(self,digit):
        '''
        validates a digit without taking into account the base
        '''
        errors=[]
        need=Number("",10)
        if need.stringToInt(digit) >16:
            errors.append("Invalid digit!The digit must be smaller than 10!\n")
        if digit< '0':
            errors.append("The digits of number can't be negative!\n")
        if not ((ord(digit)<=57 and ord(digit)>=48)or (ord(digit)<=70 and ord(digit)>=65) or(ord(digit)<=102 and ord(digit)>=97)):
            errors.append("Invalid digit!")        
        if len(errors):
            raise validationExceptions(errors)                   
        
    def validateBaseInput(self,base,nr1,nr2):
        '''
        validates a base given by the user
        base: integer number
        nr1,nr2 :number type
        '''
        if base!=nr1.get_base() and base!=nr2.get_base():
            raise validationExceptions("Invalid base!")
        
    def decreasesValidation(self,nr1,nr2):
        '''
        verify if the first number is bigger than the second one
        nr1,nr2 :string numbers
        ''' 
        if nr1<nr2:
            raise validationExceptions("The operation can't be done!First number must be bigger than the second one!\n")