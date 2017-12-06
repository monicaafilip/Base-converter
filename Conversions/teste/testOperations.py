'''
Created on Nov 21, 2017

@author: Monica
'''
from service.operations import operations
from domain.number import Number
def testOperations():
    op=operations()
    digit=12
    base=11
    d,t=op.verifDigit(digit,base)
    assert d==1 and t==1
    
    nr=13
    assert op.intToString(nr)=='D'
    nr1="47"
    nr2="55"
    res=Number("124",8)
    assert op.addNumbers(nr1,nr2,8)==res
    
    nr1="100"
    nr2="1"
    res=Number("11",2)
    assert op.decreaseNumbers(nr1,nr2,2)==res
    
    nr1="B2"
    nr2="B"
    res=Number("7A6",16)
    assert op.mulNumbers(nr1,nr2,16)==res
    
    nr1="873"
    digit="5"
    res=Number("167",9)
    r="4"
    result,rest=op.divD(nr1,digit,9)
    assert result==res and r==rest
    