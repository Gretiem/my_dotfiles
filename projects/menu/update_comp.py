#!/usr/bin/python
from sys import argv
import os
print """
This will run an update, upgrade, dist upgrade, and then a autoremove.
Do you wish to continue? CNTRL+C if no.
"""
raw_input("> ")
command1 = ("sudo apt-get update")
command2 = ("sudo apt-get upgrade -y")
command3 = ("sudo apt-get dist-upgrade -y")
command4 = ("sudo apt-get autoremove -y")
os.system(command1)
os.system(command2)
os.system(command3)
os.system(command4)

