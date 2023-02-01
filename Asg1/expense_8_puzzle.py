import time
import sys
from bfs import bfs

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    method = sys.argv[3]
    try:
        dump_flag = sys.argv[4]
        if dump_flag == "true" or dump_flag == "True":
            dump_flag = True
        else:
            dump_flag = False
    except:
        dump_flag = False
    with open (input_file , "r") as file:
        data = file.readlines()
    data = data[0:3]
    with open (output_file , "r") as file:
        goal = file.readlines()
    goal = goal [0:3]
    input = []
    output = []
    for i in range(0,3):
        input.append(data[i].replace("\n","").split(" "))
        output.append(goal[i].replace("\n","").split(" "))
    
    for i in range(0,3):
        for j in range(0,3):
            input[i][j] = int(input[i][j])
            output[i][j] = int(output[i][j])
    
    timestr = time.strftime("%Y%m%d-%H%M%S")
    if dump_flag:
        data_dump = f"Command-Line Arguments : {sys.argv[1:]} \nMethod Selected: {method} \nRunning {method}\n\n"
        with open (f"trace-{timestr}.txt",'a+') as text_file:
            text_file.write(data_dump)
            text_file.close()
    state = bfs(input, output,f"trace-{timestr}.txt", dump_flag = dump_flag)
    state.graphSearch()
