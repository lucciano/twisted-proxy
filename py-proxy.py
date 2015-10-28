"""
	uso :PROXY=127.0.0.1:8080 wget -e use_proxy=yes -e http_proxy=$PROXY http://www.lacapital.com/

	extraido de https://wiki.python.org/moin/Twisted-Examples
"""
from twisted.web import proxy, http
from twisted.internet import reactor
from twisted.python import log
import sys
log.startLogging(sys.stdout)
 
class ProxyFactory(http.HTTPFactory):
    protocol = proxy.Proxy
 
reactor.listenTCP(8080, ProxyFactory())
reactor.run()
