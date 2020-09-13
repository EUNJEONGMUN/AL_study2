#11399 ATM
#20200913

def solution(time_list):
    answer = 0
    my_sum = 0
    for i in time_list:
        answer += i
        my_sum+=answer
        

    print(my_sum)

n = int(input())
time = list(map(int,input().split()))
time.sort()
solution(time)
