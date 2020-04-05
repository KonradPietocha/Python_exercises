import random

print("Hello World")
if 5 > 2:
    print("time is near")
someNum = 5
message = "Hello, world"
if someNum < 10:
    print(message)
#something not important. I'm just testing comment
"""
some different comment
with multiple lines
"""
num1, num2, text = 1, 2, "sum"
print(text, "is:", num2 + num1)

def my_tech(x, y, z):
    print("I " + x + " " + y + " and " + z)
my_tech("love", "javascript", "python")

def somefun():
    global x
    x = 2
    print(x)
somefun()
print(x)
y = 5j + 3j
print(y)
print(type(y))

print(random.randrange(1, 10))

z = str("s1")
j = float("4")
print(type(z), type(j))

f = open("demofile.txt")
print(f.read())
f.close()
f = open("demofile.html", "w")
f.write("<!DOCTYPE html><html><head><title>test</title></head><body><div><p>some paragraph</p></div></body></html>")
f.close()
mylines = []
f = open("anotherHtml.html")
for myline in f:
    mylines.append(myline)
print(mylines[6])
f.close()