num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
num3=int(input("enter the third number: "))
#maximum
if num1>=num2 and num1>=num3:
    max_num=num1
elif num2>=num1 and num2>=num3:
    max_num=num2
else:
    max_num=num3
#minimum
if num1<=num2 and num1<=num3:
    min_num=num1
elif num2<=num1 and num2<=num3:
    min_num=num2
else:
    min_num=num3

print("maximum among three is: ",max_num)
print("minimum among three is: ",min_num)    

