import pickle

def custmenu():
    while True:
        print('------------------------------------------------------')
        print('            ~CUSTOMER MENU~')
        print('------------------------------------------------------')
        print("Press 1 to sign up.")
        print("Press 2 to log in.")
        print("Press 3 to view deals")
        print("Press 4 to check the price of a product")
        print("Press 5 to exit")
        print('------------------------------------------------------')
        cho=int(input("Enter your choice here:"))
        print('------------------------------------------------------')
        if cho==1:
            custsignup()
        elif cho==2:
            custlogin()
        elif cho==3:
            deals()
        elif cho==4:
            prodprice()
        elif cho==5:
            break
        else:
            print("*Invalid input*")
            custmenu()

def empmenu():
    while True:
        print('------------------------------------------------------')
        print('          ~EMPLOYEE MENU~')
        print('------------------------------------------------------')
        print("Press 1 log in")
        print("Press 2 to view all products")
        print("Press 3 to check product status")
        print("Press 4 to check the price of a product")
        print("Press 5 to view product details")
        print("Press 6 to restock a product")
        print("Press 7 to exit")
        print('------------------------------------------------------')
        cho=int(input("Enter your choice here:"))
        print('------------------------------------------------------')
        if cho==1:
            empdet()
        elif cho==2:
            dispprod()
        elif cho==3:
            prodstat()
        elif cho==4:
            prodprice()
        elif cho==5:
            proddet()
        elif cho==6:
            prodstock()
        elif cho==7:
            break
        else:
            print("*Input invalid*")
            empmenu()

def bossmenu():
    while True:
        print('------------------------------------------------------')
        print('              ~BOSS MENU~')
        print('------------------------------------------------------')
        print("Press 1 to view deals")
        print("Press 2 to add a new employee")
        print("Press 3 to display records of all employees")
        print("Press 4 to display records of all customers")
        print("Press 5 to display records of all products")
        print("Press 6 to display salaries of all employees")
        print("Press 7 to display details of an employee")
        print("Press 8 to exit")
        print('------------------------------------------------------')
        cho=int(input("Enter your choice here:"))
        print('------------------------------------------------------')
        if cho==1:
            deals()
        elif cho==2:
            newemp()
        elif cho==3:
            dispemp()
        elif cho==4:
            dispcust()
        elif cho==5:
            dispprod()
        elif cho==6:
            empsal()
        elif cho==7:
            empdet()
        elif cho==8:
            break
        else:
            print("*Input invalid*")
            bossmenu()

def empdet():
    f=open('emp.dat','rb')
    ec=int(input('Enter your employee code: '))
    ep=input('Enter your employee password: ')
    print('------------------------------------------------------')
    print(               '~Your Details~')
    print('------------------------------------------------------')
    try:
        while True:
            rec=pickle.load(f)
            if rec[0]==ec and rec[2]==ep:
                print(rec)
                break
    except:
        print("*Wrong id or password*")
        f.close()

def newemp():
    f=open('emp.dat','ab')
    print('------------------------------------------------------')
    print('          Entry of new employee')
    print('------------------------------------------------------')
    rec=[]
    ecode=int(input("Enter the employee code: "))
    ename=input("Enter the employee name: ")
    epass=input("Enter the employee password: ")
    esal=int(input("Enter the employee salary: "))
    bonus=float(input("How much bonus you wish to add: "))
    rec=[ecode,ename,epass,esal,bonus]
    pickle.dump(rec,f)
    print('------------------------------------------------------')
    print('              ~Data entered~')
    f.close()

def dispemp():
    f=open('emp.dat' ,'rb')
    print('------------------------------------------------------')
    print('        ~EMPLOYEES DATA~')   
    print('------------------------------------------------------')
    try:
        while True:
            rec=pickle.load(f)
            print(rec)
    except:
        f.close()

def dispcust():
    f=open('customer.dat' ,'rb')
    print('------------------------------------------------------')
    print('          ~CUSTOMER DATA~')
    print('------------------------------------------------------')
    try:
        while True:
            rec=pickle.load(f)
            print(rec)
    except:
        f.close()

def dispprod():
    import pickle
    f=open('product.dat' ,'rb')
    print('------------------------------------------------------')
    print('            ~ALL PRODUCTS~')
    print('------------------------------------------------------')
    try:
        while True:
            rec=pickle.load(f)
            print(rec)
    except:
        f.close()

def empsal():
    f=open('emp.dat' ,'rb')
    print('------------------------------------------------------')
    print('         ~EMPLOYEE SALARY~')
    print('------------------------------------------------------')
    try:
        while True:
            rec=pickle.load(f)
            print(rec[0],',',rec[1],',',rec[3])
    except:
        f.close()

