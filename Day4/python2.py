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