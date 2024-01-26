def isValidate(string):
    s=[]
    for c in string:
        if c=='(':
            s.append(c)
        elif c==')':
            if len(s)==0:
                return 0
            else:
                p=s[-1]
                if p=='(':
                    s.pop()
                else:
                    return 0
    if len(s)==0:
        return 1
    else:
        return 0

str= input("enter a string to validate")
if isValidate(str)==1:
    print("valid para")
else:
    print("invalid")


