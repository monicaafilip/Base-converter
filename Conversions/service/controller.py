'''
Created on Nov 17, 2017

@author: Monica
'''
import copy
class controller:
    def __init__(self,operations,conversions):
        self.__operations=operations
        self.__conversions=conversions

    def intToString(self,digit):
        '''
        convert an integer digit into a string
        '''
        return self.__operations.intToString(digit)
   
    def nrIntToString(self,nr):
        '''
        convert an integer number into a string
        '''
        return self.__operations.nrIntToString(nr)
        
    def convertNr(self,nr,base):
        '''
        convert a number type in the base given
        in:      ->nr:number type
                ->base:int number
        out:a number type
        '''
        keep=copy.deepcopy(nr)
        return self.__conversions.convert(keep,base)
    
    def addNumbers(self,nr1,nr2,base):
        '''
        add two numbers in a given base
        in:   ->nr1,nr2:number type
              ->base: int number
        out:sum (a number type)
        '''
        n1=nr1.get_number()
        n2=nr2.get_number()
        if nr1.get_base()!=base:
            n1=self.convertNr(nr1,base).get_number()
        if nr2.get_base()!=base:
            n2=self.convertNr(nr2,base).get_number()
        return self.__operations.addNumbers(n1,n2,base)
  
    def decreaseNumbers(self,nr1,nr2,base):
        '''
        decreases two numbers in a given base
        in:   ->nr1,nr2 :number type
              ->base:int number
        out:difference (a number type)
        '''
        n1=nr1.get_number()
        n2=nr2.get_number()
        if nr1.get_base()!=base:
            n1=self.convertNr(nr1,base)
        if nr2.get_base()!=base:
            n2=self.converNr(nr2,base)
        return self.__operations.decreaseNumbers(n1,n2,base)
    
    def multiplyNumber(self,nr,digit,base):
        '''
        multiply the number with the digit in the given base
        in:    ->nr:number type
               ->digit:string number
               ->base:int number
        out:the product (a number type)
        '''
        n=nr.get_number()
        if nr.get_base()!=base:
            n=self.convertNr(nr,base).get_number()
        return self.__operations.mulNumbers(n,digit,base)
        
    def divideNumber(self,nr,digit,base):
        '''
        divide the number with the digit in the given base
        in:    ->nr:number type
               ->digit:string number
               ->base:int number
        out:the product (a number type)
        '''
        n=nr.get_number()
        if nr.get_base()!=base:
            n=self.convertNr(nr,base).get_number()
        return self.__operations.divD(n,digit,base)
    
    def convertDiv(self,nr,base):
        '''
        converts a number in a given base with succesive division method
        in: ->nr (number type)
            ->base integer number
        out: a number type
        '''
        return self.__conversions.succesiveDiv(nr,base)
    
    
    def convertSubstitution(self,nr,base):
        '''
        converts a number in a given base with substitution method
        in: ->nr (number type)
            ->base integer number
        out: a number type
        '''
        return self.__conversions.substitution(nr,base)
    
    def fast(self,nr,base):
        '''
        converts a number in a base which is 2,4,8,or 16 and uses the tables for fast conversions
        in:    ->nr(number type)
               ->base(integer number)
        out:the converted nr(a number type)
        '''
       
        return self.__conversions.fast(nr,base)