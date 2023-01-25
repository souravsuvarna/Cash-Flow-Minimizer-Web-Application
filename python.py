#!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe
print("Content-Type: text/html\n\n")

import cgi

form = cgi.FieldStorage()

p1 = form.getvalue("p1")

p2 = form.getvalue("p2")

p3 = form.getvalue("p3")



print(p1)

print(p2)

print(p3)

#Dont touch


r0c0 = 0
r0c1 = form.getvalue("r0c1")
r0c2 = form.getvalue("r0c2")

r1c0 = form.getvalue("r1c0")
r1c1 = 0
r1c2 = form.getvalue("r1c2")

r2c0 = form.getvalue("r2c0")
r2c1 = form.getvalue("r2c1")
r2c2 = 0

print("\n")

print(r0c0) 
print(r0c1)
print(r0c2)

print(r1c0) 
print(r1c1)
print(r1c2)

print(r2c0) 
print(r2c1)
print(r2c2)


