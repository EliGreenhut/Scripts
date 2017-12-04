from fabric.api import env, run
from fabric.context_managers import settings
# from fabric.decorators import parallel
import time

# -----------------------------------------------------
#  Traffic directly on site
# -----------------------------------------------------
def traffic_site():
    with settings(host_string='10.20.4.238'):
        run('python DP_TrafficUtilizationSimulator.py --rate 25 --duration 10 --device 10.20.6.10 --policy PO-ST-S1-1', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 45 --duration 10 --device 10.20.6.10 --policy PO-ST-S1-1', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 65 --duration 10 --device 10.20.6.10 --policy PO-ST-S1-1', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 30 --duration 10 --device 10.20.6.10 --policy PO-ST-S1-1', pty=False)


# -----------------------------------------------------------------
# Traffic in two assets (non-MSA), in parallel, related to one site
# -----------------------------------------------------------------
def traffic_2assets():
    with settings(host_string='10.20.4.237'):
        run('python DP_TrafficUtilizationSimulator.py --rate 40 --duration 15 --device 10.20.6.20 --policy PO-S2-N-Traf1 >& /dev/null < /dev/null &', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 75 --duration 15 --device 10.20.6.20 --policy PO-S2-N-Traf2 >& /dev/null < /dev/null &', pty=False)


# -----------------------------------------------------
# Traffic in one asset (MSA) related to three sites
# -----------------------------------------------------
def traffic_msa_asset():
    with settings(host_string='10.20.4.238'):
        run('python DP_TrafficUtilizationSimulator.py --rate 25 --duration 10 --device 10.20.6.10 --policy PO-M1-Traffic1', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 45 --duration 10 --device 10.20.6.10 --policy PO-M1-Traffic1', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 65 --duration 10 --device 10.20.6.10 --policy PO-M1-Traffic1', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 30 --duration 10 --device 10.20.6.10 --policy PO-M1-Traffic1', pty=False)


# -----------------------------------------------------
# Attack on Network asset
# -----------------------------------------------------
def attack_nasset():
    with settings(host_string='10.20.4.237'):
        run('python DP_SecurityAttacksSimulator.py --rate 20 --policy PO-S2-N-Atk1 --device 10.20.6.20 --dest 200.10.14.0 --attack 70 --duration 10', pty=False)
        run('python DP_SecurityAttacksSimulator.py --rate 40 --policy PO-S2-N-Atk2 --device 10.20.6.20 --dest 200.10.15.0 --attack 71 --duration 5', pty=False)
        run('python DP_SecurityAttacksSimulator.py --rate 80 --policy PO-S2-N-Atk3 --device 10.20.6.20 --dest 200.10.16.0 --attack 72 --duration 5', pty=False)
        run('python DP_SecurityAttacksSimulator.py --rate 80 --policy PO-S2-N-Atk3 --device 10.20.6.20 --dest 200.10.16.0 --attack 73 --duration 5', pty=False)
        run('python DP_SecurityAttacksSimulator.py --rate 60 --policy PO-S2-N-Atk4 --device 10.20.6.20 --dest 200.10.17.0 --attack 74 --duration 5', pty=False)


# -----------------------------------------------------
# Traffic on Diverted asset (through SC)
# -----------------------------------------------------
def ingress_egress():
    with settings(host_string='10.20.4.228'):
        run('python /root/automation_japan/Simulators/NetflowSimulator.py --rate 30 --duration 20 --asset 111.1.6.0 --sdcc 10.20.4.132 --port 9996 >& /dev/null < /dev/null &', pty=False)
        run('python /root/automation_japan/Simulators/NetflowSimulator.py --rate 20 --duration 20 --asset 111.1.6.0 --sdcc 10.20.4.132 --port 9995 >& /dev/null < /dev/null &', pty=False)


if __name__ == '__main__':
    env.user = 'root'  # Default VMs user name
    env.password = 'radware'

    traffic_site()
    time.sleep(600)
    traffic_2assets()
    time.sleep(600)
    traffic_msa_asset()
    time.sleep(600)
    attack_nasset()
    time.sleep(600)

    env.user = 'root'  # Default user name for automation station
    env.password = 'securitydam'

    ingress_egress()
#   time.sleep(300)