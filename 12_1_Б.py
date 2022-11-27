def main():
    mx = -100500
    a, n = [], int(input('Кол-во элементов последовательности: '))
    for _ in range(n):
        a.append(int(input()))
    a.append(0)
    
    if len(a) == 0:
        return 0
    else:
        for i in range(len(a)-1):
            if a[i] > mx:
                mx = a[i]
        print(f"Максимальный элемент последовательности: {mx}")
    
main()


