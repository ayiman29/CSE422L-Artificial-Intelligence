from queue import PriorityQueue

n, m = 15, 15
root = (1, 0)
goal = (13, 14)

grid = """\
###############
0000#########0#
###0#####00##0#
#00000000#0##0#
#0######0####0#
#0######0#0##0#
#0000000000000#
##########0####
#0######000####
#0######000000#
#0##########00#
#0000000000000#
###0#######0###
#00000000000000
###############
"""


grid = [list(row) for row in grid.splitlines()]




def f(curr, goal):
    return (abs(curr[0] - goal[0]) + abs(curr[1] - goal[1]))





def astar(grid, n, m, root, goal):
    g = {root: 0}
    parent = {root: None}
    q = PriorityQueue()
    # q.put() q.put((2, 'g')) ---> q.get() ---> q.qsize() ---> q.full()
    q.put((0 + f(root, goal), root))

    
    while q.qsize() > 0:
        _, curr = q.get()
        x, y = curr

        if curr == goal:
            return (g[goal], parent)

        if (x - 1) >= 0 and grid[x - 1][y] != "#":
            up = (x - 1, y)
            new_g = g[curr] + 1   

            if up not in g or new_g < g[up]:  
                g[up] = new_g
                q.put((new_g + f(up, goal), up))
                parent[up] = curr

        #DOWN
        if (x + 1) < n and grid[x + 1][y] != "#":
            down = (x + 1, y)
            new_g = g[curr] + 1   

            if down not in g or new_g < g[down]:  
                g[down] = new_g
                q.put((new_g + f(down, goal), down))
                parent[down] = curr

        #LEFT
        if (y - 1) >= 0 and grid[x][y-1] != "#":
            left = (x, y-1)
            new_g = g[curr] + 1   

            if left not in g or new_g < g[left]:  
                g[left] = new_g
                q.put((new_g + f(left, goal), left))
                parent[left] = curr

        #RIGHT
        if (y + 1) < m and grid[x][y + 1] != "#":
            right = (x, y + 1)
            new_g = g[curr] + 1   

            if right not in g or new_g < g[right]:  
                g[right] = new_g
                q.put((new_g + f(right, goal), right))
                parent[right] = curr


cost, parent = astar(grid, n, m, root, goal)

print(cost, parent)