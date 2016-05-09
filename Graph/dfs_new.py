def dfs(G):
    for v in G:
        v.setColor('white')
    time = 0
    for v in G:
        if v.color == 'white':
            _dfs_visit(v)

def _dfs_visit(v):
    time += 1
    v.d = time
    v.setColor('grey')
    for nbr in v.getConnections():
        if nbr.color == 'white':
            _dfs_visit(nbr)
    v.setColor('black')
    time += 1
    v.f = time
