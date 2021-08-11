k = int(input())
for _ in range(0, k):
    p, m = map(int,input().split())
    w_list = []
    m_list = []
    for _ in range(0, p):
        w = int(input())
        w_list.append(w)
    w_list = set(w_list) #중복값 제거
    w_list = list(w_list)
    for i in range(1, m+1):
        m_list.append(i)
    if len(w_list) != m and m != 1:
        print(p - len(w_list))
    elif m == len(w_list) and m != p:
        print(p-m)
    else:
        print(0)