def char_type(x):
    if (x == '0' or x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9'):
        return 'number'
    elif ( x == '>' or x == '<' or x == ':' or x == ';' or x == '=' or x == '(' or x == ')' or x == '/' or x == '*' or x == '-' or x == '+'):
        return 'special'
    elif (x == 'e'):
        return 'e'
    elif (x == '.'):
        return '.'
    else:
        return 'char'





file = open('test.txt','r')
text = ""
text = file.read()
text = text.strip()


comments = text.split('{')
while comments[0] == '' or comments[0] =='\n':
    del comments[0]

code = ""

for x in range(len(comments)):
    if comments[x].find('}') < 0:
        code += (comments[x])

    else :
        code += ( comments[x].split('}')[1])

code = code.replace('\n',' ')

if code[0] == ' ':
    code = code[1:]

while '  ' in code:
    code = code.replace("  "," ")
    if '   ' in code:
        code = code.replace("   "," ")


iterator = 0
while (len(code) != 0):
    if (char_type(code[0]) == 'char' or char_type(code[0]) == 'e' ):

        if (code[:3] == 'if '):
            print('if, reserved')
            code = code[3:]
        elif (code[:5] == 'then '):
            print('then, reserved')
            code = code[5:]
        elif (code[:5] == 'else '):
            print('else, reserved')
            code = code[5:]
        elif (code[:4] == 'end '):
            print('end, reserved')
            code = code[4:]
        elif (code[:3] == 'end'):
            print('end, reserved')
            code = code[3:]

        elif (code[:7] == 'repeat '):
            print('repeat, reserved')
            code = code[7:]
        elif (code[:6] == 'until '):
            print('until, reserved')
            code = code[6:]
        elif (code[:5] == 'read '):
            print('read, reserved')
            code = code[5:]
        elif (code[:6] == 'write '):
            print('write, reserved')
            code = code[6:]
        else:
            while(char_type(code[iterator]) != 'special' and char_type(code[iterator]) != '.' and code[iterator] != ' ' ):
                iterator += 1
            print (code[:iterator] + ', identifier')
            if code[iterator] == ' ':
                code = code[iterator+1:]
            else:
                code = code[iterator:]
            iterator = 0

    elif char_type(code[0]) == 'number':
        while(char_type(code[iterator]) != 'special' and code[iterator] != ' ' and char_type(code[iterator]) != 'char' ):
            iterator += 1
        print (code[:iterator] + ', number')
        if code[iterator] == ' ':
            code = code[iterator+1:]
        else:
            code = code[iterator:]
        iterator = 0
    elif char_type(code[0]) == 'special':
        if code[0] == ':':
            print(':=, special')
            if (code[2] == ' '):
                code = code[3:]
            else:
                code = code[2:]
        else:
            print(code[0] + ', special')
            if (code[1] == ' '):
                code = code[2:]
            else:
                code = code[1:]
