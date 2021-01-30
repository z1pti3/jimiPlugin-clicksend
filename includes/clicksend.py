import requests
import json
import time
import base64
from pathlib import Path

class _clicksend():
    url = "https://rest.clicksend.com/v3"
    
    def __init__(self, username, apiToken, ca=None, requestTimeout=30):
        self.requestTimeout = requestTimeout
        self.headers = {
            "Authorization" : "Basic {0}".format(base64.b64encode("{0}:{1}".format(username,apiToken).encode()).decode()),
            "Content-Type": "application/json"
        }
        self.apiToken = apiToken
        if ca:
            self.ca = Path(ca)
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["headers"] = self.headers
        kwargs["timeout"] = self.requestTimeout
        if self.ca:
            kwargs["verify"] = self.ca
        try:
            if methord == "GET":
                response = requests.get("{0}/{1}".format(self.url,endpoint), **kwargs)
            elif methord == "POST":
                kwargs["data"] = json.dumps(data)
                response = requests.post("{0}/{1}".format(self.url,endpoint), **kwargs)
            elif methord == "PUT":
                kwargs["data"] = json.dumps(data)
                response = requests.put("{0}/{1}".format(self.url,endpoint), **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return 0, "Connection Timeout"
        if response.status_code == 200:
            return json.loads(response.text), response.status_code
        return response.text, response.status_code

    def sendSMS(self,to,body):
        jsonMessages = { "messages" : [ { "source" : "jimi", "to" : to, "body" : body } ] }
        response, statusCode = self.apiCall("sms/send",methord="POST",data=jsonMessages)
        return response, statusCode

    def getAccount(self):
        response, statusCode = self.apiCall("account")
        return response, statusCode

    def getAccountUsage(self,year,month):
        response, statusCode = self.apiCall("account/usage/{0}/{1}/subaccount".format(year,month))
        return response, statusCode

    def pullUnreadSMS(self):
        response, statusCode = self.apiCall("sms/inbound")
        if statusCode == 200:
            self.apiCall("sms/inbound-read",methord="PUT",data={})
        return response, statusCode

