# -*- coding: utf-8 -*-
"""    

Created on Tue Feb 19 16:58:28 2019

@author: Aayushi
"""

data=  [ ("Tom",19,80),("John",20,90),  (" Jony",17,91), ("Jony",17,93),("Json",21,85)]
sorted(data,key=lambda tup:(tup[0],tup[1],-tup[2]))
sorted(data,key=lambda tup:(tup[1],tup[0],tup[2]))

