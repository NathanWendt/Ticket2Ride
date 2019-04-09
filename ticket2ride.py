#### TICKET 2 RIDE ####
#### Code by Nathan Wendt ####
from enum import Enum
import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Color(Enum):
    BLUE = 0
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLACK = 4
    PINK = 5
    WHITE = 6
    ORANGE = 7
    GOLD = 8
    GRAY = 9

class City(Enum):
    VANCOUVER = 0
    SEATTLE = 1
    PORTLAND = 2
    SAN_FRANCISCO = 3
    LOS_ANGELAS = 4
    CALGARY = 5
    HELENA = 6
    SALT_LAKE_CITY = 7
    LAS_VEGAS = 8
    PHOENIX = 9
    WINNIPEG = 10
    DENVER = 11
    SANTA_FE = 12
    EL_PASO = 13
    DULUTH = 14
    OMAHA = 15
    KANSAS_CITY = 16
    OKLAHOMA_CITY = 17
    DALLAS = 18
    HOUSTON = 19
    SAULT_ST_MARIE = 20
    CHICAGO = 21
    SAINT_LOUIS = 22
    LITTLE_ROCK = 23
    NEW_ORLEANS = 24
    MONTREAL = 25
    TORONTO = 26
    PITTSBURGH = 27
    NASHVILLE = 28
    ATLANTA = 29
    BOSTON = 30
    NEW_YORK = 31
    WASHINGTON = 32
    RALEIGH = 33
    CHARLESTON = 34
    MIAMI = 35

#print(City(2))
destinations = {}
destinations[(City(2),City(9))] = 11 # Portland - Phoenix
destinations[(City(25),City(24))] = 13 # Montreal - New Orleans
destinations[(City(25),City(29))] = 9 # Montreal - Atlanta
destinations[(City(4),City(35))] = 20 # Los Angelas - Miami
destinations[(City(1),City(31))] = 22 # Seattle - New York
destinations[(City(5),City(7))] = 7 # Calgary - Salt Lake City
destinations[(City(4),City(21))] = 16 # Los Angelas - Chicago
destinations[(City(6),City(4))] = 8 # Helena - Los Angelas
destinations[(City(11),City(27))] = 11 # Denver - Pittsburgh
destinations[(City(16),City(19))] = 5 # Kansas City - Houston
destinations[(City(10),City(23))] = 11 # Winnipeg - Little Rock
destinations[(City(5),City(9))] = 13 # Calgary - Phoenix
destinations[(City(0),City(25))] = 20 # Vancouver - Montreal
destinations[(City(21),City(12))] = 9 # Chicago - Santa Fe
destinations[(City(30),City(35))] = 12 # Boston - Miami
destinations[(City(26),City(35))] = 10 # Toronto - Miami
destinations[(City(18),City(31))] = 11 # Dallas - New York
destinations[(City(20),City(17))] = 9 # Sault St. Marie - Oklahoma City
destinations[(City(1),City(4))] = 9 # Seattle - Los Angelas
destinations[(City(3),City(29))] = 17 # San Francisco - Atlanta
destinations[(City(2),City(28))] = 12 # Portland - Nashville
destinations[(City(14),City(19))] = 8 # Duluth - Houston
destinations[(City(0),City(12))] = 13 # Vancouver - Santa Fe
destinations[(City(4),City(31))] = 21 # Los Angelas - New York
destinations[(City(21),City(24))] = 7 # Chicago - New Orleans
destinations[(City(14),City(13))] = 10 # Duluth - El Paso
destinations[(City(10),City(19))] = 12 # Winnipeg - Houston
destinations[(City(20),City(28))] = 8 # Sault St. Marie - Nashville
destinations[(City(31),City(29))] = 6 # New York - Atlanta
destinations[(City(11),City(13))] = 4 # Denver - El Paso

class Card:
    def __init__(self, color):
        self.color = color

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(len(Color)-2): # excludes gold and gray: gold has more cards, gray is not a resource type
            self.cards = self.cards + [Card(Color(i)) for j in range(2)]
        self.cards = self.cards + [Card(Color(8)) for j in range(3)] # heres gold :)

    def Shuffle(self):
        random.shuffle(self.cards)

class Ticket:
    def __init__(self,ticket):
        self.start = ticket[0]
        self.end = ticket[1]
        self.points = destinations[ticket]

class TicketDeck:
    def __init__(self):
        self.tickets = [Ticket(tix) for tix in destinations]

class Edge:
    def __init__(self, info):
        self.taken = False
        self.start, self.stop, self.length, self.color = info

class EdgeList:  # List of Edges on Board
    def __init__(self, info_list):
        self.edges = [Edge(info) for info in info_list.info]

class InfoList:   # Configuration info for edge list
    def __init__(self, file_name):
        handle = open(file_name,"r")
        lines = handle.readlines()
        splitlines = [line.split() for line in lines]
        self.info = [[City[sl[0]], City[sl[1]], sl[2], Color[sl[3]]] for sl in splitlines] # Edge info: start city, stop city, length, color

class Board:
    def __init__(self, edge_list):
        self.G = nx.MultiGraph()
        [self.G.add_edge(edge.start, edge.stop, taken = edge.taken,
                         length = edge.length, color = edge.color) for edge in edge_list.edges]

if __name__ == '__main__':
    infolist = InfoList('edges.txt')
    #[print(info) for info in infolist.info]

    edgelist = EdgeList(infolist)
    #[print(this.start, this.stop, this.length, this.color) for this in edgelist.edges]
    board = Board(edgelist)
    nx.draw_networkx(board.G)
    plt.show()
