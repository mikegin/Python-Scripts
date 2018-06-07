#import sys


#data = sys.stdin.read()
#print data

import sys
import fileinput
import pprint

map = {} #id -> [timeBeforeTranslation, timeAfterTranslation, timeAfterIndex]

minTimeStamp = sys.maxint
maxTimeStamp = -sys.maxint - 1

for line in fileinput.input():
    words = line.split()
    beforeAfter = words[1]
    indexTranslation = words[2]
    id = words[4]
    timeStamp = words[5]

    #print beforeAfter, indexTranslation, timeStamp

    #check for max/min
    if int(timeStamp) < minTimeStamp:
        minTimeStamp = int(timeStamp)

    if int(timeStamp) > maxTimeStamp:
        maxTimeStamp = int(timeStamp)

    #initialize key mapping
    if id not in map:
        map[id] = [None]*3

    #BEFORE and TRANSLATION -> position 0
    if beforeAfter == 'BEFORE':
        map[id][0] = timeStamp
    #AFTER and TRANSLATION -> position 1
    elif indexTranslation == 'TRANLSATION':
        map[id][1] = timeStamp
    #AFTER and INDEX -> position 2
    else:
        map[id][2] = timeStamp


#Average translation time
avgTrTime = 0
#Average index time
avgIndTime = 0

for id in map:
    avgTrTime = avgTrTime + (int(map[id][1]) - int(map[id][0]))
    avgIndTime = avgIndTime + (int(map[id][2]) - int(map[id][1]))

avgTrTime = avgTrTime / len(map)
avgIndTime = avgIndTime / len(map)

#Total time to translate and index a post
totalTime = maxTimeStamp - minTimeStamp

print "Average translation time: " + str(avgTrTime)
print "Average indexing time: " + str(avgIndTime)
print "Total time: " + str(totalTime)

#pprint.pprint(map)
