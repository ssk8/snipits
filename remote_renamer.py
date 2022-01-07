from pathlib import Path
import paramiko

key_path = "/home/curt/.ssh/known_hosts"
kodi_address = "192.168.1.110"
kodi_hd_path = Path("/media/sda1-ata-WDC_WD20EZRZ-00Z")
ori_path = kodi_hd_path / 'TV Shows' / 'oldname'
target_path =  kodi_hd_path / 'TV Shows' / 'newname'

def get_sftp_client(address: str) -> paramiko.sftp_client.SFTPClient:
    ssh_client=paramiko.SSHClient()
    ssh_client.load_host_keys(key_path)
    ssh_client.connect(hostname=address, username='root')
    return ssh_client.open_sftp()


def main():
    kodi_sftp = get_sftp_client(kodi_address)
    ori_files = kodi_sftp.listdir_attr(f"{ori_path}")
    for f in ori_files:
        print(f"{f.filename} is a {(f.st_mode==16877)*'directory'}{(f.st_mode==33188)*'file'}")
        #kodi_sftp.rename(str(ori_path/f), str(target_path/new_name))

if __name__ == "__main__":
    main()