import timeDate
import List

def borrowBook():
    chosen = False
    while(True):
        fName = input("Please input the first name of the borrower: ")
        if fName.isalpha():
            break
        print("please enter an alphabet ")
    while(True):
        lName = input("Please input the last name of the borrower: ")
        if lName.isalpha():
            break
        print("please enter an alphabet ")
            
    lend = "Borrower " + fName + lName + ".txt"
    with open(lend,"w+") as s:
        s.write("\t\t\t Library Management System  \n")
        s.write("\t\t\t Borrowed By: " + fName + " " + lName + "\n")
        s.write("\t\t\t Borrowed on date: " + timeDate.date() + " at time: " + timeDate.time() + "\n\n")
        s.write("-------------------------------------------------------------------------------\n")
        s.write("S.N. \t\t BookName \t\t AuthorName \t\t Cost \n" )
        s.write("-------------------------------------------------------------------------------\n")
        
    while chosen == False:
        print("Please select a option below:")
        for i in range(len(List.nameofbook)):
            print("Enter", i, "to borrow book", List.nameofbook[i])
    
        try:   
            entry = int(input())
            try:
                if(int(List.quantityofbook[entry]) > 0):
                    print("Book is available")
                    with open(lend,"a") as s:
                        s.write("1. \t\t" + List.nameofbook[entry] + "\t\t" + List.nameofauthor[entry] + "\t  " + "$" + List.costofbook[entry] + "\n")
                        s.write("-------------------------------------------------------------------------------\n")
                    List.quantityofbook[entry] = int(List.quantityofbook[entry]) - 1
                    with open("inventory.txt","w+") as s:
                        for i in range(5):
                            s.write(List.nameofbook[i] + "," + List.nameofauthor[i] + "," + str(List.quantityofbook[i]) + "," + "$" + List.costofbook[i] + "\n")

                    again = True #For borrowing more than one book
                    number = 1
                    while again == True:
                        option = str(input("Would you like to borrow another book? Enter n for no and y for yes."))
                        if(option.upper() == "Y"):
                            number = number + 1
                            print("Please choose from an option below:")
                            for i in range(len(List.nameofbook)):
                                print("Enter", i, "to borrow book", List.nameofbook[i])
                            entry = int(input())
                            if(int(List.quantityofbook[entry]) > 0):
                                print("The selected book is currently available")
                                with open(lend,"a") as s:
                                    s.write(str(number) + ". \t\t" + List.nameofbook[entry] + "\t\t" + List.nameofauthor[entry] + "\t\t  " + "$" + List.costofbook[entry] + "\n")
                                    s.write("-------------------------------------------------------------------------------\n")
                                List.quantityofbook[entry]=int(List.quantityofbook[entry])-1
                                with open("inventory.txt","w+") as s:
                                    for i in range(5):
                                        s.write(List.nameofbook[i] + "," + List.nameofauthor[i] + "," + str(List.quantityofbook[i]) + "," + "$" + List.costofbook[i] + "\n")
                                        chosen = False
                            else:
                                again = False
                                break
                        elif (option.upper() == "N"):
                            print ("Thank you. Please come again. ")
                            print("")
                            again = False
                            chosen = True
                        else:
                            print("Please follow the instructions properly.")
                        
                else:
                    print("The book entered is currently not available.")
                    borrowBook()
                    chosen = False
            except IndexError:
                print("")
                print("Please enter the number of the book correctly.")
        except ValueError:
            print("")
            print("Please follow the instructions.")
