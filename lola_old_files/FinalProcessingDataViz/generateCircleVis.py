
class generateARCircleVis(object):
  def __init__(self, minAmt, counts,infile1,infile2):
     self.__minAmt = minAmt
     self.__counts = counts
     self.__infile1 = infile1
     self.__infile2 = infile2
     self.__ARSolutionScore = []
  def generateHTML(self):
      #Html print code will be placed here
  def decodeEvaluation(self):
     for line in self.__infile1:
         temp = line.strip().split(",")
         ARSolutionScore.append({"Student-name": temp[0], "Student-Score": temp[1]})
     



def main():
    infile1=open(input(str("Please enter the file with Students names and Score:")))
    infile2=open(input(str("Please enter the file with the Students Logs")))
    #minNum=eval(input(str("Please enter the minimum number for the solution score:")))
    countNum=eval(input("Please enter maximum number for solution score:"))
    countNum=countNum+1 
    ARFinalCircle = generateARCircleVis()
    ARFinalCircle.generateHTML()


main()
