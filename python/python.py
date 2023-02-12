#!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe
print("Content-Type: text/html\n\n")

import cgi

form = cgi.FieldStorage()

p1 = form.getvalue("p1")

p2 = form.getvalue("p2")

p3 = form.getvalue("p3")



# print(p1)

# print(p2)

# print(p3)

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

# print(r0c0) 
# print(r0c1)
# print(r0c2)

# print(r1c0) 
# print(r1c1)
# print(r1c2)

# print(r2c0) 
# print(r2c1)
# print(r2c2)

#Test Complete


import subprocess

# Set of integers to pass
vars = [r0c0, r0c1, r0c2, r1c0, r1c1, r1c2, r2c0, r2c1, r2c2,p1,p2,p3]


# Pass vars to test.py 
output = subprocess.run(["python", "test.py"] + [str(i) for i in vars], capture_output=True)

# Output will be in bytes, so we need to decode it
output = output.stdout.decode()



# Print the output
#print(f"<h1>{output}</h1>")


#Dont touch above

#From this onwards we uing html to print


print("<html>")
print("<head>")

print("<title>Result</title>")
print("""<style> 
        body{
            background-color:#F7F7F7;
        }
        h1{
            padding-top:25px;
            color:#727CF5;
            text-align:center;
            font-family: verdana;
            font-weight: bold;
            font-size: 70px;
            -webkit-text-stroke: 0.25px #000000;
            
        }
        p{  
            color:#15202B;
            font-family: Arial, Helvetica, sans-serif;
            font-weight: bold;
            font-size:40px;
            text-align:center;
            padding:50px;
        }
    </style>""")
print("</head>")
print("<body>")
print("<h1>Result</h1>")
print(f"<p>{output}</p>")
print("</body>")
print("</html>") 


#Page set 