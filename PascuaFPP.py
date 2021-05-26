#
#Created by: Jeric Pascua, ID: 0005742039
#CRN: 55101, Python Programming
#Project: Final Programming Project, Characters and Strings option

#created strcmp() function that takes two strings as parameters
def strcmp(string1, string2):
    if string1 < string2:    #string1 is printed first
        return -1
    elif string1 > string2:  #string2 is printed first
        return 1
    elif string1 == string2: #order does not matter both are the same name
        return 0

#created printOrder to print strings in alpabetical order
#depends on the integer value returned by strcmp()
def printOrder(value, string1, string2):

    #split first and last names
    fullName1 = string1.split(",")
    fullName2 = string2.split(",")

    #capitalize first and last names, just incase user inputs them as lowercase    
    last1 = fullName1[0].title()
    first1 = fullName1[1].title()
    last2 = fullName2[0].title()
    first2 = fullName2[1].title()

    #if else tree determines which name gets printed first
    if value == -1: 
        print("The names are as follows:")
        print(last1, first1, sep=",")
        print(last2, first2, sep=",")
    elif value == 1:
        print("The names are as follows:")
        print(last2, first2, sep=",")
        print(last1, first1, sep=",")
    elif value == 0:                       #elif statement is for same name case
        print("The names are as follows:")
        print(last1, first1, sep=",")
        print(last2, first2, sep=",")
        print("The names are the same")

def main():
    #take user input of the two names being evaluated
    #checks if string is in format "last, first"
    string1 = (input("Please input the first name\n"))
    while string1.find(",") == -1:
        string1 = (input('Please enter in format "last, first"\n'))

    string2 = (input("Please input the second name\n"))
    while string2.find(",") == -1:
        string2 = (input('Please enter in format "last, first"\n'))

    #assign value to the integer value strcmp() will return
    #applying lower() to the strings to ensure comparisons are in the same case
    value = strcmp(string1.lower(), string2.lower())

    #call printOrder function
    printOrder(value, string1, string2)

if __name__ == '__main__': main()
