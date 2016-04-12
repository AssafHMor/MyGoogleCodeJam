def turn_word_to_numbers(word):
    str = []
    for char in word:
        value = dict[char]
        if value == '1':
            continue
        else:
            if char
    return str

dict = {'\n':'1',' ':'0', 'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4','h':'44','i':'444','j':'5',
        'k':'55','l':'555','m':'6','n':'66','o':'666','p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88','v':'888',
        'w':'9','x':'99','y':'999','z':'9999'}
file = open("C-small-practice.in",'r')
target = open('output.txt','w')
n = int(file.readline())
for i in range(n):
    target.write(turn_word_to_numbers(file.readline())+"\n")
