import random
import math
import sys
import time
import sqlite3
import pygame
pygame.init()
cards = []
card1 = pygame.image.load('Cards/card1.png')
card2 = pygame.image.load('Cards/card2.png')
card3 = pygame.image.load('Cards/card3.png')
card4 = pygame.image.load('Cards/card4.png')
card5 = pygame.image.load('Cards/card5.png')
card6 = pygame.image.load('Cards/card6.png')
card7 = pygame.image.load('Cards/card7.png')
card8 = pygame.image.load('Cards/card8.png')
card9 = pygame.image.load('Cards/card9.png')
card10 = pygame.image.load('Cards/card10.png')
card11 = pygame.image.load('Cards/card11.png')
card12 = pygame.image.load('Cards/card12.png')
card13 = pygame.image.load('Cards/card13.png')
card14 = pygame.image.load('Cards/card14.png')
card15 = pygame.image.load('Cards/card15.png')
card16 = pygame.image.load('Cards/card16.png')
card17 = pygame.image.load('Cards/card17.png')
card18 = pygame.image.load('Cards/card18.png')
card19 = pygame.image.load('Cards/card19.png')
card20 = pygame.image.load('Cards/card20.png')
card21 = pygame.image.load('Cards/card21.png')
card22 = pygame.image.load('Cards/card22.png')
card23 = pygame.image.load('Cards/card23.png')
card24 = pygame.image.load('Cards/card24.png')
card25 = pygame.image.load('Cards/card25.png')
card26 = pygame.image.load('Cards/card26.png')
card27 = pygame.image.load('Cards/card27.png')
card28 = pygame.image.load('Cards/card28.png')
card29 = pygame.image.load('Cards/card29.png')
card30 = pygame.image.load('Cards/card30.png')
card31 = pygame.image.load('Cards/card31.png')
card32 = pygame.image.load('Cards/card32.png')
card33 = pygame.image.load('Cards/card33.png')
card34 = pygame.image.load('Cards/card34.png')
card35 = pygame.image.load('Cards/card35.png')
card36 = pygame.image.load('Cards/card36.png')
card37 = pygame.image.load('Cards/card37.png')
card38 = pygame.image.load('Cards/card38.png')
card39 = pygame.image.load('Cards/card39.png')
card40 = pygame.image.load('Cards/card40.png')
card41 = pygame.image.load('Cards/card41.png')
card42 = pygame.image.load('Cards/card42.png')
card43 = pygame.image.load('Cards/card43.png')
card44 = pygame.image.load('Cards/card44.png')
card45 = pygame.image.load('Cards/card45.png')
card46 = pygame.image.load('Cards/card46.png')
card47 = pygame.image.load('Cards/card47.png')
card48 = pygame.image.load('Cards/card48.png')
card49 = pygame.image.load('Cards/card49.png')
card50 = pygame.image.load('Cards/card50.png')
card51 = pygame.image.load('Cards/card51.png')
card52 = pygame.image.load('Cards/card52.png')
cardImgList = [
    card1, card2, card3, card4, card5, card6, card7, card8, card9, card10,
    card11, card12, card13, card14, card15, card16, card17, card18, card19, card20,
    card21, card22, card23, card24, card25, card26, card27, card28, card29, card30,
    card31, card32, card33, card34, card35, card36, card37, card38, card39,	card40,
   	card41,	card42,	card43,	card44,	card45,	card46,	card47,	card48, card49,	card50,	
    card51, card52
]
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
                    self.cards.append(Card(10, f'{self.greater_than_ten[value - cardLoopVar]} of {suit}', suit, cardImgList[cardAssigner - 1]))
                else:
                    self.cards.append(Card(value, f'{value} of {suit}', suit, cardImgList[cardAssigner - 1]))
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
    
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
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
            screen.fill((0, 0, 0))
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            for card in hand:
                if card.cardPath.get_rect(topleft=(100 + hand.index(card) * 100, 100)).collidepoint(pygame.mouse.get_pos()):
                    screen.blit(card.cardPath, (100 + hand.index(card) * 100, 90))
                else:
                    screen.blit(card.cardPath, (100 + hand.index(card) * 100, 100))
        pygame.display.update()
        clock.tick(FPS)

    
if __name__ == "__main__":
    game()
    pygame.quit()
    sys.exit()