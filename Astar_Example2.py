from queue import PriorityQueue

grid = [
[0,0,0,0],
[0,1,1,0],
[0,0,0,0],
[0,1,0,0]
]

start = (0,0)
goal = (3,3)

def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar_grid(start,goal):
    pq = PriorityQueue()
    pq.put((0,start))
    visited=set()

    while not pq.empty():
        cost,current = pq.get()

        if current == goal:
            return "Goal Reached"

        visited.add(current)

        x,y=current
        moves=[(1,0),(-1,0),(0,1),(0,-1)]

        for dx,dy in moves:
            nx,ny=x+dx,y+dy
            if 0<=nx<4 and 0<=ny<4 and grid[nx][ny]==0:
                if (nx,ny) not in visited:
                    pq.put((heuristic((nx,ny),goal),(nx,ny)))

print(astar_grid(start,goal))
