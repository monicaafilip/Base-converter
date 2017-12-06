'''
Created on Nov 17, 2017

@author: Monica
'''
from domain.number import Number
class operations:
    def verifDigit(self,digit,base):
        '''
        verify if a digit is correct in the given base
        in:   ->digit:a int number
              ->base:a int number
        out:  ->digit and base modified or not
        '''
        if digit<0:
            digit=base+digit
            t=1
        elif digit>=base:
            t=digit//base
            digit%=base
        else:
            t=0
        return digit,t
    
    def intToString(self,d):
        '''
        modify the int d into a string
        '''
        if d>=0 and d<=9:
            return str(d)
        else:
            return chr(d+55)
    
    def nrIntToString(self,nr):
        '''
        modify an integer number into a string
        '''
        res=""
        if nr>=10:
            while nr!=0:
                res+=self.intToString(nr%10)
                nr//=10
            res=res[::-1]
            return res
        else:
            return self.intToString(nr)
    
    def addNumbers(self,nr1,nr2,base):
        '''
        add two numbers with a given base
        in:   ->nr1:a string number
              ->nr2:a string number
              ->base a int number
        out:a number type
        '''
        need=Number("",10)
        a1=need.digits(nr1)
        a2=need.digits(nr2)
        t=0
        res=""
        while a1!=[] and a2!=[]:
            s=need.stringToInt(a1[-1])+need.stringToInt(a2[-1])+t
            s,t=self.verifDigit(s,base)
            res+=self.intToString(s)
            a1=a1[:-1]
            a2=a2[:-1]
        while a1!=[]:
            s=need.stringToInt(a1[-1])+t
            s,t=self.verifDigit(s,base)
            res+=self.intToString(s)
            a1=a1[:-1]
        while a2!=[]:
            s=need.stringToInt(a2[-1])+t
            s,t=self.verifDigit(s,base)
            res+=self.intToString(s)
            a2=a2[:-1]
        if t!=0:
            res+=self.intToString(t)
        res=Number(res[::-1],base)
        return res
    
    def decreaseNumbers(self,nr1,nr2,base):
        '''
        decreases two numbers in a given base
        in:    ->nr1:string number
               ->nr2:string number
               ->base:int number
        '''
        need=Number("",10)
        a1=need.digits(nr1)
        a2=need.digits(nr2)
        t=0
        res=""
        while a1!=[] and a2!=[]:
            dif=need.stringToInt(a1[-1])-need.stringToInt(a2[-1])-t
            dif,t=self.verifDigit(dif,base)
            res+=self.intToString(dif)
            a1=a1[:-1]
            a2=a2[:-1]
        while a1!=[]:
            dif=need.stringToInt(a1[-1])-t
            dif,t=self.verifDigit(dif,base)
            res+=self.intToString(dif)
            a1=a1[:-1]
        while len(res)!=1  and res[-1]=='0':
            res=res[:-1]
        res=Number(res[::-1],base)
        return res
    
    def mulNumbers(self,nr,digit,base):
        '''
        multiply a number with a digit in a given base
        in:    ->nr:string number
               ->digit:a char
               ->base:int number
        out: a number type
        '''
        need=Number("",10)
        d=need.stringToInt(digit)
        a=need.digits(nr)
        t=0
        res=""
        while a!=[]:
                product=need.stringToInt(a[-1])*d+t
                product,t=self.verifDigit(product,base) 
                res+=self.intToString(product)
                a=a[:-1]
        if t!=0:
            res+=self.intToString(t)
        res=Number(res[::-1],base)
        return res
        
    def divD(self,nr,digit,base):
        '''
        multiply a number with a digit in a given base
        in:    ->nr:string number
               ->digit:a char
               ->base:int number
        out:the result (a number type) and the rest a char
        '''
        need=Number("",10)
        res=""
        a=need.digits(nr)
        a=a[::-1]
        d=need.stringToInt(digit)
        q=need.stringToInt(a[-1])//d
        r=need.stringToInt(a[-1])%d
        res+=self.intToString(q)
        a=a[:-1]
        while a!=[]:
            r=r*base
            r+=need.stringToInt(a[-1])
            q=r//d
            res+=self.intToString(q)
            r=r%d
            a=a[:-1]
        res=res[::-1]
      
        while len(res)!=0 and res[-1]=='0':
            res=res[:-1]
        res=Number(res[::-1],base)
        return res,self.intToString(r)
    