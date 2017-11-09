from fabric.api import env, run
from fabric.context_managers import settings
# from fabric.decorators import parallel
import time

env.user = 'root'  # Default VMs user name
env.password = 'radware'

# -----------------------------------------------------
#  Traffic directly on site
# -----------------------------------------------------
def run_command():
    with settings(host_string='10.20.4.238'):
        run('python DP_TrafficUtilizationSimulator.py --rate 25 --duration 10 --device 10.20.6.10 --policy PO-ST-S1-1')
        run('python DP_TrafficUtilizationSimulator.py --rate 45 --duration 10 --device 10.20.6.10 --policy PO-ST-S1-1')
        run('python DP_TrafficUtilizationSimulator.py --rate 65 --duration 10 --device 10.20.6.10 --policy PO-ST-S1-1')
        run('python DP_TrafficUtilizationSimulator.py --rate 30 --duration 10 --device 10.20.6.10 --policy PO-ST-S1-1')

if __name__ == '__main__':
    run_command()

time.sleep (900)
# -----------------------------------------------------------------
# Traffic in two assets (non-MSA), in parallel, related to one site
# -----------------------------------------------------------------
def run_command(cmd):
    with settings(host_string='10.20.4.237'):
        run(cmd, pty=False)

if __name__ == '__main__':
    run_command(
        'python DP_TrafficUtilizationSimulator.py --rate 40 --duration 15 --device 10.20.6.20 --policy PO-S2-N-Traf1 >& /dev/null < /dev/null &')
    run_command(
        'python DP_TrafficUtilizationSimulator.py --rate 75 --duration 15 --device 10.20.6.20 --policy PO-S2-N-Traf2 >& /dev/null < /dev/null &')

time.sleep (900)
# -----------------------------------------------------
# Traffic in one asset (MSA) related to three sites
# -----------------------------------------------------
def run_command():
    with settings(host_string='10.20.4.238'):
        run(
            'python DP_TrafficUtilizationSimulator.py --rate 25 --duration 10 --device 10.20.6.10 --policy PO-M1-Traffic1')
        run(
            'python DP_TrafficUtilizationSimulator.py --rate 45 --duration 10 --device 10.20.6.10 --policy PO-M1-Traffic1')
        run(
            'python DP_TrafficUtilizationSimulator.py --rate 65 --duration 10 --device 10.20.6.10 --policy PO-M1-Traffic1')
        run(
            'python DP_TrafficUtilizationSimulator.py --rate 30 --duration 10 --device 10.20.6.10 --policy PO-M1-Traffic1')

if __name__ == '__main__':
    run_command()

time.sleep (1200)
# -----------------------------------------------------
# Attack on Network asset
# -----------------------------------------------------
def run_command():
    with settings(host_string='10.20.4.237'):
        run(
            'python DP_SecurityAttacksSimulator.py --rate 20 --policy PO-S2-N-Atk1 --device 10.20.6.20 --dest 200.10.14.0 --attack 70 --duration 10')
        run(
            'python DP_SecurityAttacksSimulator.py --rate 40 --policy PO-S2-N-Atk1 --device 10.20.6.20 --dest 200.10.14.0 --attack 71 --duration 5')
        run(
            'python DP_SecurityAttacksSimulator.py --rate 80 --policy PO-S2-N-Atk1 --device 10.20.6.20 --dest 200.10.14.0 --attack 72 --duration 10')
        run(
            'python DP_SecurityAttacksSimulator.py --rate 60 --policy PO-S2-N-Atk1 --device 10.20.6.20 --dest 200.10.14.0 --attack 73 --duration 5')


if __name__ == '__main__':
    run_command()

time.sleep(3600)
