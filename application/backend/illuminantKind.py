# CIE_DAYLIGHT2 = {
#     '2800':[74,48,91,50,96,193,205,591,109,908,913,677,697]
#     ,'3500':[162,86,163,81,154,272,266,724,92,653,611,666,493]
#     ,'4300':[148,173,222,92,291,438,414,1023,185,644,408,771,397]
#     ,'5000':[248,261,325,123,388,538,595,1023,230,634,376,838,236]
#     ,'5500':[320,313,388,140,438,585,655,1023,237,599,347,836,158]
#     ,'6500':[408,354,446,155,458,591,560,1023,178,445,270,702,103]
#     ,'7500':[466,376,481,163,464,585,473,1023,132,340,224,600,89]
#     ,'8000':[1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023,1023]
# }

# TEST = {
#      '1':[1023,0,0,0,0,0,0,0,0,0,0,0,0]
#     ,'2':[0,1023,0,0,0,0,0,0,0,0,0,0,0]
#     ,'3':[0,0,1023,0,0,0,0,0,0,0,0,0,0]
#     ,'4':[0,0,0,1023,0,0,0,0,0,0,0,0,0]
#     ,'5':[0,0,0,0,1023,0,0,0,0,0,0,0,0]
#     ,'6':[0,0,0,0,0,1023,0,0,0,0,0,0,0]
#     ,'7':[0,0,0,0,0,0,1023,0,0,0,0,0,0]
#     ,'8':[0,0,0,0,0,0,0,1023,0,0,0,0,0]
#     ,'9':[0,0,0,0,0,0,0,0,1023,0,0,0,0]
#     ,'10':[0,0,0,0,0,0,0,0,0,1023,0,0,0]
#     ,'11':[0,0,0,0,0,0,0,0,0,0,1023,0,0]
#     ,'12':[0,0,0,0,0,0,0,0,0,0,0,1023,0]
#     ,'13':[0,0,0,0,0,0,0,0,0,0,0,0,1023]
# }

CIE_DAYLIGHT = {}

import sys

f = open('led.txt', 'r')

lines = f.readlines()

for line in lines:
    s = line.strip().split(',')
    name = s[0]
    il = name[0]
    p = name[1]
    val = []
    for i in range(13):
        val.append(int(s[i+1]))
    CIE_DAYLIGHT[name] = val