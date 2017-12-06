'''
Created on Nov 16, 2017

@author: Monica
'''
from domain.number import Number
def testNumber():
    nr=Number("100",2)
    assert nr.get_number()=="100"
    assert nr.get_base()==2
    nr.set_number("12")
    assert nr.get_number()=="12"
    nr.set_base(10)
    assert nr.get_base()==10
    nr2=Number("12",10)
    assert nr==nr2
    
    array=nr.digits(nr.get_number())
    assert array==["1","2"]
    
    char='A'
    assert nr.modifyChar(char)==10
    assert nr.stringToInt(char)==10
    
    char="1"
    assert nr.stringToInt(char)==1
    

