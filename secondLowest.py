if __name__ == '__main__':
    secondBest = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        secondBest[name]=score
    print(secondBest)