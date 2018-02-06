#!/usr/bin/env python3

# Import statements
#
# # Things from the standard library (i.e., the Python programming language)
import time
#
# # Things from third-parties (i.e., other developers)
import requests
#
# # Things from my computer (i.e., programs that I wrote)
#import other


# Runtime
x = requests.get('https://fred.stlouisfed.org').text
print(x)
