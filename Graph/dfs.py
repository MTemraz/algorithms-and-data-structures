# Write code to implement Depth First Search given a Graph

def dfs(graph):
    time = 0
    for v in graph:
        if v.color == 'white':
            dfs_visit(v)
            
def dfs_visit(vertex):
    time += 1
    vertex.setStartTime(time)
    vertex.setColor('gray')
    for nbr in vertex.getConnections():
        if nbr.color == 'white':
            nbr.setParent(vertex)
            dfs_visit(nbr)
    time += 1
    vertex.setEndTime(time)
    vertex.setColor('black')
