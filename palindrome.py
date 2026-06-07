x= int(input("Enter a number: "))

original_no = x

rev = 0

while x>0:  #121
    digit = x%10 #1 ,  2
    x = x//10  #12  ,
    rev = rev*10 + digit


if rev == original_no:
    return True

else:
    return False
