from ast import Return
from pyamaze import maze,agent,COLOR,textLabel

def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2) + abs(y1-y2)

def h1(x1,y1,x2,y2):
    return sum(abs(x1-x2) + abs(y1-y2))

def iterative_deepening_a_star(maze, start, goal, threshold):
    """
    Performs the iterative deepening A Star (A*) algorithm to find the shortest path from a start to a target node.
    """
    cols = maze.cols
    rows = maze.rows
    fwdPath={}
    
    allDistance = [[-1 for i in range(cols)] for j in range(rows)] 
    while True:
        
        if(fwdPath):
            return fwdPath
        else:
            
            fwdPath= iterative_deepening_a_star_rec(maze, start, goal, threshold, allDistance,fwdPath,start,explored=[])
            threshold=threshold+1
            #print("Repeating threshold :"+str(threshold))
        
        
def get_distance(maze,currCell,start, allDistance):
    minDistance=0
    distance=[]
    #set distance if beside start is 1 and the rest add on based on largest distance
    #currcell 1st is y 2nd is x
    for d in "ESNW":
        if maze.maze_map[currCell][d]==True:
            
            if d=="E":
                childCell=(currCell[0], currCell[1]+1)
                ox = currCell[1]+1
                oy = currCell[0]
                if(childCell == start):
                    distance.append(1)
                if(allDistance[oy-1][ox-1] != -1):
                    distance1=int((allDistance[oy-1][ox-1]))+1
                    distance.append(distance1)
            
            if d=="W":
                childCell=(currCell[0], currCell[1]-1)
                ox = currCell[1]-1
                oy = currCell[0]
                if(childCell == start):
                    distance.append(1)
                if(allDistance[oy-1][ox-1] != -1):
                    distance2=int(allDistance[oy-1][ox-1])+1
                    distance.append(distance2)
            if d=="S":
                childCell=(currCell[0]+1, currCell[1])
                ox = currCell[1]
                oy = currCell[0]+1
                if(childCell == start):
                    distance.append(1)
                if(allDistance[oy-1][ox-1] != -1):
                    distance3=int(allDistance[oy-1][ox-1])+1
                    distance.append(distance3)
            if d=="N":
                childCell=(currCell[0]-1, currCell[1])
                ox = currCell[1]
                oy = currCell[0]-1
                if(childCell == start):
                    distance.append(1)
                if(allDistance[oy-1][ox-1] != -1):
                    distance4=int(allDistance[oy-1][ox-1])+1
                    distance.append(distance4)
            
    
                
    
        
    minDistance=min(distance,default=-1)
    return minDistance
                

