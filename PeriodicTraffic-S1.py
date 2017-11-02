from fabric.api import env, run
from fabric.context_managers import settings

env.hosts = ['10.20.4.238']  # Default remote host IP address. Overidden during deployment
env.user = 'root'  # Default VMs user name
env.password = 'radware'

def run_update():
    with settings(host_string=env.hosts[0]):
        run('python DP_TrafficUtilizationSimulator.py --rate 50 --duration 5 --device 10.20.6.10 --policy PO-ST-S1-1')
        run('python DP_TrafficUtilizationSimulator.py --rate 70 --duration 5 --device 10.20.6.10 --policy PO-ST-S1-1')
        run('python DP_TrafficUtilizationSimulator.py --rate 90 --duration 5 --device 10.20.6.10 --policy PO-ST-S1-1')
        run('python DP_TrafficUtilizationSimulator.py --rate 30 --duration 5 --device 10.20.6.10 --policy PO-ST-S1-1')

if __name__ == '__main__':
    run_update()