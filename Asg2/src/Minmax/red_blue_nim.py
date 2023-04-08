from argparse import ArgumentParser, Namespace
from NimGame import NimGame

parser = ArgumentParser()

parser.add_argument('red', type=int, help="The Number of red marbles for Nim game")
parser.add_argument('blue', type=int, help="The Number of blue marbles for Nim game")
parser.add_argument('-p','--player',help = "Provide the first player to play",choices=["human","computer"], default="computer")
parser.add_argument('-d',"--depth", type=int, help="Depth to which the algorithm should run.")

args : Namespace = parser.parse_args()
if args.depth == None or args.depth == 0:
    args.depth = args.red + args.blue
if args.player == "computer":
    args.player = 2
else:
    args.player = 1
g = NimGame(args.red,args.blue,args.depth,args.player)
g.nimgame()