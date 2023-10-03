"""
 PureMVC Python Port by Toby de Havilland <toby.de.havilland@puremvc.org> 
 PureMVC - Copyright(c) 2006-08 Futurescale, Inc., Some rights reserved. 
 Your reuse is governed by the Creative Commons Attribution 3.0 License 
"""

import puremvc.interfaces
import puremvc.patterns.facade


class Observer(puremvc.interfaces.IObserver):
    """
    A base C{IObserver} implementation.
    
    An C{Observer} is an object that encapsulates information
    about an interested object with a method that should 
    be called when a particular C{INotification} is broadcast.
    
    In PureMVC, the C{Observer} class assumes these responsibilities:

    Encapsulate the notification (callback) method of the interested object.
    
    Encapsulate the notification context (this) of the interested object.
    
    Provide methods for setting the notification method and context.
    
    Provide a method for notifying the interested object.
    
    @see: L{View<org.puremvc.as3.core.view.View>}
    @see: L{Notification<org.puremvc.as3.patterns.observer.Notification>}
    """
    notify = None
    context = None

    def __init__(self, notifyMethod, notifyContext):
        """
        Constructor. 
        
        The notification method on the interested object should take 
        one parameter of type C{INotification}
        
        @param notifyMethod: the notification method of the interested object
        @param notifyContext: the notification context of the interested object
        """
        self.setNotifyMethod(notifyMethod)
        self.setNotifyContext(notifyContext)

    def setNotifyMethod(self, notifyMethod):
        """
        Set the notification method.
        
        The notification method should take one parameter of type C{INotification}.
        
        @param notifyMethod: the notification (callback) method of the interested object.
        """
        self.notify = notifyMethod

    def setNotifyContext(self, notifyContext):
        """
        Set the notification context.
        
        @param notifyContext: the notification context (this) of the interested object.
        """
        self.context = notifyContext

    def getNotifyMethod(self):
        """
        Get the notification method.
        
        @return: the notification (callback) method of the interested object.
        """
        return self.notify

    def getNotifyContext(self):
        """
        Get the notification context.
        
        @return: the notification context (C{this}) of the interested object.
        """
        return self.context

    def notifyObserver(self, notification):
        """
        Notify the interested object.
        
        @param notification: the C{INotification} to pass to the interested object's notification method.
        """
        self.getNotifyMethod()(notification)

    def compareNotifyContext(self, obj):
        """
        Compare an object to the notification context. 
        
        @param obj: the object to compare
        @return: boolean indicating if the object and the notification context are the same
        """
        return (obj is self.context)


class Notifier(puremvc.interfaces.INotifier):
    """
    A Base C{INotifier} implementation.
    
    C{MacroCommand, Command, Mediator} and C{Proxy} 
    all have a need to send C{Notifications}.

    The C{INotifier} interface provides a common method called
    C{sendNotification} that relieves implementation code of 
    the necessity to actually construct C{Notifications}.

    The C{Notifier} class, which all of the above mentioned classes
    extend, provides an initialized reference to the C{Facade}
    Singleton, which is required for the convienience method
    for sending C{Notifications}, but also eases implementation as these
    classes have frequent C{Facade} interactions and usually require
    access to the facade anyway.
    
    @see: L{Facade<org.puremvc.as3.patterns.facade.Facade>}
    @see: L{Mediator<org.puremvc.as3.patterns.mediator.Mediator>}
    @see: L{Proxy<org.puremvc.as3.patterns.proxy.Proxy>}
    @see: L{SimpleCommand<org.puremvc.as3.patterns.command.SimpleCommand>}
    @see: L{MacroCommand<org.puremvc.as3.patterns.command.MacroCommand>}
    """

    facade = None

    def __init__(self):
        """
        Notifier Constructor
        """
        self.facade = puremvc.patterns.facade.Facade.getInstance()

    def sendNotification(self, notificationName, body=None, type=None):
        """
        Create and send an C{INotification}.
        
        Keeps us from having to construct new INotification 
        instances in our implementation code.
        
        @param notificationName: the name of the notiification to send
        @param body: the body of the notification (optional)
        @param type: the type of the notification (optional)
        """
        self.facade.sendNotification(notificationName, body, type)


class Notification(puremvc.interfaces.INotification):
    """
    A base C{INotification} implementation.
    
    PureMVC does not rely upon underlying event models such 
    as the one provided with Flash, and ActionScript 3 does 
    not have an inherent event model.</P>
    
    The Observer Pattern as implemented within PureMVC exists 
    to support event-driven communication between the 
    application and the actors of the MVC triad.</P>
    
    Notifications are not meant to be a replacement for Events
    in Flex/Flash/Apollo. Generally, C{IMediator} implementors
    place event listeners on their view components, which they
    then handle in the usual way. This may lead to the broadcast of C{Notification}s to 
    trigger C{ICommand}s or to communicate with other C{IMediators}. C{IProxy} and C{ICommand}
    instances communicate with each other and C{IMediator}s 
    by broadcasting C{INotification}s.</P>
    
    A key difference between Flash C{Event}s and PureMVC 
    C{Notification}s is that C{Event}s follow the 
    'Chain of Responsibility' pattern, 'bubbling' up the display hierarchy 
    until some parent component handles the C{Event}, while
    PureMVC C{Notification}s follow a 'Publish/Subscribe'
    pattern. PureMVC classes need not be related to each other in a 
    parent/child relationship in order to communicate with one another
    using C{Notification}s.
    
    @see: L{Observer<org.puremvc.as3.patterns.observer.Observer>}
    """

    name = None
    body = None
    type = None

    def __init__(self, name, body=None, type=None):
        """
        Constructor. 
        
        @param name: name of the C{Notification} instance. (required)
        @param body: the C{Notification} body. (optional)
        @param type; the type of the C{Notification} (optional)
        """
        self.name = name
        self.body = body
        self.type = type

    def getName(self):
        """
        Get the name of the C{Notification} instance.
        
        @return: the name of the C{Notification} instance.
        """
        return self.name

    def setBody(self, body):
        """
        Set the body of the C{Notification} instance.
        """
        self.body = body

    def getBody(self):
        """
        Get the body of the C{Notification} instance.
        
        @return: the body object.
        """
        return self.body

    def setType(self, type):
        """
        Set the type of the C{Notification} instance.
        """
        self.type = type;

    def getType(self):
        """
        Get the type of the C{Notification} instance.
        
        @return: the type
        """
        return self.type;

    def str(self):
        """
        Get the string representation of the C{Notification} instance.
        
        @return: the string representation of the C{Notification} instance.
        """
        msg = "Notification Name: " + self.getName();

        bd = "None"
        if self.body is not None:
            bd = str(self.body)

        ty = "None"
        if self.type is not None:
            ty = self.type

        msg += "\nBody:" + bd
        msg += "\nType:" + ty
        return msg;
