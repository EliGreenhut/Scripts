from fabric.api import env, run
from fabric.context_managers import settings

env.hosts = ['10.20.4.228']  # Default remote host IP address. Overidden during deployment
env.user = 'root'  # Default VMs user name
env.password = 'securitydam'

NAVIGATE = 'cd /root/automation_japan/'

##Master Setup (Test setup)
UPGRADE_1 = 'sdcc_upgrade_tni:japan-sp1,10.20.4.81,10.20.4.4,10.20.4.70,all'
UPGRADE_11 = 'sdcc_upgrade_mbi:japan-sp1,10.20.4.132,10.20.4.4,all'

##Screen comparison
UPGRADE_2 = 'sdcc_upgrade_sni:japan-sp1,10.20.4.72,all'

##Master Setup (For migration tests)
UPGRADE_4 = 'sdcc_upgrade_tni:japan,10.20.4.68,10.20.4.122,10.20.4.8,all'
UPGRADE_41 = 'sdcc_upgrade_mbi:japan,10.20.4.77,10.20.4.122,all'

##MSSP Setup
UPGRADE_5 = 'sdcc_upgrade_sni:mssp_2.3,10.20.4.178,all'

UPGRADES_J = [UPGRADE_1,
              UPGRADE_11,
              UPGRADE_2,
              UPGRADE_4,
              UPGRADE_41]

UPGRADES_MSSP = [UPGRADE_5]

UPGRADE_STRING_J = '"' + '","'.join(upgrade.replace(',', '\,') for upgrade in UPGRADES_J) + '"'
UPGRADE_STRING_MSSP = '"' + '","'.join(upgrade.replace(',', '\,') for upgrade in UPGRADES_MSSP) + '"'

def run_update():
    with settings(host_string=env.hosts[0]):
        run('fab -f /root/automation_japan/fabfile.py auto_upgrade:' + UPGRADE_STRING_J )
        run('fab -f /root/automation_mssp_2.3/fabfile.py auto_upgrade:' + UPGRADE_STRING_MSSP )

if __name__ == '__main__':
    run_update()