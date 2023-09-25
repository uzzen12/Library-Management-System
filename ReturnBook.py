import List
import timeDate
def returnBook():
    chosen = False
    while(True):
        fName = input(" Please input the first name of the borrower: ")
        if fName.isalpha():
            break
        print("please enter an alphabet ")
    while(True):
        lName = input(" Please input the last name of the borrower: ")
        if lName.isalpha():
            break
        print("please enter an alphabet ")
    lend = "Borrower " + fName + lName + ".txt"
    try:
        with open(lend,"r") as s:
            text = s.readlines()
            text = [v.strip("$") for v in text]
    
        with open(lend,"r") as s:
            info = s.read()
            print(info)
    except:
        print("The name entered is either incorrect or does not exist")
        returnBook()

    give = "Returner " + fName + lName + ".txt"
    with open(give,"w+")as s:
        s.write("\t\t\t Library Management System \n")
        s.write("\t\t\t Returned By: "+ fName + lName +"\n")
        s.write("\t\t\t Returned on date: " + timeDate.date() + " at time: " + timeDate.time() + "\n\n")
        s.write("-------------------------------------------------------------------------------\n")
        s.write("S.N.\t\tBookname\t\tAuthorName\t\tCost\n")
        s.write("-------------------------------------------------------------------------------\n")

    finalTotal = 0.0
    for i in range(5):
        if List.nameofbook[i] in info:
            with open(give,"a") as s:
                s.write(str(i + 1) + "\t\t" + List.nameofauthor[i] + "\t\t" + List.nameofbook[i] + "\t\t$" + List.costofbook[i] + "\n")
                List.quantityofbook[i] = int(List.quantityofbook[i]) + 1
            finalTotal += float(List.costofbook[i])
            
    print("\t\t\t\t\t\t\t" + "$" + str(finalTotal))
    print("Are you returning the book after the due date?")
    print("Enter Y for yes and N for no")
    ans = input()
    if(ans.upper() == "Y"):
        print("How many days has gone by since the expiry date?")
        day = int(input())
        fine = 1 * day
        with open(give,"a")as s:
            s.write("-------------------------------------------------------------------------------\n")
            s.write("\t\t\t\t\tFine: $" + str(fine) + "\n")
        finalTotal = finalTotal + fine
    
    print("Final Total: "+ "$" + str(finalTotal))
    with open(give,"a")as s:
        s.write("\t\t\t\t\tFinal Total: $" + str(finalTotal) + "\n")
        s.write("-------------------------------------------------------------------------------")
        
    with open("inventory.txt","w+") as s:
            for i in range(5):
                s.write(List.nameofbook[i] + "," + List.nameofauthor[i] + ","+str(List.quantityofbook[i]) + ","+"$"+ List.costofbook[i] + "\n")
