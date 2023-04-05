#!/usr/bin/env python3.11

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    new_arr = arr.copy()
    new_arr.sort()

    new_arr.reverse()


    maximun = new_arr[0]
  
    runner=0

    for i in range(n):
        if new_arr[i] < maximun:
            runner = new_arr[i]
            break
        elif new_arr[i] == maximun:
            runner = maximun

    print(runner)
    
        
    
    