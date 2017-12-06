'''
Created on Nov 16, 2017

@author: Monica
'''
from validation.commandValidation import commandValidationExceptions,\
    commandValidation
from validation.numberValidation import validation, validationExceptions
from domain.number import Number
from validation.methodInputValidation import methodExceptions,\
    methodInputValidation
class consoleExceptions(Exception):
    pass
class console:
    def __init__(self,controller):
        self.__controller=controller
        self.__commValid=commandValidation()
        self.__nrValid=validation()
        self.__methValid=methodInputValidation()
        
    def addTwoNr(self,nr1,nr2):
        '''
        add two numbers in one of number's base as the user like
        in:    ->nr1,nr2 :number type
        out: the sum : a number type
        '''
        need=Number("",10)
        print("The base can be "+self.__controller.nrIntToString(nr1.get_base()) +" or " +self.__controller.nrIntToString(nr2.get_base())+"!")
        base=input("Give the base,on which the operation will be done:\n")    
        try:
            self.__nrValid.validateBaseInput(need.stringToInt(base),nr1,nr2)
            base=int(base)
            if base==nr1.get_base():
                nr2.set_number(self.__controller.convertNr(nr2,nr1.get_base()).get_number())
                nr2.set_base(base)
            elif base==nr2.get_base():
                nr1.set_number(self.__controller.convertNr(nr1,nr2.get_base()).get_number())
                nr1.set_base(base)
            return self.__controller.addNumbers(nr1,nr2,base)
        except commandValidationExceptions as ex:
            print(ex)
        
    def addTwoNumberDifBase(self,nr1,nr2,base):
        '''
        add two number in a different base
        in:    ->nr1,nr2:number type
               ->base:int type
        '''
        nr2.set_number(self.__controller.convertNr(nr2,base).get_number())
        nr2.set_base(base)
        nr1.set_number(self.__controller.convertNr(nr1,base).get_number())
        nr1.set_base(base)
        return self.__controller.addNumbers(nr1,nr2,base)
 
    def decrTwoNr(self,nr1,nr2):
        '''
        decreases two numbers in one of number's base as the user like
        in:    ->nr1,nr2 :number type
        out: the sum : a number type
        '''
        need=Number("",10)
        print("The base can be "+self.__controller.nrIntToString(nr1.get_base()) +" or " +self.__controller.nrIntToString(nr2.get_base())+"!")
        base=input("Give the base,on which the operations will be done:\n")    
        try:
            self.__nrValid.validateBaseInput(need.stringToInt(base),nr1,nr2)
            base=int(base)
            if base==nr1.get_base():
                nr2.set_number(self.__controller.convertNr(nr2,nr1.get_base()).get_number())
                nr2.set_base(base)
            elif base==nr2.get_base():
                nr1.set_number(self.__controller.convertNr(nr1,nr2.get_base()).get_number())
                nr1.set_base(base)
            self.__nrValid.decreasesValidation(nr1.get_number(), nr2.get_number())
            return self.__controller.decreaseNumbers(nr1,nr2,base)
        except commandValidationExceptions as ex:
            print(ex)
        
    def decrTwoNumberDifBase(self,nr1,nr2,base):
        '''
        decr two number in a different base
        in:    ->nr1,nr2:number type
               ->base:int type
        out: a number type
        '''
        nr2.set_number(self.__controller.convertNr(nr2,base).get_number())
        nr2.set_base(base)
        nr1.set_number(self.__controller.convertNr(nr1,base).get_number())
        nr1.set_base(base)
        return self.__controller.decreaseNumbers(nr1,nr2,base)
    
    def multiplyD(self,nr,digit):
        '''
        multiply the number with a digit in the number's base
        in:    ->nr (number type)
               -> digit(char)
        out: a number type
        '''
        return self.__controller.multiplyNumber(nr,digit,nr.get_base())
        
    def multiplyDiff(self,nr,digit,base):
        '''
        multiply a number with a digit in a given base
        in: ->number :number type
            ->digit:a char
            ->base:int number
        out: a number type
        '''
        digit=Number(digit,16)
        digit=self.__controller.convertNr(digit,base).get_number()
        return self.__controller.multiplyNumber(nr,digit,base)
        
    def divideD(self,nr,digit):
        '''
        divide a number with a digit in the nr base
        in: ->number :number type
            ->digit:a char
            ->base:int number
        out: a number type
        '''
        return self.__controller.divideNumber(nr,digit,nr.get_base())
      
    def divideDDiff(self,nr,digit,base):
        '''
        divide a number with a digit in a given base
        in: ->number :number type
            ->digit:a char
            ->base:int number
        out: a number type
        '''
        digit=Number(digit,16)
        digit=self.__controller.convertNr(digit,base).get_number()
        return self.__controller.divideNumber(nr,digit,base)
        
    def convertDiv(self,nr, base):
        '''
        converts a number in a given base with succesive division method
        in: ->nr (number type)
            ->base integer number
        out:the converted nr(a number type)
        '''
        return self.__controller.convertDiv(nr,base)
    
    def convertSubstitution(self,nr, base):
        '''
        converts a number in a given base with substitution method
        in: ->nr (number type)
            ->base integer number
        out:the converted nr( a number type)
        '''
        return self.__controller.convertSubstitution(nr,base)
    
    def fastConversions(self,nr,base):
        '''
        converts a number in a base which is 2,4,8,or 16 and uses the tables for fast conversions
        in:    ->nr(number type)
               ->base(integer number)
        out:the converted nr(a number type)
        '''
        return self.__controller.fast(nr,base)
    
    def conversionsIntermediaryBase(self,nr,intermediary,base):
        '''
        converts a number using an intermediary base
        in:   ->nr (number type)
              ->intermediary,base(integer number)
        out:  ->the number converted in intermediary base,then the number converted in base(number type)
        '''
        interm=self.__controller.convertNr(nr,intermediary)
        final=self.__controller.convertNr(interm,base)
        return interm,final
    
    def show(self):
        
        while True:
            print("                                      ~ Monica Olanescu 's application ~")
            print("====Main menu====")
            print("1.Operations")
            print("2.Conversions")
            print("0.Exit\n")
            cmd=input("Give the command:")
            try:
                self.__commValid.validateCommand(cmd,2)
                cmd=int(cmd)
                if cmd==0:
                    break
                elif cmd==1:
                    while True:
                        print("--Operations menu--")
                        print("1.Add")
                        print("2.Decrease")
                        print("3.Multiply with a digit")
                        print("4.Division by a digit")
                        print("0.Back\n")
                        cmd=input("Give the command:")
                        try:
                            self.__commValid.validateCommand(cmd,4)
                            cmd=int(cmd)
                            if cmd==0:
                                break
                            elif cmd==1:
                                print("--Add menu--")
                                print("1.Add two numbers in one of number's base")
                                print("2.Add two numbers in a different base")
                                print("0.Back\n")
                                cmd=input("Give the command:")
                                try:
                                    self.__commValid.validateCommand(cmd,2)
                                    cmd=int(cmd)
                                    if cmd==0:
                                        break
                                    elif cmd==1:
                                        try:
                                            nr=input("Give the first number:")
                                            base=input("Give its base:")
                                            nr1=Number(nr,base)
                                            self.__nrValid.validateNumber(nr1)
                                            nr1.set_base(int(base))
                                            try:
                                                nr=input("Give the another number:")
                                                base=input("Give its base:")
                                                nr2=Number(nr,base)
                                                self.__nrValid.validateNumber(nr2)
                                                nr2.set_base(int(base))
                                                print("The sum is :"+ self.addTwoNr(nr1, nr2).get_number())
                                            except validationExceptions as ex:
                                                print(ex)
                                        except validationExceptions as ex:
                                            print(ex)
                                        
                                    elif cmd==2:
                                        try:
                                            nr=input("Give the first number:")
                                            base=input("Give its base:")
                                            nr1=Number(nr,base)
                                            self.__nrValid.validateNumber(nr1)
                                            nr1.set_base(int(base))
                                            try:
                                                nr=input("Give the second number:")
                                                base=input("Give its base:")
                                                nr2=Number(nr,base)
                                                self.__nrValid.validateNumber(nr2)
                                                nr2.set_base(int(base))
                                                base=input("Give the base on which the operations will be done:")
                                                try:
                                                    self.__nrValid.validateBase(base)
                                                    base=int(base)
                                                    print("The sum is "+self.addTwoNumberDifBase(nr1, nr2, base).get_number())
                                                except validationExceptions as ex:
                                                    print(ex)
                                            except validationExceptions as ex:
                                                print(ex)
                                        except validationExceptions as ex:
                                            print(ex)
                                except commandValidationExceptions as ex:
                                    print(ex)
                    
                            elif cmd==2:
                                while True:
                                    print("--Decrease menu--")
                                    print("1.Decrease two numbers in one of number's base")
                                    print("2.Decrease two numbers in a different base")
                                    print("0.Back\n")
                                    cmd=input("Give the command:")
                                    try:
                                        self.__commValid.validateCommand(cmd,2)
                                        cmd=int(cmd)
                                        if cmd==0:
                                            break
                                        elif cmd==1:
                                            try:
                                                nr=input("Give the first number:")
                                                base=input("Give its base:")
                                                nr1=Number(nr,base)
                                                self.__nrValid.validateNumber(nr1)
                                                nr1.set_base(int(base))
                                                try:
                                                    nr=input("Give the another number:")
                                                    base=input("Give its base:")
                                                    nr2=Number(nr,base)
                                                    self.__nrValid.validateNumber(nr2)
                                                    nr2.set_base(int(base))
                                                    try:
                                                        print("The difference is :"+ self.decrTwoNr(nr1, nr2).get_number())
                                                    except validationExceptions as ex:
                                                        print(ex)
                                                except validationExceptions as ex:
                                                    print(ex)
                                            except validationExceptions as ex:
                                                print(ex)
                                        elif cmd==2:
                                            try:
                                                nr=input("Give the first number:")
                                                base=input("Give its base:")
                                                nr1=Number(nr,base)
                                                self.__nrValid.validateNumber(nr1)
                                                nr1.set_base(int(base))
                                                try:
                                                    nr=input("Give the second number:")
                                                    base=input("Give its base:")
                                                    nr2=Number(nr,base)
                                                    self.__nrValid.validateNumber(nr2)
                                                    nr2.set_base(int(base))
                                                    base=input("Give the base on which the operations will be done:")
                                                    try:
                                                        self.__nrValid.validateBase(base)
                                                        base=int(base)
                                                        try:
                                                            self.__nrValid.decreasesValidation(nr1.get_number(), nr2.get_number())
                                                            print("The difference is :"+ self.decrTwoNumberDifBase(nr1, nr2, base).get_number())
                                                        except validationExceptions as ex:
                                                            print(ex)
                                                    except validationExceptions as ex:
                                                        print(ex)
                                                except validationExceptions as ex:
                                                    print(ex)
                                            except validationExceptions as ex:
                                                print(ex)
                                    except commandValidationExceptions as ex:
                                        print(ex)
                            elif cmd==3:
                                while True: 
                                    print("--Multiply menu--")
                                    print("1.Multiply a number with a digit in the number's base")
                                    print("2.Multiply a number with a digit in a different base")
                                    print("0.Back\n")
                                    cmd=input("Give the command:")
                                    try:
                                        self.__commValid.validateCommand(cmd,2)
                                        cmd=int(cmd)
                                        if cmd==0:
                                            break
                                        elif cmd==1:
                                            try:
                                                nr=input("Give the number:")
                                                base=input("Give its base:")
                                                nr=Number(nr,base)
                                                self.__nrValid.validateNumber(nr)
                                                nr.set_base(int(base))
                                                try:
                                                    digit=input("Give the digit:")
                                                    self.__nrValid.validateDigitB(digit,base)
                                                    print("The product is :"+ self.multiplyD(nr, digit).get_number())
                                                except validationExceptions as ex:
                                                    print(ex)
            
                                            except validationExceptions as ex:
                                                print(ex)
                                        elif cmd==2:
                                            try:
                                                nr=input("Give the number:")
                                                base=input("Give its base:")
                                                nr=Number(nr,base)
                                                self.__nrValid.validateNumber(nr)
                                                nr.set_base(int(base))
                                                try:
                                                    digit=input("Give the digit:")
                                                    self.__nrValid.validateDigit(digit)
                                                    base=input("Give the base on which the operations will be done:")
                                                    try:
                                                        self.__nrValid.validateBase(base)
                                                        base=int(base)
                                                        print("The product is :"+ self.multiplyDiff(nr, digit,base).get_number())
                                                    except validationExceptions as ex:
                                                        print(ex)
                                                    
                                                except validationExceptions as ex:
                                                    print(ex)
            
                                            except validationExceptions as ex:
                                                print(ex)
                                    except commandValidationExceptions as ex:
                                        print(ex)
                               
                            elif cmd==4:
                                while True:
                                    print("--Division menu--")
                                    print("1.Divide a number with a digit in the number's base")
                                    print("2.Divide a number with a digit in a different base")
                                    print("0.Back\n")
                                    cmd=input("Give the command:")
                                    try:
                                        self.__commValid.validateCommand(cmd,2)
                                        cmd=int(cmd)
                                        if cmd==0:
                                            break
                                        elif cmd==1:
                                            try:
                                                nr=input("Give the number:")
                                                base=input("Give its base:")
                                                nr=Number(nr,base)
                                                self.__nrValid.validateNumber(nr)
                                                nr.set_base(int(base))
                                                try:
                                                    digit=input("Give the digit:")
                                                    self.__nrValid.validateDigitB(digit,base)
                                                    q,r=self.divideD(nr,digit)
                                                    print("The quotient is :"+ q.get_number() +" and the remainder:" +r+".\n")
                                                except validationExceptions as ex:
                                                    print(ex)
            
                                            except validationExceptions as ex:
                                                print(ex)
                                        elif cmd==2:
                                            try:
                                                nr=input("Give the number:")
                                                base=input("Give its base:")
                                                nr=Number(nr,base)
                                                self.__nrValid.validateNumber(nr)
                                                nr.set_base(int(base))
                                                try:
                                                    digit=input("Give the digit:")
                                                    self.__nrValid.validateDigit(digit)
                                                    base=input("Give the base on which the operations will be done:")
                                                    try:
                                                        self.__nrValid.validateBase(base)
                                                        base=int(base)
                                                        q,r=self.divideDDiff(nr, digit, base)
                                                        print("The quotient is :"+ q.get_number()+" and the remainder:"+r+".\n")
                                                    except validationExceptions as ex:
                                                        print(ex)
                                                    
                                                except validationExceptions as ex:
                                                    print(ex)
            
                                            except validationExceptions as ex:
                                                print(ex)
                                    except commandValidationExceptions as ex:
                                        print(ex)
                        except commandValidationExceptions as ex:
                            print(ex)
                    
                elif cmd==2:
                    while True:
                        print("--Conversions menu--")
                        print("1.Successive division method")
                        print("2.Substitution method")
                        print("3.Fast conversions between 2,4,16 base")
                        print("4.Conversions with an intermediary base")
                        print("0.Back\n")
                        cmd=input("Give the command:")
                        try:
                            self.__commValid.validateCommand(cmd,4)
                            cmd=int(cmd)
                            if cmd==0:
                                break
                            elif cmd==1:
                                print("Successive division method works better when the number's base is bigger than the base on which we want to convert!")
                                try:
                                    nr=input("Give the number:")
                                    base=input("Give its base:")
                                    nr=Number(nr,base)
                                    self.__nrValid.validateNumber(nr)
                                    nr.set_base(int(base))
                                    try:
                                        base=input("Give the base in which the number will be converted:")
                                        self.__nrValid.validateBase(base)
                                        base=int(base)
                                        self.__methValid.validateDivision(nr, base)
                                        print("The converted number is " +self.convertDiv(nr,base).get_number()+"!\n")
                                    except methodExceptions as ex:
                                        print(ex)
                                    except validationExceptions as ex:
                                        print(ex)
                                    
                                except validationExceptions as ex:
                                    print(ex)
                                
                            elif cmd==2:
                                print("Substitution method works better when the number's base is bigger than the base on which we want to convert!")
                                try:
                                    nr=input("Give the number:")
                                    base=input("Give its base:")
                                    nr=Number(nr,base)
                                    self.__nrValid.validateNumber(nr)
                                    nr.set_base(int(base))
                                    try:
                                        base=input("Give the base in which the number will be converted:")
                                        self.__nrValid.validateBase(base)
                                        base=int(base)
                                        self.__methValid.validateSubstition(nr, base)
                                        print("The converted number is " +self.convertSubstitution(nr,base).get_number()+"!\n")
                                    except validationExceptions as ex:
                                        print(ex)
                                    except methodExceptions as ex:
                                        print(ex)
                                except validationExceptions as ex:
                                    print(ex)
                                
                            elif cmd==3:
                                print("Fast conversions works only between 2,4,8 and 16 base!")
                                print("Take care to have every time a base as a power to the other one!\n Ex: 4=2^2 ; 8=2^3 ;16=4^2 \n ")
                                nr=input("Give the number:")
                                base=input("Give the base:")
                                nr=Number(nr,base)
                                try:
                                    self.__nrValid.validateNumber(nr)
                                    base=int(base)
                                    nr.set_base(base)
                                    try:
                                        base=input("Give the base in which the number will be converted:")
                                        self.__nrValid.validateBase(base)
                                        base=int(base)
                                        self.__methValid.validateBasesFast(base,nr.get_base())
                                        self.__methValid.validateFast(base)
                                        print("The converted number is "+self.fastConversions(nr, base).get_number()+"!\n")
                                    except validationExceptions as ex:
                                        print(ex)
                                except validationExceptions as ex:
                                    print(ex)
                                except methodExceptions as ex:
                                    print(ex)
                            elif cmd==4:
                                nr=input("Give the number:")
                                base=input("Give its base:")
                                nr=Number(nr,base)
                                try:
                                    self.__nrValid.validateNumber(nr)
                                    base=int(base)
                                    nr.set_base(base)
                                    try:
                                        intermediary=input("Give the intermediary base:")
                                        self.__nrValid.validateBase(intermediary)
                                        intermediary=int(intermediary)
                                        base=input("Give the base in which the number will be converted:")
                                        self.__nrValid.validateBase(base)
                                        base=int(base)
                                        intermediaryNumber,finalNumber=self.conversionsIntermediaryBase(nr,intermediary,base)
                                        print("The converted number in intermediary base is: "+intermediaryNumber.get_number()+"!")
                                        print("The converted number is "+finalNumber.get_number()+"!\n")
                                    except validationExceptions as ex:
                                        print(ex)
                                except validationExceptions as ex:
                                    print(ex)
                                except methodExceptions as ex:
                                    print(ex)
                        except commandValidationExceptions as ex:
                            print(ex)
            except commandValidationExceptions as ex:
                print(ex)
            
            
