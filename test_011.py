# coding=utf-8

import ftplib
import os
import socket
import pdb


HOST = 'ftp.python.org'
DIRN = 'debian/tools'
FILE = 'loadlin.exe'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach "%s"' % HOST)
        return
    print('*** Connected to host "%s"' % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return 
    print('*** Logged in as "anonymous"')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print('***  changed to "%s" folder' % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE,
                     open(FILE,'wb').write)
    except ftplib.error_perm:
        print('ERROR: cannot read file "%s"' % FILE)
        os.unlink(FILE)
    else:
        print('*** Download "%s" to CWD' %FILE)
    f.quit()

if __name__ == '__main__':
    main()
