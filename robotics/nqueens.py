import time

class NQueens:
    def __init__ (self, size):
        self.size = size
        self.solutions = 0
        self.solve()

    def solve(self):
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        print("Found", self.solutions, "solutions. for ",self.size,"*",self.size," board")

    def put_queen(self, positions, target_row):
        if target_row==self.size:
            self.solutions+=1
            #self.show_full_board(positions)
        else:
            for column in range(self.size):
                if self.check_place(positions,target_row,column):
                    positions[target_row]=column
                    self.put_queen(positions,target_row+1)

    def check_place(self, positions,ocuppied_rows,column):
        for i in range(ocuppied_rows):
            if positions[i]==column or positions[i]-i== column-ocuppied_rows or positions[i]+i==column +ocuppied_rows:
                return False
        return True       

"""     def show_full_board(self,positions):
        for row in range(self.size):
            line=""
            for column in range(self.size):
                if positions[row]==column:
                    line+="Q "
                else:
                    line+=". "
            print(line,end="\n")
        print() """

def main(i):
    NQueens(i)

timelist=[]
for i in range(4,15):
    start = time.time()
    main(i)
    end = time.time()
    timelist.append((end-start) * 10**3)
print(timelist)

#[4.292488098144531, 13.027667999267578, 3.985166549682617, 52.99735069274902, 154.01244163513184, 820.6207752227783, 1959.0115547180176]
#[1.0018348693847656, 0.9980201721191406, 1.0025501251220703, 1.9974708557128906, 12.598752975463867, 51.22947692871094, 245.93591690063477]
#[1.0008811950683594, 1.0018348693847656, 0.9999275207519531, 2.3725032806396484, 9.952783584594727, 51.697492599487305, 240.98682403564453, 1393.5356140136719, 8277.04906463623, 58851.69053077698, 426170.65834999084]