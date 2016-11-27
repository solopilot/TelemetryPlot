'''
Created on Nov 26, 2016

@author: solo
'''

from glob import glob
import os
import time

# make a release
def build():
    with open('version.py', 'w') as f:
        f.write('# autogen\nversionDate = "%s"\n' % time.strftime('%b %d, %Y'))
    print os.system('python setup.py py2exe')

# convert changed ui files to py
def make():
    files = glob('ui/*.ui')
    for fileName in files:
        stem = fileName.rstrip('ui')
        statUi = os.stat(fileName)

        try:
            statPy = os.stat(stem+'py')
            pytime = statPy[8]         # mtime
        except:
            pytime = 0
        if statUi[8] > pytime:         # mtime
            print 'compiling %sui' % stem
            print os.system('pyuic4 %s -o %spy' % (fileName, stem))

if __name__ == '__main__':
    make()
    build()
    print 'Done'
