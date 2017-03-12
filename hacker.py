def rotate(n, s):
    r = ""
    for idx in range(len(s)-1, -1, -1):
        r = r + s[idx]
    return r

s = "racecar"
print(isPalindrome(s))
