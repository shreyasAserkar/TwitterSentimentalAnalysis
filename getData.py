
import tweepy
import csv #Import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

auth = tweepy.auth.OAuthHandler('gAsENP9Qv7FvzUsei4taAn0O4', 'fOfKfiGJDYxcEh9tyeIH0mdvqEeR12Pc2hmuxKcbLmp59MmOjB')
auth.set_access_token('1914365996-OdMlCzyEFkqpHkqUIuFfB8CncSdCTJYP8xUgrYS', 'TCPgeZyZq4TKcYj2dBmfk4ftlOrXeYDyfeEiu3st2xlfT')

api = tweepy.API(auth)


csvFile = open('result_MANchsterUNTD3.csv', 'a')


csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = "Manchester United",
                           since = "2017-10-28",
                           until = "2017-11-29",
                           lang = "en").items():

    #Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text.encode('utf-8')
csvFile.close()




