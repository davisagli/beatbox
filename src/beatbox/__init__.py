from beatbox._beatbox import _tPartnerNS, _tSObjectNS, _tSoapNS, SoapFaultError, SessionTimeoutError
from beatbox._beatbox import DEFAULT_SERVER_URL
from beatbox._beatbox import Client as XMLClient
from beatbox.python_client import Client as PythonClient

__all__ = (
    'XMLClient', '_tPartnerNS', '_tSObjectNS', '_tSoapNS',
    'SoapFaultError', 'SessionTimeoutError', 'PythonClient', 'DEFAULT_SERVER_URL')
