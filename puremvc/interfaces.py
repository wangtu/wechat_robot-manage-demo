"""
 PureMVC Python Port by Toby de Havilland <toby.de.havilland@puremvc.org> 
 PureMVC - Copyright(c) 2006-08 Futurescale, Inc., Some rights reserved. 
 Your reuse is governed by the Creative Commons Attribution 3.0 License 
"""


class ICommand(object):
    """
    The interface definition for a PureMVC Command.

    @see: L{INotification<puremvc.interfaces.INotification>}
    """

    def execute(self, notification):
        """
        Execute the C{ICommand}'s logic to handle a given C{INotification}.

        Raises C{NotImplemented} if subclass does not implement this method

        @param notification: an C{INotification} to handle.
        """
        raise NotImplemented


class IController(object):
    """
    The interface definition for a PureMVC Controller.

    In PureMVC, an C{IController} implementor 
    follows the 'Command and Controller' strategy, and 
    assumes these responsibilities:

    Remembering which C{ICommand}s 
    are intended to handle which C{INotifications}.

    Registering itself as an C{IObserver} with
    the C{View} for each C{INotification} 
    that it has an C{ICommand} mapping for.
  
    Creating a new instance of the proper C{ICommand}
    to handle a given C{INotification} when notified by the C{View}.
  
    Calling the C{ICommand}'s C{execute}
    method, passing in the C{INotification}.
    

    @see: L{INotification<puremvc.interfaces.INotification>}
    @see: L{ICommand<puremvc.interfaces.ICommand>}
    """

    def registerCommand(self, notificationName, commandClassRef):
        """
        Register a particular C{ICommand} class as the handler for a particular C{INotification}.
        
        @param notificationName: the name of the C{INotification}
        @param commandClassRef: the Class of the C{ICommand}
        """
        raise NotImplemented

    def executeCommand(self, notification):
        """
        Execute the C{ICommand} previously registered as thehandler for C{INotification}s with the given notification name.
        
        @param notification: the C{INotification} to execute the associated C{ICommand} for
        """
        raise NotImplemented

    def removeCommand(self, notificationName):
        """
        Remove a previously registered C{ICommand} to C{INotification} mapping.
        
        @param notificationName: the name of the C{INotification} to remove the C{ICommand} mapping fo
        """
        raise NotImplemented

    def hasCommand(self, notificationName):
        """
        Check if a Command is registered for a given Notification 
        
        @param notificationName: the name of the C{INotification}
        @return: whether a Command is currently registered for the given C{notificationName}.
        """
        raise NotImplemented


class IFacade(object):
    """
    The interface definition for a PureMVC Facade.
    
    The Facade Pattern suggests providing a single
    class to act as a central point of communication 
    for a subsystem. 
    
    In PureMVC, the Facade acts as an interface between
    the core MVC actors (Model, View, Controller) and
    the rest of your application.
    
    @see: L{IModel<puremvc.interfaces.IModel>}
    @see: L{IView<puremvc.interfaces.IView>}
    @see: L{IController<puremvc.interfaces.IController>}
    @see: L{ICommand<puremvc.interfaces.ICommand>}
    @see: L{INotification<puremvc.interfaces.INotification>}
    """

    def notifyObservers(self, note):
        """
        Notify the C{IObserver}s for a particular C{INotification}.

        All previously attached IObservers for this INotification's list are notified 
        and are passed a reference to the INotification in the order in which they were registered.

        NOTE: Use this method only if you are sending custom Notifications. Otherwise use the 
        sendNotification method which does not require you to create the Notification instance.
        
        @param note: the C{INotification} to notify C{IObserver}s of.
        """
        raise NotImplemented

    def registerProxy(self, proxy):
        """
        Register an C{IProxy} with the C{Model} by name.
        
        @param proxy: the C{IProxy} to be registered with the C{Model}.
        """
        raise NotImplemented

    def retreieveProxy(self, proxyName):
        """
        Retrieve a C{IProxy} from the C{Model} by name.
        
        @param proxyName: the name of the C{IProxy} instance to be retrieved.
        @return: the C{IProxy} previously regisetered by C{proxyName} with the C{Model}.
        """
        raise NotImplemented

    def removeProxy(self, proxyName):
        """
        Remove an C{IProxy} instance from the C{Model} by name.
        
        @param proxyName: the C{IProxy} to remove from the C{Model}.
        @return: the C{IProxy} that was removed from the C{Model}
        """
        raise NotImplemented

    def hasProxy(self, proxyName):
        """
        Check if a Proxy is registered
        
        @param proxyName:
        @return: whether a Proxy is currently registered with the given C{proxyName}.
        """
        raise NotImplemented

    def registerCommand(self, noteName, commandClassRef):
        """
        Register an C{ICommand} with the C{Controller}.
        
        @param noteName: the name of the C{INotification} to associate the C{ICommand} with.
        @param commandClassRef: a reference to the C{Class} of the C{ICommand}.
        """
        raise NotImplemented

    def removeCommand(self, notificationName):
        """
         Remove a previously registered C{ICommand} to C{INotification} mapping from the Controller.
 
        @param notificationName: the name of the C{INotification} to remove the C{ICommand} mapping for
        """
        raise NotImplemented

    def hasCommand(self, notificationName):
        """
        Check if a Command is registered for a given Notification 

        @param notificationName: the name of the C{INotification}
        @return: whether a Command is currently registered for the given C{notificationName}.
        """
        raise NotImplemented

    def registerMediator(self, mediator):
        """
        Register an C{IMediator} instance with the C{View}.
 
        @param mediator: a reference to the C{Mediator} instance
        """
        raise NotImplemented

    def retreieveMediator(self, mediatorName):
        """
        Retrieve an C{IMediator} instance from the C{View}.
        
        @param mediatorName: the name of the C{IMediator} instance to retrievve
        @return: the C{IMediator} previously registered with the given C{mediatorName}.
        """
        raise NotImplemented

    def removeMediator(self, mediatorName):
        """
        Remove a C{IMediator} instance from the C{View}.
        
        @param mediatorName: name of the C{IMediator} instance to be removed.
        @return: the C{IMediator} instance previously registered with the given C{mediatorName}.
        """
        raise NotImplemented


