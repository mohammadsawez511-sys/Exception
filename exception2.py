# handle multiple exception 
# handle any type of exception 
# handle custome exception
# use of finally 
# use of else 
class InvalidAgeException(Exception):
     def __init__(self,age,message):
          self.age = age 
          self.message = message
     def __str__(self):
          return f"age is {self.age} and  {self.message}"     
          
try:
        a = int(input("enter number :"))
        b = int(input("enter number :"))
        age = int(input("enter age require for army :"))
        c = "ADDITION : ",a+b
        d = "SEPRATION :",a-b
        e = "MULTIPLICATION :",a*b
        f = "DIVISION :",a/b
        if age<10 or age>50:
             raise InvalidAgeException(age,"age must be between 10 to 50 require for army")
except ZeroDivisionError:
     print("any number is not divisible by zero")        
except InvalidAgeException as e:
     print(e)
     
except ValueError:
     print("string number is not allowed")

except Exception as f:
    print("some error has occured :",f)

else:
    print(c,d,e,f,sep="\n")

finally:
    print("FINISHED !")        
           