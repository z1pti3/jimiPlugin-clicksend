import jimi

class _clicksend(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        jimi.model.registerModel("clicksendSMS","_clicksendSMS","_action","plugins.clicksend.models.action")
        jimi.model.registerModel("clicksendPullUnreadSMS","_clicksendPullUnreadSMS","_action","plugins.clicksend.models.action")
        jimi.model.registerModel("clicksendGetAccountUsage","_clicksendGetAccountUsage","_action","plugins.clicksend.models.action")
        jimi.model.registerModel("clicksendGetAccountInfo","_clicksendGetAccountInfo","_action","plugins.clicksend.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("clicksendSMS","_clicksendSMS","_action","plugins.clicksend.models.action")
        jimi.model.deregisterModel("clicksendPullUnreadSMS","_clicksendPullUnreadSMS","_action","plugins.clicksend.models.action")
        jimi.model.deregisterModel("clicksendGetAccountUsage","_clicksendGetAccountUsage","_action","plugins.clicksend.models.action")
        jimi.model.deregisterModel("clicksendGetAccountInfo","_clicksendGetAccountInfo","_action","plugins.clicksend.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        pass
        #if self.version < 0.2:
