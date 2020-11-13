import pyzm
import pyzm.api as zmapi
import getpass
import traceback
import pyzm.ZMMemory as zmmemory
import pyzm.helpers.utils as utils
from pyzm.helpers.Base import ConsoleLog



print ('Using pyzm version: {}'.format(pyzm.__version__))

logger = ConsoleLog()
logger.set_level(2)

conf = utils.read_config('/etc/zm/secrets.ini')
api_options  = {
    'apiurl': utils.get(key='ZM_API_PORTAL', section='secrets', conf=conf),
    'portalurl':utils.get(key='ZM_PORTAL', section='secrets', conf=conf),
    'user': utils.get(key='ZM_USER', section='secrets', conf=conf),
    'password': utils.get(key='ZM_PASSWORD', section='secrets', conf=conf),
    'logger': logger, # use none if you don't want to log to ZM,
    #'disable_ssl_cert_check': True
}

zmapi = zmapi.ZMApi(options=api_options)

event_filter = {
    'from': '9 am',
    'to': '7 pm',
    'object_only':False,
    'min_alarmed_frames': 0,
    'max_events':5,
    
}
cam_events = zmapi.events(event_filter)
print ('I got {} events'.format(len(cam_events.list())))
for e in cam_events.list():
    print ('Event:{} Cause:{} Notes:{}'.format(e.name(), e.cause(), e.notes()))




