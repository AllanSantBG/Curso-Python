def fatorial(num, show=True):
    f = 1
    print(f'{num}! = ', end='')
    for i in range(num, 0, -1):
        f *= i
        if show == True:
            if i == 1:
                print(i, end=' = ')
            else:
                print(i, end=' * ')
    return f


print(fatorial(2, True))