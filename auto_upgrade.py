from fabric.api import env, run
from fabric.context_managers import settings

##### Old Automation station #####
## env.hosts = ['10.20.4.228']  # Default remote host IP address. Overidden during deployment
## env.user = 'root'  # Default VMs user name
## env.password = 'securitydam'

##### New Automation station #####
env.hosts = ['10.20.4.10']
env.user = 'root'
env.password = '123456'

## Master Setup (Test setup)
UPGRADE_1 = 'sdcc_upgrade_tni:19.12,10.20.4.81,10.20.4.4,10.20.4.70,all'
UPGRADE_11 = 'sdcc_upgrade_mbi:19.12,10.20.4.132,10.20.4.4,all'

##Screen comparison
UPGRADE_2 = 'sdcc_upgrade_sni:kenya_sp2,10.20.4.72,all'

##Master Setup (For migration tests)
UPGRADE_4 = 'sdcc_upgrade_tni:kenya_sp2,10.20.4.68,10.20.4.122,10.20.4.9,all'
UPGRADE_41 = 'sdcc_upgrade_mbi:kenya_sp2,10.20.4.77,10.20.4.122,all'

##MSSP Setup
UPGRADE_5 = 'sdcc_upgrade_sni:mssp_2.3,10.20.4.178,all'

UPGRADES_L = [UPGRADE_1,
              UPGRADE_11]

UPGRADES_K = [UPGRADE_4,
              UPGRADE_41]

UPGRADES_MSSP = [UPGRADE_5]

UPGRADE_STRING_L = '"' + '","'.join(upgrade.replace(',', '\,') for upgrade in UPGRADES_L) + '"'
UPGRADE_STRING_K = '"' + '","'.join(upgrade.replace(',', '\,') for upgrade in UPGRADES_K) + '"'
UPGRADE_STRING_MSSP = '"' + '","'.join(upgrade.replace(',', '\,') for upgrade in UPGRADES_MSSP) + '"'

def run_update():
    with settings(host_string=env.hosts[0]):
        run('fab -f /root/automation_19.8/fabfile.py auto_upgrade:' + UPGRADE_STRING_L )
        print '###########################################################'
        print '########## END OF PRIMARY SETUP (MASTER) UPGRADE ##########'
        print '###########################################################'

##        run('fab -f /root/automation_19.3/fabfile.py auto_upgrade:' + UPGRADE_STRING_K )
##        print '################################################################'
##        print '########## END OF SECONDARY SETUP (KENYA_SP2) UPGRADE ##########'
##        print '################################################################'

##        run('fab -f /root/automation_mssp_2.3/fabfile.py auto_upgrade:' + UPGRADE_STRING_MSSP )
##        print '########## END OF MSSP_2.3 SETUP UPGRADE ##########'
##        print '###############################################'

if __name__ == '__main__':
    run_update()