def isValid(s):
    flag = 0
    for i in range(len(s)):
        if s[i] == "(":
            for x in s[i+1:]:
                
                if x == ")":
                    flag = 1

        elif s[i] == "[":
            for x in s[i+1 :]:
                if x == "]":
                    flag = 1

        elif s[i] == "{":
            for x in s[i+1 :]:
                if x == "}":
                    flag = 1
    if flag == 1:
        return 'True'
    return 'False'


st = input('Enter a str :')
res = isValid(st)
if res == 'True' :
    print('true')
else:
    print('false')
                    
