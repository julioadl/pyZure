#Python wrappers to access Azure cloud resources
import requests
import json

#Bing News
#Key (required)  is a string needed to access bing resources
#query (required) is a string indicating the search query. If more than one word, the queries should be concatenated with '&'
#count (optional) is an integer ranging bewteen 10 and 100 indicating the number of results bing will return
#market (optional) is a string indicating the region/language where bing is going to look for the information
#To get more info visit https://msdn.microsoft.com/en-us/library/dn760793.aspx
def bingNews(key, query, count = 10, market = 'en-us'):

#Set requests
    bingNews_url = 'https://api.cognitive.microsoft.com/bing/v5.0/news/search?q=' + query + '&count=' + str(count) + '&mkt=' + market
    header = {'Ocp-Apim-Subscription-Key': key}

#Send request
    r = requests.get(url = bingNews_url, headers = header)
    data = json.loads(r.text)

    return data

#Sentiment api
#Key (required)  is a string needed to access bing resources
#data (required) is a JSON formatted dictionary containing the documents to be analyzed - to see the exact format see https://azure.microsoft.com/en-us/documentation/articles/cognitive-services-text-analytics-quick-start/
#To get more info visit https://azure.microsoft.com/en-us/documentation/articles/cognitive-services-text-analytics-quick-start/
def sentimentAPI(key, data):

    #Set requeste
    sentimentAPI_url = 'https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment/'
    header = {'Ocp-Apim-Subscription-Key': key}

    #Send requests
    r = requests.post(url = sentimentAPI_url, headers = header, data = data)
    data = json.loads(r.text)

    return data
