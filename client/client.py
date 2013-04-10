import os
import time
import urllib
from twisted.internet import reactor
from twisted.internet.protocol import Factory, Protocol
from twisted.internet.endpoints import TCP4ClientEndpoint
from config import SERVER as S

class Greeter(Protocol):
    def sendMessage(self, msg):
        self.transport.write("%s\n" % msg)
        pass

    def dataReceived(self, msg):
        msg = urllib.unquote(msg)
        os.system("export G_TITLE=%s;growl %s"% ("From\ Your\ Phone", msg))


class GreeterFactory(Factory):
    def buildProtocol(self, addr):
        return Greeter()


def gotProtocol(p):
    pass
    #p.sendMessage("Hello")
    #time.sleep(3)
    #reactor.callLater(1, p.sendMessage, "This is sent in a second")
    #reactor.callLater(2, p.transport.loseConnection)

point = TCP4ClientEndpoint(reactor, S['domain'], S['port'])
d = point.connect(GreeterFactory())
d.addCallback(gotProtocol)
reactor.run()
