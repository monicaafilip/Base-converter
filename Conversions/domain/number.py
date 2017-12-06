class Number:
    def __init__(self,num,base):
        self.__number=num
        self.__base=base

    def get_number(self):
        return self.__number
    
    def get_base(self):
        return self.__base

    def set_number(self, value):
        self.__number = value


    def set_base(self, value):
        self.__base = value


    def del_number(self):
        del self.__number


    def del_base(self):
        del self.__base

    def __eq__(self,other):
        return self.__number==other.__number
    
    def digits(self,stringNr):
        array=[]
        copy=stringNr
        while len(copy)!=0:
            array.append(copy[-1])
            copy=copy[:-1]
        return array[::-1]
    
    def modifyChar(self,char):
        if ord(char)>=97:
            char=chr(ord(char)-32)
        return ord(char)-55
    
    def stringToInt(self,char):
        if len(char)>=2:
            return self.nrStringToInt(char)
        elif ord(char)<=57 and ord(char)>=48:
            return int(char)
        else:
            return int(self.modifyChar(char))
    
    def nrStringToInt(self,nr):
        res=0
        p=1
        while len(nr)!=0:
            d=nr[-1]
            res=res+self.stringToInt(d)*p
            p*=10
            nr=nr[:-1]
        return res