class IMediator(object):
    """
    The interface definition for a PureMVC Mediator.
    
    In PureMVC, C{IMediator} implementors assume these responsibilities:

    Implement a common method which returns a list of all C{INotification}s the C{IMediator} has interest in.
    
    Implement a notification callback method.
    
    Implement methods that are called when the IMediator is registered or removed from the View.
    
    
    Additionally, C{IMediator}s typically:

    Act as an intermediary between one or more view components such as text boxes or list controls, maintaining references and coordinating their behavior.
    
    In Flash-based apps, this is often the place where event listeners are
    added to view components, and their handlers implemented.
    
    Respond to and generate C{INotifications}, interacting with of the rest of the PureMVC app.
    
    When an C{IMediator} is registered with the C{IView}, the C{IView} will call the C{IMediator}'s C{listNotificationInterests} method. The C{IMediator} will 
    return an C{List} of C{INotification} names which 
    it wishes to be notified about.
    

    The C{IView} will then create an C{Observer} object 
    encapsulating that C{IMediator}'s (C{handleNotification}) method
    and register it as an Observer for each C{INotification} name returned by 
    C{listNotificationInterests}.
    
    @see: L{INotification<puremvc.interfaces.INotification>}
    """

    def getMediatorName(self):
        """
        Get the C{IMediator} instance name
        
        @return: the C{IMediator} instance name
        """
        raise NotImplemented

    def getViewComponent(self):
        """
        Get the C{IMediator}'s view component.
        
        @return: the view component
        """
        raise NotImplemented

    def setViewComponent(self, viewComponent):
        """
        Set the C{IMediator}'s view component.
        
        @param viewComponent: the view component
        """
        raise NotImplemented

    def listNotificationInterests(self):
        """
        List C{INotification} interests.
        
        @return: an C{List} of the C{INotification} names this C{IMediator} has an interest in.
        """
        raise NotImplemented

    def handleNotification(self, notification):
        """
        Handle an C{INotification}.
        
        @param notification: the C{INotification} to be handled
        """
        raise NotImplemented

    def onRegister(self):
        """
        Called by the View when the Mediator is registered
        """
        raise NotImplemented

    def onRemove(self):
        """
        Called by the View when the Mediator is removed
        """
        raise NotImplemented


class IModel(object):
    """
    The interface definition for a PureMVC Model.
    
    In PureMVC, C{IModel} implementors provide
    access to C{IProxy} objects by named lookup.
    
    An C{IModel} assumes these responsibilities:
    
    Maintain a cache of C{IProxy} instances and Provide methods for registering, retrieving, and removing C{IProxy} instances
    """

    def registerProxy(self, proxy):
        """
        Register an C{IProxy} instance with the C{Model}.
        
        @param proxy: an object reference to be held by the C{Model}.
        """
        raise NotImplemented

    def retrieveProxy(self, proxyName):
        """
        Retrieve an C{IProxy} instance from the Model.
        
        @param proxyName: name of the C{IProxy} instance to retrieve.
        @return: the C{IProxy} instance previously registered with the given C{proxyName}.
        """
        raise NotImplemented

    def removeProxy(self, proxyName):
        """
        Remove an C{IProxy} instance from the Model.
        
        @param proxyName: name of the C{IProxy} instance to be removed.
        @return: the C{IProxy} that was removed from the C{Model}
        """
        raise NotImplemented

    def hasProxy(self, proxyName):
        """
        Check if a Proxy is registered
        
        @param proxyName: name of the C{IProxy} instance
        @return: whether a Proxy is currently registered with the given C{proxyName}.
        """
        raise NotImplemented


