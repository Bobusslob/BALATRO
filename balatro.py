import random
import math
import sys
import time
import sqlite3
import pygame
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
        for suit in self.suite:
            for value in range(2, 14):
                if value > 10:
                    if value - cardLoopVar > len(self.greater_than_ten) - 1:
                        cardLoopVar+=len(self.greater_than_ten)
                    self.cards.append(Card(10, f'{self.greater_than_ten[value - cardLoopVar]} of {suit}', suit))
                else:
                    self.cards.append(Card(value, f'{value} of {suit}', suit))
class Card:
    def __init__(self, value, name, suit):
        self.value = value
        self.suit = suit
        self.name = name
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
    pygame.init()
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