# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:15:58 2022

@author: alairtonpereira
"""

import base64

with open("arquivo.pdf", "rb") as pdf_file:
    encoded_string = base64.b64encode(pdf_file.read())
    print(encoded_string)

file_64_decode = base64.b64decode(encoded_string) 
file_result = open('arquivo.pdf', 'wb')
file_result.write(file_64_decode)