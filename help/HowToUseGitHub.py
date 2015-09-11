#!/usr/bin/python
from sys import argv
import os
print """
To push all files

git add -A
git commit -m "enter message here"
git push origin master


To push one file

git add (file name or folder name)
git commit -m "enter message here"
git push origin master

Press enter to go back to menu
"""
raw_input("> ")
