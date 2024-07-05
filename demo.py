import pickle
f=open('product.dat','rb')
try:
    while True:
        rec=pickle.load(f)
        print(rec)
except:
    f.close()
        
