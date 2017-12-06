'''
Created on Nov 16, 2017

@author: Monica
'''
from teste.runTests import runTests
from UI.uiConsole import console
from service.operations import operations
from service.conversions import conversions
from service.controller import controller

ctrl=controller(operations(),conversions())
c=console(ctrl)
c.show()
runTests()

