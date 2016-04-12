def find_best_couple(items,credit,price_list):
    for i in range(items-1):
        first_item = price_list[i]
        for j in range(1,items):
            if j == i:
                continue
            else:
                second_item = price_list[j]
                if first_item + second_item == credit:
                    return [i,j]
                else:
                    continue

file = open("A-large-practice.in", 'r')
T = int(file.readline()) # number of iterations
target = open("output.txt", 'w')
for i in range(0, T):
    credit = int(file.readline()) # credit amount
    items = int(file.readline()) # amount of items in store
    price_list = file.readline()
    price_list = [int(k) for k in price_list.split(' ')]
    target.write("Case #%d: %d %d\n" %(i+1, find_best_couple(items,credit,price_list)[0]+1,
                                     find_best_couple(items,credit,price_list)[1]+1))
file.close()
target.close()


