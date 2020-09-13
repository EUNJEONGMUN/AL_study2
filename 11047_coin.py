#11047 동전 0
#20200905

def solution(N,K):

    count = 0

    while K!=0:
        for i in range(N-1):
            if money[i]<=K<money[i+1]:
                K-=money[i]
                count+=1

    print(count)
                
                
            


N,K = map(int,input().split())
money = []
for _ in range(N):
    money.append(int(input()))

solution(N,K)
