'''젓가락통에 N 종류의 젓가락이 종류별로 충분히 많이 들어있다. 당신은 이 젓가락통에서 무작위로 젓가락을 뽑아서 R 개의 짝을 맞춰야 한다.
최악의 경우 몇 개의 젓가락을 뽑아야 하는가?'''

n, r = map(int, input().split())

print(n+1 + (r-1)*2)




