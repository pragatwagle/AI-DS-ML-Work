# The program keeps a score and prints winner in a tennis game.
# Date: 06/27/2021
# Author: Pragat Wagle


def point():
    # prompt and take input
    pointWinner = input("Who wins a point. player A or player B? ")

    if pointWinner == 'A' or pointWinner == 'a':
        return 'A' # return A
    elif pointWinner == 'B' or pointWinner == 'b':
        return 'B' # return B
    elif pointWinner == 'Q' or pointWinner == 'q':
        return 'Q'
    else:
        # return E
        return 'E'


def game():
  
    score_A = 0
    score_B = 0

    while True:
        pointWinner = point()
        if pointWinner == 'A':
            score_A += 1
        elif pointWinner == 'B':
            score_B += 1
        elif pointWinner == 'Q':
            print('You quit the game\n')
            break
        elif pointWinner == 'E':
            print('Invalid input. Please enter A, B or Q (to quit).\n')
            continue # restart the loop
        if max(score_A, score_B) >= 4 and abs(score_A - score_B) >= 2:
            if score_A > score_B:
                print('A won\n')
            else:
                print('B won\n')
          
            # return function
            return

        # print the score
        display(score_A, score_B)
  

def display(score_A, score_B):
    scores = [0 , 15, 30, 40]
    # index in scores to get display scores
    dispA = scores[min(score_A, 3)]
    dispB = scores[min(score_B, 3)]

    advA = ""
    advB = ""
    # if decuce
    if score_A >= 3 and score_B >= 3 and abs(score_A - score_B) <= 1:
        if score_A > score_B:
            advA = "Adv"
        elif score_B > score_A:
            advB = "Adv"
  
    # print
    print("Score of Player B:", str(dispB), advB)
    print() # for new line


def main():
    game()


main()


















