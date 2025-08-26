# 1. Guess The Number Game
import random
money=100
game_played=0
game_won=0
game_lost=0
print("Welcome to the Guessing Game!")
print("You start with $100. Each game costs $5 to play.")

while money>=5:  # chơi khi người chơi còn ít nhất 5$
    print('Computer thinks a number from 1 to 100')
    computer_number= random.randint(1,100)

    level=int(input('choose level [1,2,3]?'))
    #1:easy, 2:medium, 3:hard
    time=10 if level ==1 else 6 if level ==2 else 3

    game_played = game_played + 1

    is_win= False
    for i in range(time):
        your_number= int(input("Enter your gessing number#" +str( i +1) + ": "))
        if your_number==computer_number:
            is_win=True
            break
        elif your_number< computer_number:
                print('too low!')
        else:
                print('too high!')
        print('-------------------')
    if not is_win:
        print('Game over!')
        game_lost += 1
        money = money - 5
    else:
        print("You win!")
        game_won += 1
        money = money + 5

    cont= input("Dare to you to play [y/n]")
    if cont== 'n' or cont=='N':
        break
print("-------GAME SUMMARY-------")
print("game played: ", game_played)
print("game won:", game_won)
print("game lost:", game_lost)
print("money left:", money,'$')

# 2.a game that simulate rolling a pair of dice.
print("Welcome to Tai-Xiu Game!")
print("Rule: Roll 2 sum dice > 5 => 'Tai' | Otherwise => 'Xiu'.")

money =int(input("Enter your starting money ($) :", ))
game_played= 0
game_won=0
game_lost=0

while money>0:
    bet = int(input("Enter your money to bet:"))
    if bet>money:
        print('You do not have enough money!')
        continue
    guess= input("Your gess [Tai/Xiu]:").strip().lower()

    die_1=random.randint(1, 6)
    die_2=random.randint(1, 6)
    Total= die_1 + die_2
    result= "tai" if Total >5 else "xiu"
    print(f"Dice rolled: {die_1} + {die_2} = {Total} => {result.upper()}")

    game_played +=1
    if guess == result:
        print("You win!")
        money= money+bet
        game_won +=1
    else:
        print("You lost!")
        money = money - bet
        game_lost +=1

    if money<=0:
        print("You are run out of money!")
        print("===GAME OVER===")
        break
    cont=input("Dare to you to play [y/n]")
    if cont == 'n' or cont == 'N':
        break
    print('----------------------------')

print("-------GAME SUMMARY-------")
print("game played: ", game_played)
print("game won:", game_won)
print("game lost:", game_lost)
print("money left:", money,'$')



