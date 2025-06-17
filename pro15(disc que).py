'''Write a program to enter marks of 3 subject  from the user and store them in dictonary.
start with an empty dictonary & add one by one. use subject name as key and marks as value'''

subject={
    "python": input("python marks :"),
    "c":input("c marks:"),
    "java":  input("java marks: ")
}
print(subject)
print(type(subject))