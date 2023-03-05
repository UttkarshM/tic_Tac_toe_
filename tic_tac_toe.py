class Game:
    def __init__(self):
        self.board=[[3*y+x for x in range(3)] for y in range(3)]
        self.poss=[x for x in range(0,9)]
        self.moves=0
    
    def display(self):
        for x in range(3):
            for y in range(3):
                print(self.board[x][y],end=" ")
            print("\n")

    def logic(self):
            while True:
                #this is a infinte loop
                index=int(input("enter the index at which it is to be inserted at"))
                print(index)
                if index in self.poss:
                    self.poss.remove(index)
                    row=int(index/3)
                    column=(index)%3
                    self.board[row][column]=active[self.moves%2]
                    self.moves+=1
                    break#breaks from the infinte loop
                else:
                    print("invalid index")

    def is_win(self):
        for i in range(3):
            print("entered the range")
            if self.board[i][0]==self.board[i][1] and self.board[i][1]==self.board[i][2]:
                self.moves-=1
                print("enters")
                return 1
            elif self.board[0][i]==self.board[1][i] and self.board[1][i]==self.board[2][i]:
                self.moves-=1
                return 1

            elif self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2]:
                self.moves-=1
                return 1
            elif self.board[0][2]==self.board[1][1] and self.board[1][1]==self.board[2][0]:
                self.moves-=1
                return 1
            else:
                print("exits")
                return 0

        

active=["X","O"]
p1=Game()
while p1.moves<10:
    p1.display()
    p1.logic()
    if p1.is_win():
        print(active[p1.moves%2]+' has won')
        p1.display()
        break