from fabric.api import env, run
from fabric.context_managers import settings

env.hosts = ['10.20.4.228']  # Default remote host IP address. Overidden during deployment
env.user = 'root'  # Default VMs user name
env.password = 'securitydam'

## NAVIGATE_J = 'cd /root/automation_japan/'
## NAVIGATE_K = 'cd /root/automation_kenya/'

##Master Setup (Test setup)
#UPGRADE_1 = 'sdcc_upgrade_tni:kenya_sp1,10.20.4.81,10.20.4.4,10.20.4.70,all'
#UPGRADE_11 = 'sdcc_upgrade_mbi:kenya_sp1,10.20.4.132,10.20.4.4,all'

##Master Setup (Test setup)
UPGRADE_1 = 'sdcc_upgrade_tni:kenya,10.20.4.81,10.20.4.4,10.20.4.70,all'
UPGRADE_11 = 'sdcc_upgrade_mbi:kenya,10.20.4.132,10.20.4.4,all'

##Screen comparison
UPGRADE_2 = 'sdcc_upgrade_sni:kenya_sp1,10.20.4.72,all'

##Master Setup (For migration tests)
UPGRADE_4 = 'sdcc_upgrade_tni:kenya_sp1,10.20.4.68,10.20.4.122,10.20.4.8,all'
UPGRADE_41 = 'sdcc_upgrade_mbi:kenya_sp1,10.20.4.77,10.20.4.122,all'

##MSSP Setup
UPGRADE_5 = 'sdcc_upgrade_sni:mssp_2.3,10.20.4.178,all'

UPGRADES_K = [UPGRADE_1,
              UPGRADE_11]

UPGRADES_J = [UPGRADE_4,
              UPGRADE_41]

UPGRADES_MSSP = [UPGRADE_5]

UPGRADE_STRING_K = '"' + '","'.join(upgrade.replace(',', '\,') for upgrade in UPGRADES_K) + '"'
UPGRADE_STRING_J = '"' + '","'.join(upgrade.replace(',', '\,') for upgrade in UPGRADES_J) + '"'
UPGRADE_STRING_MSSP = '"' + '","'.join(upgrade.replace(',', '\,') for upgrade in UPGRADES_MSSP) + '"'

def run_update():
    with settings(host_string=env.hosts[0]):
        run('fab -f /root/automation_kenya/fabfile.py auto_upgrade:' + UPGRADE_STRING_K)
        print '########## END OF KENYA_SP1 SETUP UPGRADE ##########'
        print '################################################'
        run('fab -f /root/automation_kenya/fabfile.py auto_upgrade:' + UPGRADE_STRING_J )
        print '########## END OF KENYA_SP1 SETUP UPGRADE ##########'
        print '################################################'
        run('fab -f /root/automation_mssp_2.3/fabfile.py auto_upgrade:' + UPGRADE_STRING_MSSP )
        print '########## END OF MSSP_2.3 SETUP UPGRADE ##########'
        print '###############################################'

if __name__ == '__main__':
    run_update()