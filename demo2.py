import pickle
f=open('customer.dat','ab')
print('--------------------------------------------')
print("~~~SIGN UP IN PROCESS~~~")
print('--------------------------------------------')
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
