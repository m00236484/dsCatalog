import urllib
import json
import requests
import wget
import boto3
import os

class FdaAdapter():
    def __init__(self):
        self.id = None

    def getDsRequest(self):
        url = "https://api.fda.gov/download.json"
        response = urllib.urlopen(url)
        return response


    def processResponse(self, response):
        data = json.loads(response.read())
        results = data['results']
        # Get the service client
        s3 = boto3.client('s3')
        sDir = ''
        for category  in data['results'].keys():
            dataSets = data['results'][category]
            for ds in dataSets.keys():
                dataset = dataSets[ds]
                for i in  dataset['partitions']:
                    url =  i['file']
                    print "Download File :" + url
                    #r = requests.get(url, "~/tmp")
                    filename = wget.download(url)
                    sDir= 'fda' + '/'+ category + '/' +ds +'/'+filename
                    s3.upload_file(filename, "datainsight-dc", sDir)
                    os.remove(filename)
                    #print(r.text)
if __name__ == '__main__':
    fdAd = FdaAdapter()
    fdAd.processResponse(fdAd.getDsRequest())

