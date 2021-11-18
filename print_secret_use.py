import os

a = os.environ.get('MY_SECRET')
if a == 'SECRETVALUE':
    print('Secret correctly fetched')