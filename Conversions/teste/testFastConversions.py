'''
Created on Nov 22, 2017

@author: Monica
'''
from domain.number import Number
from service.conversions import conversions
def testFastConversions():
    c=conversions()
    nr=Number("10010111",2)
    assert c.fast(nr,16).get_number()=='97'
    assert c.fast(nr,16).get_base()==16
    
    nr=Number("10010111",2)
    assert c.fast(nr,4).get_number()=='2113'
    assert c.fast(nr,4).get_base()==4
    
    nr=Number("10010111",2)
    assert c.fast(nr,8).get_number()=='227'
    assert c.fast(nr,8).get_base()==8
    
    nr=Number("1123",4)
    assert c.fast(nr,16).get_number()=='5B'
    assert c.fast(nr,16).get_base()==16
    
    nr=Number("1123",4)
    assert c.fast(nr,2).get_number()=='01011011'
    assert c.fast(nr,2).get_base()==2
    
    nr=Number("1123",16)
    assert c.fast(nr,2).get_number()=='0001000100100011'
    assert c.fast(nr,2).get_base()==2
    
    nr=Number("AB",16)
    assert c.fast(nr,4).get_number()=='2223'
    assert c.fast(nr,4).get_base()==4