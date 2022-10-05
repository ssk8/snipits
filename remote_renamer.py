#!/usr/bin/python3

from pathlib import Path
from os import environ
import paramiko
import re
from typing import List

kodi_address = "192.168.1.110"
#kodi_hd_path = Path("/media/sda1-usb-WDC_WD20_EZRZ-00")
kodi_hd_path = Path("/media/sda1-ata-WDC_WD20EZRZ-00Z")
ori_path = kodi_hd_path / 'TV Shows' / 'old name'
target_path =  kodi_hd_path / 'TV Shows' / 'new name'

def get_remote(sftp_client: paramiko.sftp_client.SFTPClient, path, dirs=True) -> List[str]:
    """returns a list of remote directories at 'path' on 'sftp_client' if 'dirs' or list of files if not 'dirs'"""
    mode = 16877*dirs or 33188
    return [f.filename for f in sftp_client.listdir_attr(str(path)) if f.st_mode==mode]


def get_sftp_client(address: str) -> paramiko.sftp_client.SFTPClient:
    ssh_client=paramiko.SSHClient()
    ssh_client.load_host_keys("/home/curt/.ssh/known_hosts")
    ssh_client.connect(hostname=address, username='root')
    return ssh_client.open_sftp()


def main():
    kodi_sftp = get_sftp_client(kodi_address)
    ori_files = get_remote(kodi_sftp, ori_path, dirs=False)

    fixmatch = re.compile('S\d{2}E\d{2}')
    for f in ori_files:
        if se:=fixmatch.search(f):
            s, e = int(se.group()[1:3]), int(se.group()[4:])
            if s==1 and e>12:
                s, e = divmod(e, 12)
                s+=1
                new_name = fixmatch.sub(f'S{s:02}E{e:02}', f)
                kodi_sftp.rename(str(ori_path/f), str(target_path/new_name))
    if ori_path != target_path:
        kodi_sftp.rmdir(str(ori_path))

if __name__ == "__main__":
    main()
