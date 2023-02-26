Name: Abhishek Girish Patel
UTA ID: 1002033618
Programming language: Python 3.10.6

Code Structure: 
    expense_8_puzzle.py 
        Main driver file it will take the command line inputs, process them and convert them 
        into the required form for the program. 
        If dump_flag is set it will create the log file with the required name. 
        Contains an if-else ladder to select approprite method given as command line arugment.
        This will call the approprite function in the otherfiles to perform diffent serch technique.
        It will also keep a track of the runtime of the program.

    tools.py
        Contains required additional function and tools need for the program.
        eg. heurstic calculation, successor generator etc...

    datastructure.py
        Contains implementation of diffent datastructure needed.
        Stack,Queue and Priority queue are implemented here.
    
    bfs.py
        BFS implementation for Graph Search
    
    dfs.py
        DFS implementation for Graph Search
    
    ucs.py
        UCS implementation for Graph Search

    dls.py
        DLS implementation for Tree Search
    
    ids.py
        IDS implementation for Tree Search
    
    greedy.py
        Greedy implementation for Graph Search
    
    astar.py
        A* implementation for Graph Search

How to Run the Code:

    Best case running envionment for this code:
    OS: Ubuntu 22.04.1 LTS 
    Programming language: Python 3.10.6
    Processor: Intel core Series(9th Gen +) and AMD equivalent
    Ram: 16GB minimum, more the better.
    Storage: 100 GB minimum, more the better. (log files be very large.)

    Use of python3 is required. specifically Python 3.10.6 
    
    if python is not installed please install python using terminal in ubunut/mac/other linux or using chocolaty/downloading .exe file in windows computer
    installation guide for linux/ubunut: https://docs.python-guide.org/starting/install3/linux/
    installation guide for mac: https://docs.python-guide.org/starting/install3/osx/
    installation guide for windows: https://docs.python-guide.org/starting/install3/win/

    Intructions for Ubuntu/mac/other linux OS:
        python3 expense_8_puzzle.py "initial state in txt file" "goal state in txt file" "method of implementation" "dump_flag(true/True or false/False)"
        example: using the initial state and goal state file in the folder you can run the program for a* methedology with log file creation as,
                python3 expense_8_puzzle.py StartFile.txt GoalFile.txt a* True 

        Note: 
        * The envionment variable to run Python 3.10.6 program is set as python3 by default IF you have changed it please use the envionment variable
        defined by you.  
        * python is the default envionment variable to run Python 2 program if used the code will not run and throw errors.(unless you have changed
        your python envionment variable to run Python 3.10.6)
    
    Intructions for windows:
        python expense_8_puzzle.py "initial state in txt file" "goal state in txt file" "method of implementation" "dump_flag(true/True or false/False)"
        example: using the initial state and goal state file in the folder you can run the program for a* methedology with log file creation as,
                python expense_8_puzzle.py StartFile.txt GoalFile.txt a* True
        
        Note:
        * If you have multiple python versions installed on your computer please uninstall other versions and just keep Python 3.10.6. if not errors
        might be encounted due to different versions. 
        * if you have diffent versions of python installed please be carefull while running the code and make sure Python 3.10.6 is only used to run.
        * The envionment variable to run Python 3.10.6 program is set as python by default IF you have changed it please use the envionment variable
        defined by you.
    
    Extra: 
    For depth limited search/DLS/dls: If this method is selectd please provied the depth limit as imput when prompted on command line.
    


    
            Approximate run time of each algorithm 
    *------------------------------------------------------------------------------*
    | methedology | time required with dump file | time required without dump file | 
    *------------------------------------------------------------------------------*
    |     bfs     |         7.745712 sec         |          0.136029 sec           |
    *------------------------------------------------------------------------------*
    |     dfs     |         3.110014 sec         |          0.236178 sec           |
    *------------------------------------------------------------------------------*
    |     ucs     |        56.498704 sec         |          3.381236 sec           |
    *------------------------------------------------------------------------------*
    |     dls     |        16.604037 sec         |          6.316990 sec           | **for depth limt 13**
    *------------------------------------------------------------------------------*
    |     ids     |        17.096615 sec         |          4.050294 sec           |
    *------------------------------------------------------------------------------*
    |    greedy   |         0.002006 sec         |          0.000579 sec           |
    *------------------------------------------------------------------------------*
    |     a*      |         0.014061 sec         |          0.002388 sec           |
    *------------------------------------------------------------------------------*