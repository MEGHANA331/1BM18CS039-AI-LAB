

from _collections import defaultdict
class Graph:
    
    def __init__(self,vertices):
        
        self.ver = vertices
        self.graphlist = defaultdict(list)
        
        
    
    def Edgeaddition(self, u, v):
        self.graphlist[u].append(v)
        
        
    def DLS(self, s, t, d):
        
        if s == t: return True
        
        if d<= 0: return False
        
        for i in self.graphlist[s]:
            if(self.DLS(i, t, d-1)):
                return True
        return False    
        
        
    def IDDFS(self, s, t, d):
        for i in range(d):
            if(self.DLS(s,t,i)):
                return True
        return False    
        
        
tv=int(input("Enter the value of total vertices: "))        
g=Graph(tv)
for i in range(tv):
    x=int(input("Enter the value of left edge: "))
    y=int(input("Enter the value of right edge: "))
    g.Edgeaddition(x,y)


s=int(input("Enter the value of source edge: "))
t=int(input("Enter the value of target edge: "))
d=int(input("Enter the value of depth"))

if g.IDDFS(s, t, d)== True:
    print("Target is reachable")
else:
    print("Target is not reachable")        
