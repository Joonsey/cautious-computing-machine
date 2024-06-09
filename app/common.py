import os
from app.sceptile import SceptileInterface

if os.environ['SERVICE_ADDRESS']:
    client = SceptileInterface(os.environ['SERVICE_ADDRESS'])
else:
    client = SceptileInterface()
