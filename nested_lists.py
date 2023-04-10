#!/usr/bin/env python3.11

# return the 2nd lowest score for a given list of scores
       
if __name__ == '__main__':
    scores = []
    
    for i in range(int(input())):  
        name = input()
        score = float(input())
        scores.append([name, score])

    minimun_score = min(scores, key=lambda x: x[1])
    scores = [score for score in scores if score[1] > minimun_score[1]]
    second_lowest_score = min(scores, key=lambda x: x[1])
    scores = [score for score in scores if score[1] == second_lowest_score[1]]

    #sort scores by name
    scores.sort(key=lambda x: x[0])

    for score in scores:
        print(score[0])


    
        

        
