import random
import math
import sys
import time
import sqlite3
import pygame
pygame.init()
cards = []
card1 = pygame.image.load('Cards/card1')
card2 = pygame.image.load('Cards/card2')
card3 = pygame.image.load('Cards/card3')
card4 = pygame.image.load('Cards/card4')
card5 = pygame.image.load('Cards/card5')
card6 = pygame.image.load('Cards/card6')
card7 = pygame.image.load('Cards/card7')
card8 = pygame.image.load('Cards/card8')
card9 = pygame.image.load('Cards/card9')
card10 = pygame.image.load('Cards/card10')
card11 = pygame.image.load('Cards/card11')
card12 = pygame.image.load('Cards/card12')
card13 = pygame.image.load('Cards/card13')
card14 = pygame.image.load('Cards/card14')
card15 = pygame.image.load('Cards/card15')
card16 = pygame.image.load('Cards/card16')
card17 = pygame.image.load('Cards/card17')
card18 = pygame.image.load('Cards/card18')
card19 = pygame.image.load('Cards/card19')
card20 = pygame.image.load('Cards/card20')
card21 = pygame.image.load('Cards/card21')
card22 = pygame.image.load('Cards/card22')
card23 = pygame.image.load('Cards/card23')
card24 = pygame.image.load('Cards/card24')
card25 = pygame.image.load('Cards/card25')
card26 = pygame.image.load('Cards/card26')
card27 = pygame.image.load('Cards/card27')
card28 = pygame.image.load('Cards/card28')
card29 = pygame.image.load('Cards/card29')
card30 = pygame.image.load('Cards/card30')
card31 = pygame.image.load('Cards/card31')
card32 = pygame.image.load('Cards/card32')
card33 = pygame.image.load('Cards/card33')
card34 = pygame.image.load('Cards/card34')
card35 = pygame.image.load('Cards/card35')
card36 = pygame.image.load('Cards/card36')
card37 = pygame.image.load('Cards/card37')
card38 = pygame.image.load('Cards/card38')
card39 = pygame.image.load('Cards/card39')
card40 = pygame.image.load('Cards/card40')
card41 = pygame.image.load('Cards/card41')
card42 = pygame.image.load('Cards/card42')
card43 = pygame.image.load('Cards/card43')
card44 = pygame.image.load('Cards/card44')
card45 = pygame.image.load('Cards/card45')
card46 = pygame.image.load('Cards/card46')
card47 = pygame.image.load('Cards/card47')
card48 = pygame.image.load('Cards/card48')
card49 = pygame.image.load('Cards/card49')
card50 = pygame.image.load('Cards/card50')
card51 = pygame.image.load('Cards/card51')
card52 = pygame.image.load('Cards/card52')

class Deck:
    def __init__(self):
        self.cards = []
        self.suite = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.greater_than_ten = ['Jack', 'Queen', 'King']
        self.reShuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    
    def reShuffle(self):
        cardLoopVar = 11
        cardAssigner = 0
        for suit in self.suite:
            for value in range(2, 14):
                cardAssigner+=1
                if value > 10:
                    if value - cardLoopVar > len(self.greater_than_ten) - 1:
                        cardLoopVar+=len(self.greater_than_ten)
                    self.cards.append(Card(10, f'{self.greater_than_ten[value - cardLoopVar]} of {suit}', suit))
                else:
                    self.cards.append(Card(value, f'{value} of {suit}', suit, f'Cards/card{cardAssigner}'))
class Card:
    def __init__(self, value, name, suit, cardPath):
        self.value = value
        self.suit = suit
        self.name = name
        self.cardPath = cardPath
    def change_suit(self, new_suit):
        self.suit = new_suit
    def pullCard(self):
        return self.value, self.suit

def dbConnection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection 

def initDb():
    with dbConnection() as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, score INTEGER NOT NULL)')

def game():
    
    SCREEN_WIDTH = 2160
    SCREEN_HEIGHT = 1080
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

    screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Balatro")
    clock = pygame.time.Clock()
    FPS = 60
    running = True
    pokerHands = {
        "High Card":{"Worth":5, "Mult":1}, 
        "Pair":{"Worth":10, "Mult":2}, 
        "Two Pair":{"Worth":20, "Mult":2}, 
        "Three Of A Kind":{"Worth":30, "Mult":3}, 
        "Straight":{"Worth":30, "Mult":4}, 
        "Flush":{"Worth":35, "Mult":4}, 
        "Full House":{"Worth":40, "Mult":4},
        "Four Of A Kind":{"Worth":60, "Mult":7},
        "Straight Flush":{"Worth":100, "Mult":8},
        "Royal Flush":{"Worth":100, "Mult":8},
        "Five Of A Kind":{"Worth":120, "Mult":12},
        "Flush House":{"Worth":140, "Mult":14},
        "Flush Five":{"Worth":160, "Mult":16},
    }
    deck = Deck()
    hand = []
    deck.shuffle()
    for i in range(0,8):
        card = deck.cards[i]
        hand.append(card)
        deck.cards.remove(card)
        print(card.name)
    print()
    for card in deck.cards:
        print(card.name)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.fill((0,0,0))
        pygame.display.update()
        clock.tick(FPS)
    
if __name__ == "__main__":
    game()
    pygame.quit()
    sys.exit()