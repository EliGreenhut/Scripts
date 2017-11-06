from fabric.api import env, run
from fabric.context_managers import settings

#env.hosts = ['10.20.4.238']  # Default remote host IP address. Overidden during deployment
env.user = 'root'  # Default VMs user name
env.password = 'radware'

def run_command(cmd, host):
    with settings(host_string=host):
        r = run(cmd, pty=False)
        print ''

if __name__ == '__main__':
    run_command('python DP_TrafficUtilizationSimulator.py --rate 40 --duration 15 --device 10.20.6.20 --policy PO-S2-N-Traf1 >& /dev/null < /dev/null &', '10.20.4.237')
    run_command('python DP_TrafficUtilizationSimulator.py --rate 65 --duration 15 --device 10.20.6.20 --policy PO-S2-N-Traf2 >& /dev/null < /dev/null &', '10.20.4.237')
