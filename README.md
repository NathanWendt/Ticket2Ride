# Ticket2Ride
Beginnings of a python implementation of Ticker to Ride. Eventually will be used to train a deep-learning AI. 

I used this project as an opportunity to transition away from the line-by-line scripting style of coding that Matlab built into me into a more OOP style. ticket_to_ride_map.jpg was taken from the following reddit post complaining about Maine being under-represented: https://www.reddit.com/r/Maine/comments/40gxxb/anyone_else_annoyed_by_the_ticket_to_ride_map/

ticket2ride.py has class definitions for the resource cards, deck, destination cards, destination deck, all game edges, and the board via a networkx multigraph. 

edges.txt is a text file with each line representing an edge on the game board. The format is as follows:
[start node] [stop node] [length] [color]
