#dictonary in python
#info is the name of dictonary

info = {                 
  "key" : "value",
  "name": "ankit",
  "learning" : "coding",
  "subject": ["python","java","c"],     #list also make in dict
  "topic": ("dictonary","sets"),        #tuple also make in dict
  "age": 35 

}

print(info)
print(type(info))

print(info["name"])
print(info["subject"])
print(info["age"])