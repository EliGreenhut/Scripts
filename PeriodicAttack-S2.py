from fabric.api import env, run
from fabric.context_managers import settings
from fabric.decorators import parallel

env.hosts = ['10.20.4.237']  # Default remote host IP address. Overidden during deployment
env.user = 'root'  # Default VMs user name
env.password = 'radware'

def run_command():
    with settings(host_string=env.hosts[0]):
        run('python DP_SecurityAttacksSimulator.py --rate 20 --policy PO-S2-N-Atk1 --device 10.20.6.20 --dest 200.10.14.0 --attack 70 --duration 10')
        run('python DP_SecurityAttacksSimulator.py --rate 40 --policy PO-S2-N-Atk1 --device 10.20.6.20 --dest 200.10.14.0 --attack 71 --duration 5')
        run('python DP_SecurityAttacksSimulator.py --rate 80 --policy PO-S2-N-Atk1 --device 10.20.6.20 --dest 200.10.14.0 --attack 72 --duration 10')
        run('python DP_SecurityAttacksSimulator.py --rate 60 --policy PO-S2-N-Atk1 --device 10.20.6.20 --dest 200.10.14.0 --attack 73 --duration 5')

if __name__ == '__main__':
    run_command()