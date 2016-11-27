#!/usr/bin/python -u

import os
import subprocess
import time

os.chdir('..')
output = subprocess.Popen(['svn', 'up'], stdout=subprocess.PIPE).communicate()[0]
if 'At revision' not in output:
    print 'samestrem-reloader: restarting samestrem'
    os.system('/etc/init.d/apache2 stop')
    os.system('/etc/init.d/apache2 start')
    # os.system('svc -t .')
time.sleep(5)
