from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

PORT = '8888'

class Echo(Protocol):
    def sendMessage(self, msg):
        self.transport.write("%s" % msg)

    def dataReceived(self, data):
        #self.transport.write(data)
        if data.startswith('GET'):
            msg = data.split('\n')[0].split(' ')[1]
            msg = msg[6:]
            for x in self.factory.protocols:
                if x != self:
                    x.sendMessage(msg)
    def connectionLost(self, reason):
        print 'lost'
        self.factory.protocols.remove(self)


class EFactory(Factory):
    protocol = Echo
    def __init__(self, quote=None):
        self.quote = quote or 'An'
        self.protocols = []
    def buildProtocol(self, addr):
        p = self.protocol()
        p.factory = self
        self.protocols.append(p)
        return p



while True:
    endpoint = TCP4ServerEndpoint(reactor, PORT)
    endpoint.listen(EFactory("Ok"))
    reactor.run()
    print 'stop'
