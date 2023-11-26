def inputN(msg):
    while True:
        n = int(input(msg))
        if n > 0:
            break
        else:
            print("Внимание! Введено не правильное число. Попробуйте еще раз.")
    return n

def showTable(N):
    for i in range(1,N+1):
        for j in range(1,N+1):
            print(F"{i}*{j}={i*j}")
        print()

numberN=inputN("Введите число N, с 1 до 9:")
showTable(numberN)