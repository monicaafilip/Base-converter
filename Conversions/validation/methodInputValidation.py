'''
Created on Nov 21, 2017

@author: Monica
'''
from service.conversions import conversions

class methodExceptions(Exception):
    pass
class methodInputValidation:
    def validateDivision(self,nr,base):
        '''
        validates the number's base
        to be sure that it isn't smaller than the given base
        in:   ->nr(number type)
              ->base (integer number)
        '''
        if nr.get_base()<base:
            raise methodExceptions("The number's base must be bigger than the given base!\n")
        
    def validateSubstition(self,nr,base):
        '''
        validates the number's base
        to be sure that it isn't bigger than the given base
        in:   ->nr(number type)
              ->base (integer number)
        '''
        if nr.get_base()>base:
            raise methodExceptions("The number's base must be smaller than the given base!\n")  
        
    def validateFast(self,base):
        '''
        validates the base to be only 2,4,8 or 16 
        in: base(integer number)
        '''
        if base not in [2,4,8,16]:
            raise methodExceptions("The base must be 2,4,8 or 16!\n")
            
    def validateBasesFast(self,b1,b2):
        '''
        validates the bases to be sure that one is the power to other one
        '''
        c=conversions()
        if (b1< b2 and b1**c.power(b2,b1)!=b2) or (b2<b1 and b2**c.power(b1,b2)!=b1):
            raise methodExceptions("Number not converted, because the bases must be one the power of other one!\n")