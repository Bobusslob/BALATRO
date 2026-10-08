import random
import math
import time
import sqlite3
import pygame
class Deck:
    def __init__(self):
        self.cards = []
        self.suite = ['hearts', 'diamonds', 'clubs', 'spades']
        self.greater_than_ten = ['Jack', 'Queen', 'King']
        for suit in self.suite:
            for value in range(1, 14):
                if value > 10:
                    self.suite.append(Card(value, self.greater_than_ten[value - 11], suit))

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
    play = True
    while play:
        userInp = input("Do you want to play? (y/n): ")
        if userInp.lower() == "n":
            play = False
        else:


if __name__ == "__main__":
    game()