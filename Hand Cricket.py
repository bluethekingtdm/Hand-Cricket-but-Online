'''
This project (game) is fully owned by bluethekingtdm. Enjoy!
'''
#First import 'Random' Module.
import random
#Module imported.
print("Welcome to Online Hand Cricket League, Enjoy!")
a1 = int(input("To chose even, press 0, To chose odd, press 1:"))
score_sys = 0
score_you = 0
#Tossing the Coin.
for a2 in range(0,1):
    a3 = random.randint(1,6)
    a4 = random.randint(0,1)
    a5 = random.randint(1,6)
    #Here only the middle value determines the toss.
    print(a3, end=' ')
    print(a4, end=' ')
    print(a5)
    #You win the toss.
    if a4 == a1:
        a6 = input("You won the toss. Do you want to BAT or BALL first?, Enter 'BAT' for Batting, 'BALL' for Balling:")
        if a6 == 'BAT':
            #You Chose to BAT first.
            #You are Batting.
            print("You are currently BATTING. You have 'SIX OVERS' and '1 WICKET'.")
            for a7 in range(1,37):
                a8 = int(input("Score anywhere between 0-6 using Number Keys: "))
                a9 = random.randint(0,6)
                if a8>6:
                    print("You can't score more than 6 runs a ball.")
                    print("Thanks for playing.")
                    break
                if a8 != a9:
                    score_you = score_you + a8
                elif a8 == a9:
                    print("OUT!")
                    print("Your Score: ", score_you, "System needs", score_you+1, "runs from 'SIX OVERS' to win.")
                    #You are Balling.
                    print("You are currently BALLING.")
                    for a10 in range(1,37):
                        a11 = random.randint(0, 6)
                        a12 = int(input("Catch anywhere between 0-6 using Number Keys: "))
                        if a12>6:
                            print("You can't catch more than 6 in a ball.")
                            print("Thanks for playing.")
                            break
                        if a11 != a12:
                            score_sys = score_sys + a11
                        elif a11 == a12:
                            print("OUT!")
                            # Winner Declaration.
                            if score_sys > score_you:
                                print("System Wins!")
                                print("Thanks for playing.")
                            elif score_sys < score_you:
                                print("You Win!")
                                print("Thanks for playing.")
                            elif score_sys == score_you:
                                print("Game ended in a Tie!")
                                print("Thanks for playing.")
                            break
                        if score_sys > score_you:
                            print("System Wins!")
                        elif score_sys < score_you:
                            print("You Win!")
                        elif score_sys == score_you:
                            print("Game ended in a Tie!")
                            
        elif a6 == 'BALL':
            #You Chose to Ball first.
            #You are Balling.
            print("You are currently BALLING.")
            for a13 in range(1,37):
                a14 = int(input("Catch anywhere between 0-6 using Number Keys: "))
                a15 = random.randint(0,6)
                if a14>6:
                    print("You can't catch more than 6 in a ball.")
                    print("Thanks for playing.")
                    break
                if a15 != a14:
                    score_sys = score_sys + a15
                elif a15 == a14:
                    print("OUT!")
                    print("System's Score ", score_sys, "You need", score_sys+1, "runs from 'SIX OVERS' to win.")
                    #You are Batting.
                    print("You are currently BATTING.")
                    for a16 in range(1,37):
                        a17 = int(input("Score anywhere between 0-6 using Number Keys: "))
                        a18 = random.randint(0,6)
                        if a17>6:
                            print("You can't score more than 6 runs a ball.")
                            print("Thanks for playing.")
                            break
                        if a17 != a18:
                            score_you = score_you + a17
                        elif a17 == a18:
                            print("OUT!")
                            # Winner Declaration.
                            if score_sys > score_you:
                                print("System Wins!")
                                print("Thanks for playing.")
                            elif score_sys < score_you:
                                print("You Win!")
                                print("Thanks for playing.")
                            elif score_sys == score_you:
                                print("Game ended in a Tie!")
                                print("Thanks for playing.")
                            break
                        if score_sys > score_you:
                            print("System Wins!")
                        elif score_sys < score_you:
                            print("You Win!")
                        elif score_sys == score_you:
                            print("Game ended in a Tie!")
    #You lose the toss.
    elif a4 != a1:
        print("You lost the toss. System gets to decide to 'BAT' or 'BALL'.")
        a19 = random.randint(0,1)
        if a19 == 1:
            #System Chose to BAT first.
            #You are Balling.
            print("System decides to 'BAT' first.")
            print("You are currently BALLING.")
            for a20 in range(1,37):
                a21 = int(input("Catch anywhere between 0-6 using Number Keys: "))
                a22 = random.randint(0,6)
                if a21>6:
                    print("You can't catch more than 6 in a ball.")
                    print("Thanks for playing.")
                    break
                if a22 != a21:
                    score_sys = score_sys + a22
                elif a22 == a21:
                    print("OUT!")
                    print("System's Score ", score_sys, "You need", score_sys+1, "runs from 'SIX OVERS' to win.")
                    #You are Batting.
                    print("You are currently BATTING.")
                    for a23 in range(1,37):
                        a24 = int(input("Score anywhere between 0-6 using Number Keys: "))
                        a25 = random.randint(0,6)
                        if a24>6:
                            print("You can't score more than 6 runs a ball.")
                            break
                        if a24 != a25:
                            score_you = score_you + a24
                        elif a24 == a25:
                            print("OUT!")
                            # Winner Declaration.
                            if score_sys > score_you:
                                print("System Wins!")
                                print("Thanks for playing.")
                            elif score_sys < score_you:
                                print("You Win!")
                                print("Thanks for playing.")
                            elif score_sys == score_you:
                                print("Game ended in a Tie!")
                                print("Thanks for playing.")
                            break
                        if score_sys > score_you:
                            print("System Wins!")
                        elif score_sys < score_you:
                            print("You Win!")
                        elif score_sys == score_you:
                            print("Game ended in a Tie!")
        elif a19 == 0:
            #System Chose to BALL first.
            #You are Batting.
            print("System decides to 'BALL' first.")
            print("You are currently BATTING. You have 'SIX OVERS' and '1 WICKET'.")
            for a26 in range(1,37):
                a27 = int(input("Score anywhere between 0-6 using Number Keys: "))
                a28 = random.randint(0,6)
                if a27>6:
                    print("You can't score more than 6 runs a ball.")
                    print("Thanks for playing.")
                    break
                if a27 != a28:
                    score_you = score_you + a27
                elif a27 == a28:
                    print("OUT!")
                    print("Your Score: ", score_you, "System needs", score_you+1, "runs from 'SIX OVERS' to win.")
                    #You are Balling.
                    print("You are currently BALLING.")
                    for a29 in range(1,37):
                        a30 = random.randint(0, 6)
                        a31 = int(input("Catch anywhere between 0-6 using Number Keys: "))
                        if a31>6:
                            print("You can't catch more than 6 in a ball.")
                            break
                        if a30 != a31:
                            score_sys = score_sys + a30
                        elif a30 == a31:
                            print("OUT!")
                            # Winner Declaration.
                            if score_sys > score_you:
                                print("System Wins!")
                                print("Thanks for playing.")
                            elif score_sys < score_you:
                                print("You Win!")
                                print("Thanks for playing.")
                            elif score_sys == score_you:
                                print("Game ended in a Tie!")
                                print("Thanks for playing.")
                            break
                        if score_sys > score_you:
                            print("System Wins!")
                        elif score_sys < score_you:
                            print("You Win!")
                        elif score_sys == score_you:
                            print("Game ended in a Tie!")
#Ends
#Thanks.
