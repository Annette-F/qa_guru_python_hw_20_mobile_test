import os
from selene_in_action import utils

# context = os.getenv('context', 'bstack')

# run_on_bstack = os.getenv('run_on_bstack', 'false').lower() = 'true'
remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723')
deviceName = os.getenv('deviceName')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
app = os.getenv('app', './app-alpha-universal-release.apk')
runs_on_bstack = app.startswith('bs://')
if runs_on_bstack:
    remote_url = 'http://hub.browserstack.com/wd/hub'
bstack_userName = os.getenv('bstack_userName', 'anna_AdBgcK')
bstack_accessKey = os.getenv('bstack_accessKey', 'n9u5fcs9D7VG85hzWbwU')
# app_url = os.getenv('app_url', 'bs://sample.app')



