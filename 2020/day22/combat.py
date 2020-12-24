#!/bin/python3
import sys
import time
import queue
import re

class Player():
    def __init__(self, number):
        self.num  = number
        self.deck = queue.Queue()

    def getCard(self):
        return self.deck.get()
    
    def putCard(self, card):
        self.deck.put(card)

    def deckSize(self):
        return self.deck.qsize()

    def empty(self):
        return self.deck.empty()

    def copy(self, count):
        new = Player(self.num)
        
        for _ in range(count):
            card = self.getCard()
            new.putCard(card)
            self.putCard(card)

        for _ in range(self.deckSize() - count):
            self.putCard(self.getCard())
        return new

    def tup(self):
        qlist = list()
        for _ in range(self.deckSize()):
            card = self.getCard()
            qlist.append(card)
            self.putCard(card)
        return tuple(qlist)

players = dict()

def parse(filename):
    with open(filename, "r") as fd:
        data = fd.read().splitlines()

    for line in data:
        if re.match(r'Player [\d]+:', line):
            pnum = re.findall(r'[\d]+', line)[0]
            player = Player(int(pnum))
        elif line:
            player.deck.put(int(line))
        else:
            players[player.num] = player

    return data

def calculateScore(winner):
    multiplier = winner.deckSize()
    score = 0
    while not winner.empty():
        score += winner.getCard() * multiplier
        multiplier -= 1
    return score

def partOne():
    human = players[1].copy(players[1].deckSize())
    crab  = players[2].copy(players[2].deckSize())

    while not human.empty() and not crab.empty():
        hCard = human.getCard()
        cCard = crab.getCard()

        if hCard > cCard:
            # human wins round
            human.putCard(hCard)
            human.putCard(cCard)
        else:
            # crab wins round
            crab.putCard(cCard)
            crab.putCard(hCard)

    # determine who won the game
    if human.empty():
        winner = crab
    else:
        winner = human

    return calculateScore(winner)

memoization = dict()
Game = 0
# returns a winner
def play(human, crab, game):
    print("=== Game {0} ===".format(game))
    global Game
    gameConfigs = set()
    initialConfig = (human.tup(), crab.tup())

    if initialConfig in memoization:
        return memoization[initialConfig]        

    # run all rounds of this game
    _round = 1
    while not human.empty() and not crab.empty():
        config = (human.tup(), crab.tup())
        if config in gameConfigs:
            return human
       
        # log this config
        gameConfigs.add(config)

        # draw this round's cards
        hCard = human.getCard()
        cCard = crab.getCard()

        # see if this config has been seen ever before
        if config in memoization:
            memoization[initialConfig] = memoization[config].copy()
            return memoization[config]
            winner = memoization[config]
            if winner.num == human.num:
                human.putCard(hCard)
                human.putCard(cCard)
            else:
                crab.putCard(cCard)
                crab.putCard(hCard)

        else:
            if hCard <= human.deckSize() and cCard <= crab.deckSize():
                # play sub-game to determine this round's winner
                tHuman = human.copy(hCard)
                tCrab  = crab.copy(cCard)
                Game  += 1
                winner = play(tHuman, tCrab, game=Game)

                if winner.num == human.num:
                    human.putCard(hCard)
                    human.putCard(cCard)
                else:
                    crab.putCard(cCard)
                    crab.putCard(hCard)
            else:
                if hCard > cCard:
                    human.putCard(hCard)
                    human.putCard(cCard)
                else:
                    crab.putCard(cCard)
                    crab.putCard(hCard)
        _round += 1

    if human.empty():
        winner = crab
    else:
        winner = human

    memoization[initialConfig] = winner
    return winner

def partTwo():
    global Game
    human = players[1].copy(players[1].deckSize())
    crab  = players[2].copy(players[2].deckSize())

    Game += 1
    winner = play(human, crab, game=Game)
    
    return calculateScore(winner)


if __name__ == '__main__':
    # parse data
    data = parse(sys.argv[1])

    # part 1
    start = time.perf_counter()
    solution1 = partOne()

    # part 2
    solution2 = partTwo()
    end = time.perf_counter()
    # results
    print("Part 1:\n{0}".format(solution1))
    print("Part 2:\n{0}".format(solution2))
    print("Time: {0} ms".format(round((end-start) * 1000,4)))
