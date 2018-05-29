from nltk.stem import PorterStemmer, WordNetLemmatizer

lemmatiser = WordNetLemmatizer()

import io
import csv
from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize


with open('filteredtext1.txt', 'rb') as csvfile:
     tweetreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in tweetreader:
        try:
            for r in row[0].split():
                        appendFile = open('filteredtext_Lemma.txt','a')
                        appendFile.write(" "+ lemmatiser.lemmatize(r, pos="v"))
                        appendFile.close()
            appendFile = open('filteredtext_Lemma.txt','a')
            appendFile.write("\n")
            appendFile.close()
        except:
            print ''