def custsignup():
    f=open('customer.dat','ab')
    print('------------------------------------------------------')
    print("    ~~~SIGN UP IN PROCESS~~~")
    print('------------------------------------------------------')
    rec=[]
    cname=input("Customer name: ")  
    cno=int(input("Customer phone number: "))
    cid=input("Customer id: ")
    city=input('Customer city name: ')
    points=int(input('Enter the points gained: '))
    rec=[cname,cno,cid,city,points]
    pickle.dump(rec,f)
    print('~Account created~')    
    f.close()


def custlogin():
    f=open('customer.dat','rb')
    print('------------------------------------------------------')
    print('           LOGIN PROCESS')
    print('------------------------------------------------------')
    cc=input('Enter your customer id: ')
    cn=int(input('Enter your phone number: '))
    print('------------------------------------------------------')
    print('                  ~Your Details~')
    print('------------------------------------------------------')
    try:
        while True:
            rec=pickle.load(f)
            if rec[2]==cc and rec[1]==cn:
                print(rec)
                break
    except:
        print("*Wrong id or phone number*")
        f.close()

def deals():
    print('                         ~DEALS~')
    print('~Get 20% off on all personal care products on points upto 500~')
    print('~Get 10% off all products using xyz credit/debit card~')
    print('~Get upto 500/- on purchase above 2000/-~')
    print('~Get 30% off on purchase above 5000/-~')
    print('~Use code DIWALI2022 and get upto 20% off on decorative items~')
    print('~For festive offers, contact your nearest store~')

def prodprice():
    f=open('product.dat' ,'rb')
    pc=int(input('Enter product code to check the price:'))
    print('------------------------------------------------------')
    print('             ~Product Details~')
    print('------------------------------------------------------')
    try:
        while True:
            rec=pickle.load(f)
            if rec[1]==pc:
                print(rec[1],',',rec[0],',',rec[4])
                break
    except:
        print('*Invalid Product Code*')
        f.close()
        
def prodstat():
    f=open('product.dat' ,'rb')
    print('------------------------------------------------------')
    print('             ~Product Status~')
    print('------------------------------------------------------')
    try:
        while True:
            rec=pickle.load(f)
            print(rec[1],',',rec[0],',',rec[2])
    except:
        f.close()

def proddet():
    f=open('product.dat' ,'rb')
    print('------------------------------------------------------')
    print('             ~Product Detail~')
    print('------------------------------------------------------')
    pc=int(input("Enter product code to check it's details: "))
    try:
        while True:
            rec=pickle.load(f)
            if rec[1]==pc:
                print(rec)
                break
    except:
        print("*Invalid Product Code*")


def prodstock():
    f=open('product.dat' ,'rb')
    pc=int(input("Enter product code to restock: "))
    print('------------------------------------------------------')
    print('      ~Product Restock In Process~')
    print('------------------------------------------------------')
    try:
        while True:
            rec=pickle.load(f)
            if rec[1]==pc:
                if rec[2]=='IN STOCK':
                    print('Product already in stock')
                elif rec[2]=='OUT OF STOCK':
                    print('Product: ',rec[1],':',rec[0],':','Order sent for restocking')
                break
    except:
        print("*Invalid Product Code*")
        f.close()
        

def mainmenu():
    while True:
        print('------------------------------------------------------')
        print("Hello! Choose your method of interaction:")
        print('------------------------------------------------------')
        print('                 ~MAIN MENU~')
        print('------------------------------------------------------')
        print("Press 1 for Customer access.")
        print("Press 2 for Employee access.")
        print("Press 3 for Boss access.")
        print("Press 4 to exit the system.")
        print('------------------------------------------------------')
        cho=int(input("Enter your choice here:"))
        print('------------------------------------------------------')
        if cho==1:
            custmenu()
        elif cho==2:
            pswd=int(input("Please enter the employee password:"))
            if pswd==123:
                empmenu()
            else:
                print('------------------------------------------------------')
                print("*Incorrect password*")
                mainmenu()
        elif cho==3:
            pswd=int(input("Please enter the boss password:"))
            if pswd==456:
                bossmenu()
            else:
                print('------------------------------------------------------')
                print("*Incorrect password*")
                mainmenu()
        elif cho==4:
            print('          HAVE A NICE DAY!! :)')
            flag=1
            break
        else:
            print('------------------------------------------------------')
            print("*Invalid input*")
            mainmenu()

flag=0
if flag==0:
    mainmenu()




