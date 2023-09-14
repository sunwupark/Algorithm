X = int(input())
total_list = [64]

while(True):
    if sum(total_list) > X:
        into_half = total_list.pop() / 2
        total_list.append(into_half)
        if(sum(total_list) < X):
            total_list.append(into_half)
    elif sum(total_list) == X:
        print(len(total_list))
        break

