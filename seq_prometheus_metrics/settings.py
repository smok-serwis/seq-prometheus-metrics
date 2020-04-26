import os

SEQ_ADDRESS = os.environ['SEQ_ADDRESS']
if not SEQ_ADDRESS.endswith('/'):
    SEQ_ADDRESS = SEQ_ADDRESS + '/'
BIND_ADDRESS = os.environ['BIND_ADDRESS']
BIND_PORT = int(os.environ['BIND_PORT'])
SEQ_API_KEY = os.environ.get('SEQ_API_KEY')
