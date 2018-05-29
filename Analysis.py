
import io
import csv

def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


bog = {}

with open('bow.csv', 'rb') as csvfile:
     bow_reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
     for row in bow_reader:
        bog[row[0]] = row[1]

#print bog

countN = 0
countP = 0
countNu = 0
tweetSentiWt = 0
with open('filteredtext_Lemma.txt', 'rb') as csvfile:
     tweetreader = csv.reader(csvfile, delimiter=',', quotechar='|')

     for row in tweetreader:
        try:
                for r in row[0].split():
                        if r.lower() in bog:
                                value = int(bog[r])

                                if value==0:
                                        countNu = countNu + 1
                                if value > 0:
                                        countP = countP + 1
                                if value < 0:
                                        countN = countN + 1

                if countNu>0 and countN ==0 and countP == 0:
                        print row[0] + ' : NEU'
                        print '0'
                elif countN < countP :
                        print row[0] + ' : POS'
                        print countP - countN
                elif  countN > countP :
                        print row[0] + ' : NEG'
                        print countN - countP
                elif countN == countP and countN !=0:
                        print row[0] + ' : MIX'
                        print '0'
                elif isEnglish(row[0]):
                        print row[0] + ' : NON'
                else:
                        print row[0] + ' : NEN'
                countP = 0
                countN = 0
                countNu = 0

        except Exception, e:
                print "Couldn't do it: %s" % e






