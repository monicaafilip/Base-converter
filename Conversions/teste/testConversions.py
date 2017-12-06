'''
Created on Nov 21, 2017

@author: Monica
'''
from service.conversions import conversions
from domain.number import Number
def testConversions():
    c=conversions()
    nr=Number("6F",16)
    res=Number("111",10)
    assert c.substitution(nr,10)==res
    
    nr=Number("111",10)
    res=Number("6F",16)
    assert c.succesiveDiv(nr,16)==res
    
    nr=Number("179",10)
    res=Number("263",8)
    assert c.succesiveDiv(nr,8)==res
    
    nr=Number("263",8)
    res=Number("179",10)
    assert c.substitution(nr,10)==res
    
    nr=Number("263",8)
    res=Number("179",10)
    assert c.succesiveDiv(nr,10)==res
    
    nr=Number("AB",13)
    res=Number("8D",16)
    assert c.succesiveDiv(nr,16)==res
    

    