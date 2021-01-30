import jimi
from plugins.clicksend.includes import clicksend

class _clicksendSMS(jimi.action._action):
    username = str()
    apiToken = str()
    to = str()
    body = str()
    
    def run(self,data,persistentData,actionResult):
        username = self.username
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)
        to = jimi.helpers.evalString(self.to,{"data" : data})
        body = jimi.helpers.evalString(self.body,{"data" : data})
        
        result, statusCode = clicksend._clicksend(username,apiToken).sendSMS(to,body)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from clicksend API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_clicksendSMS,self).setAttribute(attr,value,sessionData=sessionData)

class _clicksendPullUnreadSMS(jimi.action._action):
    username = str()
    apiToken = str()
    
    def run(self,data,persistentData,actionResult):
        username = self.username
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)
        
        result, statusCode = clicksend._clicksend(username,apiToken).pullUnreadSMS()

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from clicksend API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_clicksendPullUnreadSMS,self).setAttribute(attr,value,sessionData=sessionData)

class _clicksendGetAccountUsage(jimi.action._action):
    username = str()
    apiToken = str()
    year = str()
    month = str()
    
    def run(self,data,persistentData,actionResult):
        username = self.username
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)
        year = jimi.helpers.evalString(self.year,{"data" : data})
        month = jimi.helpers.evalString(self.month,{"data" : data})
        
        result, statusCode = clicksend._clicksend(username,apiToken).getAccountUsage(year,month)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from clicksend API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_clicksendGetAccountUsage,self).setAttribute(attr,value,sessionData=sessionData)

class _clicksendGetAccountInfo(jimi.action._action):
    username = str()
    apiToken = str()
    
    def run(self,data,persistentData,actionResult):
        username = self.username
        apiToken = jimi.auth.getPasswordFromENC(self.apiToken)
        
        result, statusCode = clicksend._clicksend(username,apiToken).getAccount()

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from clicksend API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiToken" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiToken = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_clicksendGetAccountInfo,self).setAttribute(attr,value,sessionData=sessionData)