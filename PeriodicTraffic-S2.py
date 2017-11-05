from fabric.api import env, run
from fabric.context_managers import settings
from fabric.decorators import parallel

#env.hosts = ['10.20.4.238']  # Default remote host IP address. Overidden during deployment
env.user = 'root'  # Default VMs user name
env.password = 'radware'

@parallel
def run_command(cmd, host):
    with settings(host_string=host):
        run(cmd)

if __name__ == '__main__':
    run_command('python DP_TrafficUtilizationSimulator.py --rate 40 --duration 10 --device 10.20.6.20 --policy PO-S2-N-Traf1', '10.20.4.237')
    run_command('python DP_TrafficUtilizationSimulator.py --rate 65 --duration 10 --device 10.20.6.20 --policy PO-S2-N-Traf2', '10.20.4.237')
