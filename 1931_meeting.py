#1931 회의실배정
#20200905

def solution(M):

    my_list = []
    my_list.append(M.pop(0))

    for i in M:
        if my_list[-1][1]<=i[0]:
            my_list.append(i)

    print(len(my_list))
        
        


N = int(input())
meeting = []

for _ in range(N):
    meeting.append(tuple(map(int,input().split())))

meeting.sort()
meeting.sort(key = lambda x : x[1])
solution(meeting)
