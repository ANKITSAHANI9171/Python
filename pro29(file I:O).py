#file i/o in python
#python can be use to perform operations on file (read & write data).

#let open, read and close file.

f =open("demo.txt", "r")
data=f.read()
print(data)
print(type(data))