class INotification(object):
    """
    The interface definition for a PureMVC Notification.

    PureMVC does not rely upon underlying event models such 
    as the one provided with Flash, and ActionScript 3 does 
    not have an inherent event model.
    
    The Observer Pattern as implemented within PureMVC exists 
    to support event-driven communication between the 
    application and the actors of the MVC triad.
    
    Notifications are not meant to be a replacement for Events
    in Flex/Flash/AIR. Generally, C{IMediator} implementors
    place event listeners on their view components, which they
    then handle in the usual way. This may lead to the broadcast of C{Notification}s to 
    trigger C{ICommand}s or to communicate with other C{IMediators}. C{IProxy} and C{ICommand}
    instances communicate with each other and C{IMediator}s by broadcasting C{INotification}s.
    
    A key difference between Flash C{Event}s and PureMVC 
    C{Notification}s is that C{Event}s follow the 
    'Chain of Responsibility' pattern, 'bubbling' up the display hierarchy 
    until some parent component handles the C{Event}, while
    PureMVC C{Notification}s follow a 'Publish/Subscribe'
    pattern. PureMVC classes need not be related to each other in a 
    parent/child relationship in order to communicate with one another
    using C{Notification}s.
    
    @see: L{IView<puremvc.interfaces.IView>}
    @see: L{IObserver<puremvc.interfaces.IObserver>}
    """

    def getName(self):
        """
        Get the name of the C{INotification} instance. 
        """
        raise NotImplemented

    def setBody(self, body):
        """
        Set the body of the C{INotification} instance
        """
        raise NotImplemented

    def getBody(self):
        """
        Get the body of the C{INotification} instance
        """
        raise NotImplemented

    def setType(self, type):
        """
        Set the type of the C{INotification} instance
        """
        raise NotImplemented

    def getType(self):
        """
        Get the type of the C{INotification} instance
        """
        raise NotImplemented

    def str(self):
        """
        Get the string representation of the C{INotification} instance
        """
        raise NotImplemented


class INotifier(object):
    """
    The interface definition for a PureMVC Notifier.
    
    C{MacroCommand, Command, Mediator} and C{Proxy}
    all have a need to send C{Notifications}.
    
    The C{INotifier} interface provides a common method called
    C{sendNotification} that relieves implementation code of 
    the necessity to actually construct C{Notifications}.
    
    The C{Notifier} class, which all of the above mentioned classes
    extend, also provides an initialized reference to the C{Facade}
    Singleton, which is required for the convienience method
    for sending C{Notifications}, but also eases implementation as these
    classes have frequent C{Facade} interactions and usually require
    access to the facade anyway.
    
    @see: L{IFacade<puremvc.interfaces.IFacade>}
    @see: L{INotification<puremvc.interfaces.INotification>}
    """

    def sendNotification(self, notificationName, body=None, type=None):
        """
        Send a C{INotification}.

        Convenience method to prevent having to construct new 
        notification instances in our implementation code.
        
        @param notificationName: the name of the notification to send
        @param body: the body of the notification (optional)
        @param type: the type of the notification (optional)
        """
        raise NotImplemented


class IObserver(object):
    """
    The interface definition for a PureMVC Observer.

    In PureMVC, C{IObserver} implementors assume these responsibilities:

    Encapsulate the notification (callback) method of the interested object.
    
    Encapsulate the notification context of the interested object.
    
    Provide methods for setting the interested object' notification method and context.
    
    Provide a method for notifying the interested object.
    

    PureMVC does not rely upon underlying event
    models such as the one provided with Flash,
    and ActionScript 3 does not have an inherent
    event model.
    

    The Observer Pattern as implemented within
    PureMVC exists to support event driven communication
    between the application and the actors of the
    MVC triad.
    

    An Observer is an object that encapsulates information
    about an interested object with a notification method that
    should be called when an C{INotification} is broadcast. The Observer then
    acts as a proxy for notifying the interested object.
    
    
    Observers can receive C{Notification}s by having their
    C{notifyObserver} method invoked, passing
    in an object implementing the C{INotification} interface, such
    as a subclass of C{Notification}.
    
    @see: L{IView<puremvc.interfaces.IView>}
    @see: L{INotification<puremvc.interfaces.INotification>}
    """

    def setNotifyMethod(self, notifyMethod):
        """
        Set the notification method.
        
        The notification method should take one parameter of type C{INotification}
        
        @param notifyMethod: the notification (callback) method of the interested object
        """
        raise NotImplemented

    def setNotifyContext(self, notifyContext):
        """
        Set the notification context.
        
        @param notifyContext: the notification context of the interested object
        """
        raise NotImplemented

    def notifyObserver(self, notification):
        """
        Notify the interested object.
        
        @param notification: the C{INotification} to pass to the interested object's notification method
        """
        raise NotImplemented

    def compareNotifyContext(self, object):
        """
        Compare the given object to the notificaiton context object.
        
        @param object: the object to compare.
        @return: boolean indicating if the notification context and the object are the same.
        """
        raise NotImplemented


