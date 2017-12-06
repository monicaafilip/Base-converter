'''
Created on Nov 17, 2017

@author: Monica
'''
from service.operations import operations
from domain.number import Number
class conversions:
    def __init__(self):
        self.op=operations()
        
    def convert(self,nr,base):
        '''
        convert the number nr in base:base without a specified method
        using the easiest way 
        in:    ->nr: number type
               ->base:an integer number
        out: the converted number (number type)
        '''
        if nr.get_base() in [2,4,8,16] and base in [2,4,8,16]:
            return self.fast(nr,base)
        if nr.get_base()<base:
            return self.substitution(nr, base)
        else:
            return self.succesiveDiv(nr, base)
        
    
    def succesiveDiv(self,nr,base):
        '''
        the succesive division method
        in:    ->nr: number type
               ->base:an integer number
        out: the result (a number type)
        '''
        res=""
        while nr.get_number()!="":
            q,r=self.op.divD(nr.get_number(),self.op.nrIntToString(base),nr.get_base())
            nr.set_number(q.get_number())
            res+=r
        res=Number(res[::-1],base)
        return res
    
    def substitution(self,nr,base):
        '''
        the substitution method
        in:    ->nr: number type
               ->base:an integer number
        out: the result (a number type)
        '''
        res=Number("0",base)
        need=Number("",base)
        a1=[]
        if need.stringToInt(nr.get_number())<base:
            #if the number is smaller than the base then it is a digit for this base
            res.set_number(self.op.intToString(need.stringToInt(nr.get_number())))
        else:
            a1=need.digits(nr.get_number())
            p=0
            need=Number("",10)
        
        while a1!=[]:
            copy=p
            strBase=self.op.intToString(nr.get_base())
            power='1'
            while copy!=0:
                power=self.op.mulNumbers(power,strBase,base).get_number()
                copy-=1
            digit=a1[-1]
            product=self.op.mulNumbers(power,digit,base)
            p+=1
            res.set_number(self.op.addNumbers(res.get_number(),product.get_number(),base).get_number())
            a1=a1[:-1]
        
        return res
    
    @staticmethod
    def power(nr,p):
        '''
        calculate the  2 power on p
        in:  ->nr,p integer numbers
        out:the power (integer number)
        '''
        i=1
        keep=p
        while p*keep<=nr:
            i+=1
            p*=2
        return i
    
    def fast(self,nr,base):
        '''
        convert a number from 2,4,8 in 16 or reverse
        in:    ->nr (number type)
               ->base (integer type)
        out: the converted number (number type)
        '''
        switcher={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101',\
                  '6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011',\
                  'C':'1100','D':'1101','E':'1110','F':'1111'}
        switcher4={'0':'00','1':'01','2':'02','3':'03','4':'10','5':'11',\
                  '6':'12','7':'13','8':'20','9':'21','A':'22','B':'23',\
                  'C':'30','D':'31','E':'32','F':'33'}
        
        need=Number("",10)
        a=need.digits(nr.get_number())
        res=""
      
        if nr.get_base()==2 or nr.get_base()==4:
            p=self.power(base,nr.get_base())
            part=4-p
            a=a[::-1]
            if part!=0:
                while (len(a)%p)!=0:
                    a+='0'
            a=a[::-1]
            while a!=[]:
                whole=""
                copy=p
                if nr.get_base()==4 and base==2:
                    copy//=2
                while copy!=0:
                    whole+=a[-1]
                    copy-=1
                    a=a[:-1]
                whole=whole[::-1]
                if nr.get_base()==2:
                    for i in switcher.keys():
                        if whole==switcher[i][part:4]:
                            res+=i
                            break
                else:
                    for i in switcher4.keys():
                        if whole==switcher4[i][0:part]:
                            res+=i
                            break
                    
            res=res[::-1]
        else:
            p=self.power(nr.get_base(),base)
            part=4-p
            if (nr.get_base()==4 or nr.get_base()==8 or nr.get_base()==16 )and (base==2 or base==4):
                a=a[::-1]
                while a!=[]:
                    whole=a[-1]
                    if base==2:
                        for i in switcher.keys():
                            if whole==i:
                                res+=switcher[i][part:4]
                                break
                    else:
                        for i in switcher4.keys():
                            if whole==i:
                                res+=switcher4[i][0:part]
                                break
                    a=a[:-1]
        while res!="" and res[0]=='0' :
            res=res[1:]
        res=Number(res,base)
        return res
    