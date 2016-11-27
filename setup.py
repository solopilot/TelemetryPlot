'''
Created on Nov 26, 2016

@author: solo

'''

from distutils.core import setup
import py2exe   # used inside quotes
from glob import glob

includes = ["sip", "PyQt4.QtGui"]
dataFiles = [('state', glob('state/*.*'))]
packages=[]
#data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

setup(name='telemetryPlot',
      version='1.0',
      author='cue',
      author_email="cue@pejaver.com",
      url="http://pejaver.com",
      #data_files = dataFiles,
      #console=['telemetryPlot.py' ],
      windows=['telemetryPlot.py'],
      options = {
        "py2exe": { "dll_excludes": ["MSVCP90.dll"],
                    "packages": packages,
                    "includes": includes }
        }
      )