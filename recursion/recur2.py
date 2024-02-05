# palindrome via recursion

def pal(s,first, last):
    if first>=last: # >= to consider odd len string too, otherwise == is for even len string
        return "palindrome"
    else:
        if s[first]==s[last] :
            return pal(s,first+1,last-1)
        else:
            return "not palindrome"

s="maaaam"
print(pal(s,0,len(s)-1))