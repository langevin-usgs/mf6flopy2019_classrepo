# setup absolute paths to the executables based on the OS

import sys
import os

bindir = '../bin'
exeext = ''

if sys.platform.lower() == 'darwin':
    exepth = os.path.join(bindir, 'macos')
elif sys.platform.lower() == 'linux':
    exepth = os.path.join(bindir, 'linux')
elif 'win' in sys.platform.lower():
    exeext = '.exe'
    winarch = 'win64'  #change to 'win32' for a 32-bit system
    exepth = os.path.join(bindir, winarch)
else:
    raise Exception('Could not find binaries for {}'.format(sys.platform))    

def add_to_config(name, exeext):
    exe = os.path.abspath(os.path.join(exepth, name.format(exeext)))
    return exe


mfexe = os.path.abspath(os.path.join(exepth, 'mf2005{}'.format(exeext)))
mpexe = os.path.abspath(os.path.join(exepth, 'mp7{}'.format(exeext)))
mtexe = os.path.abspath(os.path.join(exepth, 'mt3dms{}'.format(exeext)))
mf6exe = os.path.abspath(os.path.join(exepth, 'mf6{}'.format(exeext)))

exelist = [mfexe, mpexe, mtexe, mf6exe]
for e in exelist:
    if not os.path.isfile(e):
        print('Executable file could not be found: {}'.format(e))
    else:
        print('Executable file found: {}'.format(e))
