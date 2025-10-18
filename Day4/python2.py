import calculator as cal

print(cal.add(5,7))

import qrcode
img = qrcode.make('https://www.naver.com/')
type(img)
img.save('some_file.png')

from os import stat
import requests

url = 'https://www.naver.com/'
response = requests.get(url)

requests.get(url)

items = "zero one two three".split()
print(items)

example = "computer.mokwon.edu"
example.split(".")
a,b,c = example.split(".")
print(a,b,c)

f = lambda x,y: x + y
f1 = f(1,5)
print(f1)

f = lambda x: x**2
f2 = f(3)
print(f2)

f = lambda x: x/2
f3 = f(3)
print(f3)

f = open("dream.txt","r")
contents = f.read()
print(contents)
f.close()

