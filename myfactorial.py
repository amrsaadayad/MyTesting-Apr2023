#testing python, writing a factorial code
#code will get an input number no more than 15 and output the factorial
user_input = input("Enter an integer: ")
try:
    x = int(user_input)
except ValueError:
    print("Invalid input. Please enter an integer.")
if(x>15):
    print("too large for me!")
else:
    Fact=1
    for i in range (1,x+1):
        Fact=Fact*i
        i+=1
    print("the factorial is", Fact)