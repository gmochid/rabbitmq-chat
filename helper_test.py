from pprint import pprint
from helper import ConnHelper

# testing class ConnHelper

connhelper = ConnHelper()

pprint (vars(connhelper.connection))
print '--------------'
pprint (vars(connhelper.connection.channel))
print '--------------'
pprint (vars(connhelper.channel))
