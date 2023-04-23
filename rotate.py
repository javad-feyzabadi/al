def rotate(s,k):
    double_s = s + s
    if k <= len(s):
        return double_s[k:k+len(s)]
    else:
        return double_s[k - len(s):k]
    
print(rotate('hello',7))