import time
import sys
from bfs import bfs
from dfs import dfs
from ucs import ucs
from dls import dls
from ids import ids
from astar import astar
from greedy import greedy

if __name__ == "__main__":
    begin = time.time()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    method = sys.argv[3]
    if method == "astar.py":
        method = "a*"
    dump_flag = sys.argv[4]
    if dump_flag == "true" or dump_flag == "True":
        dump_flag = True
    else:
        dump_flag = False
    with open (input_file , "r") as file:
        data = file.readlines()
    data = data[0:3]
    with open (output_file , "r") as file:
        goal = file.readlines()
    goal = goal [0:3]
    start = []
    output = []
    for i in range(0,3):
        start.append(data[i].replace("\n","").split(" "))
        output.append(goal[i].replace("\n","").split(" "))
    
    for i in range(0,3):
        for j in range(0,3):
            start[i][j] = int(start[i][j])
            output[i][j] = int(output[i][j])
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    if dump_flag:
        data_dump = f"Command-Line Arguments : {sys.argv[1:]} \nMethod Selected: {method} \nRunning {method}\n\n"
        with open (f"trace-{timestr}.txt",'a+') as text_file:
            text_file.write(data_dump)
            text_file.close()

    if method == "bfs" or method == "BFSs":
        state = bfs(start, output,f"trace-{timestr}.txt",dump_flag = dump_flag)
        result = state.graphSearch()
    elif method == "dfs" or method == "DFS":
        state = dfs(start, output,f"trace-{timestr}.txt",dump_flag = dump_flag)
        result = state.graphSearch()
    elif method == "ucs" or method == "UCS":
        state = ucs(start, output,f"trace-{timestr}.txt",dump_flag = dump_flag)
        result = state.graphSearch()
    if method == "dls" or method == "DLS":
        depth_limit = input("Enter depth limit: ")
        state = dls(start, output,f"trace-{timestr}.txt", int(depth_limit),dump_flag = dump_flag)
        result = state.graphSearch()
    elif method == "ids" or method == "IDS":
        state = ids(start, output,f"trace-{timestr}.txt",dump_flag = dump_flag)
        result = state.ids()
    elif method == "greedy" or method == "GREEDY":
        state = greedy(start, output,f"trace-{timestr}.txt",dump_flag = dump_flag)
        result = state.graphSearch()
    elif method == "a*" or method == "A*":
        state = astar(start, output,f"trace-{timestr}.txt",dump_flag = dump_flag)
        result = state.graphSearch()

    print(time.time()-begin)
