#!/usr/bin/env python3

# this is my resubmission of the python rock paper Scissors
# projects
# I have mainly sourced this project from cross checking with
# notes i took through the python course, general youtube
# tutorials to breakdown/bridge the gaps that I was not
# so confident in. And then with friends who are software
# devs and have extensive knowledge in python.

# Note - I got a plagarism warning for my first submission.
# This is NOT a copy / paste job. I did my best to grind
# through the tough parts to put this together.

import random
import time

# I have added time in order to slow down
# the flow of the game so it can be read easily

moves = ['rock', 'paper', 'scissors']

# I learned that case sensitivity means everything
# with the moves list. I had capital R, P and S in
# the list. This caused a lot of issues in the HumanPlayer
# class. I eventually figured it out and reverted back to
# current state.

# I set up the player class to hold some global values and variables
# Before setting up the human and computer move variables I was havving issues
# with Reflect and Cycle players - object has no attribute
# 'humanmove' / 'computermove'


class Player:
    wins = 0
    humanmove = ""
    computermove = ""

    def move(self):
        return 'rock'

    def learn(self, humanmove, computermove):
        self.humanmove = humanmove
        self.computermove = computermove


# the .lower() was brought in to ensure that Upper case input was accepted


class HumanPlayer(Player):
    def move(self):
        humaninput = input("Rock, Paper, Scissors?!: ").lower()

        if humaninput.lower() in moves:
            return humaninput.lower()
        else:
            time.sleep(1)
            print("Wrong! Try getting it right!")
            time.sleep(1)
            return self.move()


# a simple random method linked to the moves list took care of the random
# player.


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# if statement was used to mimmic human moves. But the first turn there
# is no human move to copy so a random move will do fine.


class ReflectPlayer(Player):
    def move(self):
        if self.humanmove in moves:
            return self.computermove
        else:
            return random.choice(moves)


# Cycle player uses an extended if statement in order to have specific
# responses to the human players moves. Again, first move requires a random
# move before human input can be read.


class CyclePlayer(Player):
    def move(self):
        if self.humanmove == "rock":
            return "scissors"
        elif self.humanmove == "paper":
            return "rock"
        elif self.humanmove == "scissors":
            return "paper"
        else:
            return random.choice(moves)


# Basic rules of the game.


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Defining how the game plays. Defining p1, p2, move1 and move2
# sets us up to be able to display moves, scores and keep track
# of those inputs. Again, sleep timers are used to pace the game.


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        time.sleep(1)
        print(f"Player 1: {move1} Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        # Individual game conditions.
        # I used color to reflect a win, lose or draw.
        # Again, sleep timer to run things a little slower so it can be read
        # if statement to then determine the game outcome.

        if beats(move1, move2):
            self.p1.wins += 1
            time.sleep(1)
            print(f"You won this round! {self.p1.wins}"f" - {self.p2.wins}")
            time.sleep(1)
        elif beats(move2, move1):
            self.p2.wins += 1
            time.sleep(1)
            print(f"You lost this round! ", f"{self.p1.wins}"f" - ",
                  f"{self.p2.wins}")
            time.sleep(1)
        else:
            time.sleep(1)
            print(f"Stalemate this time! {self.p1.wins} - ",
                  f"{self.p2.wins} Run it back!")
            time.sleep(1)


# A for loop is used to run the 5 games.
# The round counter originally started at 0 so adding +1
# displays the right round count.

    def play_game(self):
        print(f" ")
        print("Game start!")
        time.sleep(1)
        for round in range(5):
            time.sleep(1)
            print(f"Round {round +1}:")
            self.play_round()
        print("Game over!")
        time.sleep(2)
        print("FINAL SCORE!")
        print(f"{self.p1.wins}" f" - "f"{self.p2.wins}")
        time.sleep(1)


# Endings

# if statement used to determine the end game message based
# on your final score. Pulls your win count, compares against
# the computer and then makes a decision by running through
# the if statement.
# I also wanted this to be a bit more involved with text, color,
# and sleep. Changing color depending on outcome, slow so it can
# be read, and changed up the message to be a bit more fun.

        if self.p1.wins > self.p2.wins:
            time.sleep(1)
            print("YOU WIN!")
            time.sleep(2)
            print(f"{self.p1.wins}" f" - "f"{self.p2.wins}")
            time.sleep(2)
            print("LET'S GOOOOOOO!")
            time.sleep(2)

        elif self.p1.wins < self.p2.wins:
            time.sleep(1)
            print("YOU LOST TO A COMPUTER!")
            time.sleep(2)
            print(f"{self.p1.wins} - {self.p2.wins}")
            time.sleep(2)
            print("Don't beat yourself up, computers are",
                  "quite smart these days :')")
            time.sleep(2)
        else:
            time.sleep(1)
            print(f"A tie. You both won {self.p1.wins} games each.",
                   "I guess that is OK...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("...I guess.")
            time.sleep(2)


if __name__ == '__main__':
    play_again = "Y"
    while play_again.upper() == 'Y':
        game = Game(HumanPlayer(), random.choice([RandomPlayer(),
                    ReflectPlayer(), CyclePlayer()]))
        game.play_game()
        play_again = input("Do you want to play again? Y/N? ")
