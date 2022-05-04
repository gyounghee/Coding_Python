# linked_list 이용
def solution(n, k, cmd):
    class node : 
        def __init__(self, idx, up, down):
            self.idx = idx
            self.up = up
            self.down = down
            self.state = 'O'

    def U(k, p):
        for _ in range(p):
            k = linked_list[k].up
        return k

    def D(k, p):
        for _ in range(p):
            k = linked_list[k].down
        return k

    def C(k):
        pick = linked_list[k]
        trash_can.append(pick)
        pick.state = "X"
        if pick.up != None : linked_list[pick.up].down = pick.down
        if pick.down != None : linked_list[pick.down].up = pick.up
        return pick.down if pick.down != None else pick.up
            
    def Z(k):
        pick = trash_can.pop()
        pick.state = "O"
        if pick.up != None : linked_list[pick.up].down = pick.idx
        if pick.down != None : linked_list[pick.down].up = pick.idx
        return k
        
    # linked_list 생성
    linked_list = [node(i,i-1,i+1) for i in range(n)]
    linked_list[0].up = None
    linked_list[-1].down = None

    # 복구를 위한 휴지통 생성
    trash_can = []

    cmd = [c.split() for c in cmd]
    for c in cmd:
        if c[0] == 'U':  k = U(k,int(c[1]))
        elif c[0] == 'D':  k = D(k,int(c[1]))
        elif c[0] == 'C':  k = C(k)
        else :  k = Z(k) # "Z"일 때

    return "".join([node.state for node in linked_list])



# TEST CASE Ⅰ
n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))

# TEST CASE Ⅰ
n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
print(solution(n, k, cmd))
