import random
import matplotlib.pyplot as plt
class stairs():
    position = 0
    histList = []
    def __init__(self):
        pass
    def start(self):
        for j in range(0,15):
            N = int(input("Enter number of times dice is rolled : "))
            for i in range(0,N) :
                x = random.randint(1,7)
                if x == 1 or x == 2 or x == 3 :
                    if self.position != 0:
                        self.position = self.position - 1
                elif x == 4 or  x == 5 :
                    self.position = self.position + 1
                else : 
                    x = random.randint(1,6)
                    self.position = self.position + x
            print("Position after "+str(N)+" iterations : "+str(self.position))
            self.histList.append(self.position)
            self.position = 0
    def drawHist(self):
        plt.hist(self.histList)
stairsObj = stairs()
stairsObj.start()
stairsObj.drawHist()
