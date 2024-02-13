def palindrome(y):
    return y == y[::-1]
y = "radar"
ans = palindrome(y)

if ans:
    print("Yes")
else:
    print("No")

y = "madama"
ans = palindrome(y)

if ans:
    print("Yes")
else:
    print("No")

y = "smile"
ans = palindrome(y)

if ans:
    print("Yes")
else:
    print("No")

y = "malayalam"
ans = palindrome(y)

if ans:
    print("Yes")
else:
    print("No")