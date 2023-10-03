"""
 PureMVC Python Port by Toby de Havilland <toby.de.havilland@puremvc.org> 
 PureMVC - Copyright(c) 2006-08 Futurescale, Inc., Some rights reserved. 
 Your reuse is governed by the Creative Commons Attribution 3.0 License 
"""

import puremvc.interfaces
import puremvc.patterns.facade
import puremvc.patterns.observer


class Proxy(puremvc.patterns.observer.Notifier, puremvc.interfaces.IProxy, puremvc.interfaces.INotifier):
    """
    A base C{IProxy} implementation. 
    
    In PureMVC, C{Proxy} classes are used to manage parts of the 
    application's data model.
    
    A C{Proxy} might simply manage a reference to a local data object, 
    in which case interacting with it might involve setting and 
    getting of its data in synchronous fashion.
    
    C{Proxy} classes are also used to encapsulate the application's 
    interaction with remote services to save or retrieve data, in which case, 
    we adopt an asyncronous idiom; setting data (or calling a method) on the 
    C{Proxy} and listening for a C{Notification} to be sent 
    when the C{Proxy} has retrieved the data from the service.
    
    @see: L{Model<org.puremvc.as3.core.model.Model>}
    """

    NAME = "Proxy"
    facade = None
    proxyName = None
    data = None

    def __init__(self, proxyName=None, data=None):
        """
        Proxy Constructor
        
        @param proxyName: the name of the proxy instance (optional)
        @param data: the proxy data (optional)
        """
        self.facade = puremvc.patterns.facade.Facade.getInstance()
        proxyName = proxyName or self.NAME
        if proxyName is None:
            raise ValueError("Proxy name cannot be None")
        self.proxyName = proxyName
        if data:
            self.setData(data)

    def getProxyName(self):
        """
        Get the Proxy name
        
        @return: the proxy name
        """
        return self.proxyName

    def setData(self, data):
        """
        Set the Proxy data
        
        @param data: the Proxy data object
        """
        self.data = data

    def getData(self):
        """
        Get the proxy data
        
        @return: the Proxy data object
        """
        return self.data

    def onRegister(self):
        """
        Called by the Model when the Proxy is registered
        """
        pass

    def onRemove(self):
        """
        Called by the Model when the Proxy is removed
        """
        pass