def iterative_deepening_a_star_rec(maze, start, goal, threshold, allDistance,fwdPath,currCell,explored=[]):
    """
    Performs DFS up to a depth where a threshold is reached (as opposed to interative-deepening DFS which stops at a fixed depth).
     """
    gx,gy = goal
    sx,sy = start
    cx,cy =currCell
    explored.append(currCell)
    notFound=True
    allDistance[sx-1][sy-1]=0
    #EWSN
    if(allDistance[cx-1][cy-1]< threshold):
        if maze.maze_map[currCell]["E"]==True:
            ox = currCell[0]
            oy = currCell[1]+1
            childCell=(currCell[0], currCell[1]+1)
            allDistance[ox-1][oy-1]= get_distance(maze,childCell,start,allDistance)
            if((allDistance[ox-1][oy-1]< int(threshold)) and (childCell not in explored)):
                explored.append(childCell)
                fwdPath=iterative_deepening_a_star_rec(maze,start,goal,threshold,allDistance,fwdPath,childCell,explored) 

        if maze.maze_map[currCell]["W"]==True:
            ox = currCell[0]
            oy =currCell[1]-1
            childCell=(currCell[0], currCell[1]-1)
            allDistance[ox-1][oy-1]= get_distance(maze,childCell,start,allDistance)
            if((allDistance[ox-1][oy-1]<int(threshold)) and (childCell not in explored)):
                explored.append(childCell)
                fwdPath=iterative_deepening_a_star_rec(maze,start,goal,threshold,allDistance,fwdPath,childCell,explored) 
        if maze.maze_map[currCell]["S"]==True:
            ox = currCell[0]+1
            oy =currCell[1]
            childCell=(currCell[0]+1, currCell[1])
            allDistance[ox-1][oy-1]= get_distance(maze,childCell,start,allDistance)
            if((allDistance[ox-1][oy-1]<int(threshold)) and (childCell not in explored)):
                explored.append(childCell)
                fwdPath=iterative_deepening_a_star_rec(maze,start,goal,threshold,allDistance,fwdPath,childCell,explored) 
        if maze.maze_map[currCell]["N"]==True:
            ox = currCell[0]-1
            oy =currCell[1]
            childCell=(currCell[0]-1, currCell[1])
            allDistance[ox-1][oy-1]= get_distance(maze,childCell,start,allDistance)
            if((allDistance[ox-1][oy-1]<int(threshold)) and (childCell not in explored)):
                explored.append(childCell)
                fwdPath=iterative_deepening_a_star_rec(maze,start,goal,threshold,allDistance,fwdPath,childCell,explored)
    if(currCell!=goal):
        return fwdPath
    

    

    
    
                         
    
    allDistance[sx-1][sy-1]=0
    endDistance = allDistance[gx-1][gy-1]
    #print("All distance :")
    """
    for row in allDistance:
        for col in row:
            print(col, end=" ") # print each element separated by space
        print()
    """
    currentPath = goal
    cols = maze.cols
    rows = maze.rows
    #print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in dfsPath.items()) + "}")
    if(currCell==goal and not bool(fwdPath)):
        
        while currentPath!=start and endDistance:
            endDistance= int(endDistance)-1
            ny = currentPath[0]
            nx = currentPath[1]
            """
            > for getting index 
                maze > list
                right,left,down,up
            E right: y,x+1 > x,y-1
            W left: y,x-1 > x-2,y-1
            S down: y+1,x > x-1,y
            N up: y-1,x > x-1,y-2

            accessing list change
            E right:  x+1,y > x+2,y-1
            W left:   x-1,y > 
            S down:   x,y-1 >
            N up:     x,y+1 >
            accessing [y][x]
            maze y,x

            current path :1 , 1
            maze: y 1, x 2
            list: x 0, y 1

            maze: y 1, x 0
            list: x 0, y -1

            maze: y 0, x 1
            list: x -1, y 0

            maze: y 2, x 1
            list: x 1, y 0
            27
            """
            #1,1 
            #E right 
            if(nx <cols and ny-1 <rows and nx >-1 and ny-1 >-1):
                if(int(allDistance[ny-1][nx])==endDistance):
                    pathcell=(ny,nx+1)
                    if(checkOpen(maze,pathcell,start,"E")):
                        fwdPath[pathcell]=currentPath
                        currentPath=pathcell
                        if(endDistance<0):
                            break
                        continue
            #W left
            if(nx-2 <cols and ny-1 <rows and nx-2 >-1 and ny-1 >-1):
                if(int(allDistance[ny-1][nx-2])==endDistance):
                    pathcell=(ny,nx-1)
                    if(checkOpen(maze,pathcell,start,"W")):
                        fwdPath[pathcell]=currentPath
                        currentPath=pathcell
                        if(endDistance<0):
                            break
                        continue
            #S down
            if(nx-1 <cols and ny <rows and nx-1 >-1 and ny >-1):
                if(int(allDistance[ny][nx-1])==endDistance):
                    pathcell=(ny+1,nx)
                    if(checkOpen(maze,pathcell,start,"S")):
                        fwdPath[pathcell]=currentPath
                        currentPath=pathcell
                        if(endDistance<0):
                            break
                        continue
            #N up
            if(nx-1 <cols and ny-2 <rows and nx-1 >-1 and ny-2 >-1):
                if(int(allDistance[ny-2][nx-1])==endDistance):
                    pathcell=(ny-1,nx)
                    if(checkOpen(maze,pathcell,start,"N")):
                        fwdPath[pathcell]=currentPath
                        currentPath=pathcell
                        if(endDistance<0):
                            break
                        continue
            if(endDistance<0):
                break
            
            
        
            
    if(endDistance==0):
        notFound=False
        return fwdPath
        print("before fwd status of notfound:" + str(notFound))
    """
    print("=============================================")
    print("FWDPATH")
    print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in fwdPath.items()) + "}")
    print("Final End distance: " + str(endDistance))
    """
    return fwdPath

def checkOpen(maze,pathCell,start,direction):
    condition = False
    # 1E,W,S,N
    ny = pathCell[0]
    nx = pathCell[1]
    if(direction=="W"):
        if(pathCell == start):
            condition = True
        if maze.maze_map[pathCell]["E"]==True:  
            condition = True
    elif(direction=="E"):
        if(pathCell == start):
            condition = True
        if maze.maze_map[pathCell]["W"]==True:
            condition = True
    elif(direction=="N"):
        if(pathCell == start):
            condition = True
        if maze.maze_map[pathCell]["S"]==True:
            condition = True
    elif(direction=="S"):
        if(pathCell == start):
            condition = True
        if maze.maze_map[pathCell]["N"]==True:
            condition = True
    
    return condition
    
