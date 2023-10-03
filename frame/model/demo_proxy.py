import puremvc.patterns.proxy


class DemoProxy(puremvc.patterns.proxy.Proxy):
    NAME = "DemoProxy"

    def __init__(self, proxyName=None, data=None):
        super(DemoProxy, self).__init__(DemoProxy.NAME, [])

    def onRegister(self):
        print("DemoProxy onRegister")

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data
