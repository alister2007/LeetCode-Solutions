class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m,n=len(classroom),len(classroom[0])
        litter={}
        start=None

        #Finding start pt and litter numbering
        for i in range(m):
            for j in range(n):
                if classroom[i][j]=='S':
                    start=(i,j)
                elif classroom[i][j]=='L':
                    litter[(i,j)]=len(litter)

        #Mask represntation fof litter collected
        total=len(litter)
        target=(1<<total)-1

        #Definimg the state
        best={}
        best[(start[0],start[1],0)]=energy
        queue=[(start[0],start[1],energy,0)]
        directions=[(1, 0), (-1, 0), (0, 1), (0, -1)]
        moves=0
        head=0

        while head<len(queue):
            size=len(queue)-head
            for _ in range(size):
                r,c,e,mask=queue[head]
                head+=1

                #All letter collected
                if mask ==target:
                    return moves
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    #Outside grid
                    if nr<0 or nr>=m or nc<0 or nc>=n:
                        continue
                    #Obstacles
                    if classroom[nr][nc]=='X':
                        continue
                    #Low energy
                    if e==0:
                        continue
                    ne=e-1
                    new_mask=mask
                    #Collect litter
                    if (nr,nc) in litter:
                        new_mask |=1<<litter[(nr,nc)]
                    #Energy reset
                    if classroom[nr][nc]=='R':
                        ne=energy

                    key=(nr,nc,new_mask)
                    if ne>best.get(key,-1):
                        best[key]=ne
                        queue.append((nr,nc,ne,new_mask))
                        
            moves+=1
        return-1