n = int(input('Для какого числа (3..20) сгенерировать ключ?  '))
for i in range (1, n):
    for j in range (i, 20):
        if n % (i + j) == 0:
            if i != j:
                print(n,'-=-',i,'+',j)