import requests
import sys
from routerModules import zyxel

if len(sys.argv) < 2:
    print("Enter password list filne name at the end")
    exit()
file = str(sys.argv[1])
passwordList = open(file,'r')

print('''
 1-Zyxel
''')
settings = int(input("-> "))

if settings == 1:
    zyxel.exec(passwordList)
    passwordList.close()


