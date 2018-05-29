
import io
import csv
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

with open('output.csv', 'rb') as csvfile:
     tweetreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in tweetreader:
        try:
            for r in row[0].split():
                if not r in stop_words:
                        appendFile = open('filteredtext1.txt','a')
                        appendFile.write(" "+r)
                        appendFile.close()
            appendFile = open('filteredtext1.txt','a')
            appendFile.write("\n")
            appendFile.close()
        except:
            print ''










