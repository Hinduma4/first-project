n = int(input("enter the number: "))
temp = n
sum = 0
while(n != 0):
    rem = n % 10
    sum = sum * 10
    sum = sum + rem
    n = n // 10
if(temp == sum):
   print("the number is palindrome")
else:
    print("it is not palindrome")
