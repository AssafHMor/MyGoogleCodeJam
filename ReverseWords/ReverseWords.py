import re
def turn_line_to_list(line):
    return re.sub("[^\w]"," ",line).split()

def reverse_line(line):
    str = ""
    for j in range(len(line)-1,-1,-1):
        str += line[j]+" "

    return str[0:len(str)-1]

file = open('B-small-practice.in','r')
N = int(file.readline()) # number of cases to deal with
target = open('target.txt','w')
for i in range (N):
    line_list = turn_line_to_list(file.readline())
    target.write("Case #%d: %s\n" %(i+1,str(reverse_line(line_list))))
file.close()
target.close()
