def list():
    global nameofbook
    global nameofauthor
    global quantityofbook
    global costofbook
    nameofbook = []
    nameofauthor = []
    quantityofbook = []
    costofbook = []
    with open("inventory.txt","r") as s:
        
        text = s.readlines()
        text = [u.strip('\n') for u in text]
        for i in range(len(text)):
            no = 0
            for a in text[i].split(','):
                if(no == 0):
                    nameofbook.append(a)
                elif(no == 1):
                   nameofauthor.append(a)
                elif(no == 2):
                    quantityofbook.append(a)
                elif(no == 3):
                   costofbook.append(a.strip("$"))
                no += 1 
