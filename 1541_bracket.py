#1541 잃어버린 괄호
#202020913

def solution(my_list):

    my_answer = 0

    for i in range(len(my_list)):
        temp = list(map(int,my_list[i].split('+')))
        temp_sum = 0
        for j in temp:
            temp_sum += int(j)

        if i != 0:
            my_answer -= temp_sum
        else:
            my_answer += temp_sum


    print(my_answer)




n = list(map(str,input().split('-')))
solution(n)