class IProxy(object):
    """
    The interface definition for a PureMVC Proxy.

    In PureMVC, C{IProxy} implementors assume these responsibilities:

    Implement a common method which returns the name of the Proxy.
    
    Provide methods for setting and getting the data object.
    
    Additionally, C{IProxy}s typically:

    Maintain references to one or more pieces of model data.
    Provide methods for manipulating that data.
    Generate C{INotifications} when their model data changes.
    Expose their name as a C{public static const} called C{NAME}, if they are not instantiated multiple times.
    Encapsulate interaction with local or remote services used to fetch and persist model data.
    """

    def getProxyName(self):
        """
        Get the Proxy name
        
        @return: the Proxy instance name
        """
        raise NotImplemented

    def setData(self, data):
        """
        Set the data object
         
         @param data: the data object
        """
        raise NotImplemented

    def getData(self):
        """
        Get the data object
         
         @return: the data as type Object
        """
        raise NotImplemented

    def onRegister(self):
        """
        Called by the Model when the Proxy is registered
        """
        raise NotImplemented

    def onRemove(self):
        """
        Called by the Model when the Proxy is removed
        """
        raise NotImplemented


class IView(object):
    """
    The interface definition for a PureMVC View.
    
    In PureMVC, C{IView} implementors assume these responsibilities:
    
    In PureMVC, the C{View} class assumes these responsibilities:
    
    Maintain a cache of C{IMediator} instances.
    
    Provide methods for registering, retrieving, and removing C{IMediators}.
    
    Managing the observer lists for each C{INotification} in the application.
    
    Providing a method for attaching C{IObservers} to an C{INotification}'s observer list.
    
    Providing a method for broadcasting an C{INotification}.
    
    Notifying the C{IObservers} of a given C{INotification} when it broadcast.
    
    @see: L{IMediator<puremvc.interfaces.IMediator>}
    @see: L{IObserver<puremvc.interfaces.IObserver>}
    @see: L{INotification<puremvc.interfaces.INotification>}
    """

    def registerObserver(self, notificationName, observer):
        """
        Register an C{IObserver} to be notified of C{INotifications} with a given name.
        
        @param notificationName: the name of the C{INotifications} to notify this C{IObserver} of
        @param observer: the C{IObserver} to register
        """
        raise NotImplemented

    def notifyObservers(self, notification):
        """
        Notify the C{IObservers} for a particular C{INotification}.
        
        All previously attached C{IObservers} for this C{INotification}'s
        list are notified and are passed a reference to the C{INotification} in 
        the order in which they were registered.</P>
        
        @param notification: the C{INotification} to notify C{IObservers} of.
        """
        raise NotImplemented

    def registerMediator(self, mediator):
        """
        Register an C{IMediator} instance with the C{View}.
        
        Registers the C{IMediator} so that it can be retrieved by name,
        and further interrogates the C{IMediator} for its 
        C{INotification} interests.

        If the C{IMediator} returns any C{INotification} 
        names to be notified about, an C{Observer} is created encapsulating 
        the C{IMediator} instance's C{handleNotification} method 
        and registering it as an C{Observer} for all C{INotifications} the 
        C{IMediator} is interested in.
        
        @param mediator: a reference to the C{IMediator} instance
        """
        raise NotImplemented

    def retrieveMediator(self, mediatorName):
        """
        Retrieve an C{IMediator} from the C{View}.
        
        @param mediatorName: the name of the C{IMediator} instance to retrieve.
        @return: the C{IMediator} instance previously registered with the given C{mediatorName}.
        """
        raise NotImplemented

    def removeMediator(self, mediatorName):
        """
        Remove an C{IMediator} from the C{View}.
        
        @param mediatorName: name of the C{IMediator} instance to be removed.
        @return: the C{IMediator} that was removed from the C{View}
        """
        raise NotImplemented

    def hasMediator(self, mediatorName):
        """
        Check if a Mediator is registered or not
        
        @param mediatorName: name of the C{IMediator}
        @return: whether a Mediator is registered with the given C{mediatorName}.
        """
        raise NotImplemented
