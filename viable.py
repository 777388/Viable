import certstream
import shodan
try:
    certstream.core.time.mktime = shodan.__path__
except:
    shodan.__doc__.count.__closure__ = certstream.__path__