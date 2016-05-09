def bfs(G, start):
    for v in G:
        v.setColor('white')
        v.setParent(None)
        v.setDistance(sys.maxint)
    start.setColor('grey')
    start.setDistance(0)
    q = Queue()
    q.enqueue(start)
    while not q.isEmpty():
        curr = q.dequeue()
        for u in curr.getConnections():
            if u.color == 'white':
                u.setParent(curr)
                u.setDistance(curr.distance+1)
                u.setColor('grey')
                q.enqueue(u)
        curr.setColor('black')
