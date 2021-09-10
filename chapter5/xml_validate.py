xml_str = """<message>
    <body>
        Something
        <p>
        Other thing
        </p>
    </body2>
</message>
"""
stack = []
valid = True
lines = xml_str.splitlines()
for line in lines:
    #if it is start tag, push into stack
    line = line.strip()
    line_length = len(line)
    #print("line ",line)
    if line.startswith("</"): #end tag
        tag = line[2:line_length-1]
        top_of_stack = stack.pop()
        print("End tag ",tag)
        if tag != top_of_stack:
            valid = False
            break
    elif line.startswith("<"): #start tag
        tag = line[1:line_length-1]
        stack.append(tag)
        print("Start tag ",tag)
    else:
        print("Normal line ",line )
if valid == False:
    print ("Invalid ")
elif len(stack) == 0:
    print("Valid")
else:
    print("Invalid")