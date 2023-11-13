

try:
    num = int(input("enter a number : "))
    num1 = int(input("enter a number : "))
    print(num + num1)
except:
    print("exception occur")
else:
    print("program excuted successfully")
finally:
    print("program is completed")
