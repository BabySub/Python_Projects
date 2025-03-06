def get_number(number): #using functions, inside the brackets is soomething called a parameter, can add multiple parameters using ','
    while True:
        operand =input("number "+ str(number)+ " : ") #seperation by ',' doesnt work inside input statement only inside print it works, use '+' 
        try: 
            return float(operand)
        except: 
            print("INVALID INPUT")

operand1=get_number(1)
operand2=get_number(2)
sign = input("Sign: ")
result=0
if sign=="+":
    result= operand1+ operand2
elif sign=="-":
    result= operand1-operand2
elif sign=="*":
    result= operand1* operand2
elif sign=="/":
    if operand2!=0:
        result= operand1/ operand2
    else:
        print("Error, division by zero result= not defined")

print(result)
