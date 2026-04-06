import csv

#Open a file to write data into
#file = open("phonebook.csv", "a")

name = input("Name: ")
number = input("Numbers: ")

with open("phonebook.csv","a") as file:
#accessing the writer function to input data in the file
   #writer = csv.writer(file)
    #ensuring I do not have to keep inputting row header multiple times
    writer = csv.DictWriter(file,fieldnames = ["name", "number"])
    writer.writerow({"name": name, "number": number})


#file.close()
