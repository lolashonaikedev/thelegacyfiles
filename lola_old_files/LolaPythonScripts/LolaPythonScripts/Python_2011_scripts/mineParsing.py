from itertools import izip

infile1 = open("Solution_Score.csv", "r").readlines()
infile2 = open("Logs.csv", "r").readlines()
t1 = map(lambda s: s.strip(), infile1)
t2 = map(lambda s: s.strip(), infile2)

ARScore = [x.split(',') for x in t1]
ARSname = dict((item[0],int(item[1])) for item in ARScore[1:])

countFnct = lambda cnt, dictInput : sum( x == cnt for x in dictInput.values())

countLimit = 6
counts = [countFnct(x,ARSname) for x in xrange(countLimit+1)]
#count0 = countFnct(0,ARSname)
#count1 = countFnct(1,ARSname)
#count2 = countFnct(2,ARSname)
#count3 = countFnct(3,ARSname)
#count4 = countFnct(4,ARSname)
#count5 = countFnct(5,ARSname)
#count6 = countFnct(6,ARSname)
print counts


## list of the six tools
toolsList = ['solar system', 'alien database','mission control','notebook','probe launch','probe design']


ARTcore = [x.split(',') for x in t2]
ARTname = dict((item[0],item[1]) for item in ARTcore[1:])

# These are the names of the user name of those who used the specified tools
# key list of what she called ARTable
StudentNameWhoUsedTools = [v for v, x in ARTname.items() if x in toolsList]
countNull = len(ARTname) - len(StudentNameWhoUsedTools)

