#Que 1. create a new file "practice.txt" using python . add following data in it.
#Hi everyone
#we are learning file I/O
#using java
#I like programmming in java


#code
#with open("practice.txt" ,"w") as f:
    #f.write("Hi everyone\nWe are learning file I/O \n")
    #f.write("using java.\nI like programming in java,")


#Que 2.write a function that replace all occurance of "java" with "python" in above file


#code   
#with open("practice.txt" ,"r") as f:  
    #data = f.read()

#new_data= data.replace("java", "Python") 
#print(new_data)  


#Que 3.search if th word "learning" exists in the file or not. 

#code
def check_for_word():
    word="learning"
    with open("practice.txt" , "r") as f:
        data = f.read()
        if(data.find(word) != -1 ):
            print("Found")
        else:
            print("Not Found")


check_for_word()   
