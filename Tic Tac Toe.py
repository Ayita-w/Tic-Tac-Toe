def sum(a,b,c):
   return a + b + c 
def printBoard(xState,State_0):
   zero='X' if xState[0] else ('O' if State_0[0] else 0)
   one= 'X' if xState[1] else ('O' if State_0[1] else 1)
   two='X' if xState[2] else ('O' if State_0[2] else 2)
   three='X' if xState[3] else ('O' if State_0[3] else 3)
   four='X' if xState[4] else ('O' if State_0[4] else 4)
   five='X' if xState[5] else ('O' if State_0[5] else 5)
   six='X' if xState[6] else ('O' if State_0[6] else 6)
   seven='X' if xState[7] else ('O' if State_0[7] else 7)
   eight='X' if xState[8] else ('O' if State_0[8] else 8)
   print(f" {zero} | {one} | {two} ") 
   print(     f"--|---|--") 
   print(f" {three} | {four} | {five} ")
   print(     f"--|---|--")  
   print(f" {six} | {seven} | {eight} ") 

def checkwin(xState, State_0):
    wins= [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
            print("X Won the match!!")
            return 1
        if(sum(State_0[win[0]],State_0[win[1]],State_0[win[2]])==3):
            print("0 Won the match!!")
            return 0 
    return -1

     
if __name__ == "__main__":
        xState = [0,0,0,0,0,0,0,0,0]
        State_0 = [0,0,0,0,0,0,0,0,0]
        turn= 1 # 1 for x and 0 for zero
        print("****Welcome to Tic Tac Toe Game****")
        while(True):
            printBoard(xState,State_0)
            if(turn==1):
                print("X's Turn")
                value=int(input("PLease enter a value"))
                xState[value]=1
            else:
                print("0's Turn")
                value=int(input("PLease enter a value: "))
                State_0[value] =1
            cwin= checkwin(xState, State_0) 
            if(cwin != -1): 
                print("Match Over!")
                break  
            turn = 1- turn 
            
            