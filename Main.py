import ReturnBook
import List
import BorrowBook

def main():
    while(True):
        print(" ----->Welcome. You are accessing the Library Management System<-----")
        print("---------------------------------------------------------------------")
        print("To display all the books that are available in the library, Press 1")
        print("To borrow a book, Press 2")
        print("To return a book, Press 3")
        print("To exit the Library Management System, Press 4")
        try:
            choice = int(input("Please choose from an option mentioned above: "))
            print()
            if(choice == 1):
                with open("inventory.txt","r") as s:
                    text = s.read()
                    print(text)
                    print ()
            elif(choice == 2):
                List.list()
                BorrowBook.borrowBook()
            elif(choice == 3):
                List.list()
                ReturnBook.returnBook()
            elif(choice == 4):
                print("Thank you very much for using the library management system")
                break
            else:
                print("The choice entered is not valid. Please enter a valid choice.")
        except ValueError:
            print("Please enter the correct input.")
main()
