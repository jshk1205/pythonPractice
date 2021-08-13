for _ in range(0, int(input())):
    num_list = list(map(int, input().split()))
    even_list = []
    for i in range(0, len(num_list)):
        if num_list[i] % 2 ==0:
            even_list.append(num_list[i])
    print(sum(even_list), min(even_list))