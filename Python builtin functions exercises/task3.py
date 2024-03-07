def isPalindrome(s):
    x = ''.join(reversed(s))
    if (s == x):
        return True
    return False
 
s = str(input())
z = isPalindrome(s)
 
if (z):
    print("Yes")
else:
    print("No")