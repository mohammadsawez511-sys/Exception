#   example 1
for i in range(4):
    try:
        p1 = int(input("enter number :"))
        p2 = int(input("enter number :"))
        print("DIVISION =",p1/p2)

    except Exception as s:
        print(s)    
    

#exampe 2
try:
    with open("main1.py","r") as f:
       
        print(f.read())
        f.close()
            

        

except:
    print("file not found")    


