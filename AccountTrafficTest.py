from fabric.api import env, run
from fabric.context_managers import settings
# from fabric.decorators import parallel
import time

# -----------------------------------------------------
#  Traffic for 2:30 hours
# -----------------------------------------------------
def traffic_all():
    with settings(host_string='10.20.4.237'):
# 1.1
        run('python DP_TrafficUtilizationSimulator.py --rate 20 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1-AS1', pty=False)
# 1.2
        run('python DP_TrafficUtilizationSimulator.py --rate 40 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1-AS2', pty=False)
# 1.3
        run('python DP_TrafficUtilizationSimulator.py --rate 60 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1-AS3', pty=False)
# S2
        run('python DP_TrafficUtilizationSimulator.py --rate 30 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST2', pty=False)
# 1.1+1.2+1.3
        run('python DP_TrafficUtilizationSimulator.py --rate 20 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1-AS1 >& /dev/null < /dev/null &', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 40 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1-AS2 >& /dev/null < /dev/null &', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 60 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1-AS3 >& /dev/null < /dev/null &', pty=False)
# S1+S3
        run('python DP_TrafficUtilizationSimulator.py --rate 30 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1 >& /dev/null < /dev/null &', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 90 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST3 >& /dev/null < /dev/null &', pty=False)
# 1.1+1.2+1.3+3.1
        run('python DP_TrafficUtilizationSimulator.py --rate 20 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1-AS1 >& /dev/null < /dev/null &', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 40 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1-AS2 >& /dev/null < /dev/null &', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 60 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1-AS3 >& /dev/null < /dev/null &', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 80 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST3-AS1 >& /dev/null < /dev/null &', pty=False)
# S1
        run('python DP_TrafficUtilizationSimulator.py --rate 30 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1', pty=False)
# 1.1+3.1
        run('python DP_TrafficUtilizationSimulator.py --rate 20 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1-AS1 >& /dev/null < /dev/null &', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 80 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST3-AS1 >& /dev/null < /dev/null &', pty=False)
# S1+1.3+S2+3.1
        run('python DP_TrafficUtilizationSimulator.py --rate 30 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1 >& /dev/null < /dev/null &', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 20 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST1-AS1 >& /dev/null < /dev/null &', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 60 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST2 >& /dev/null < /dev/null &', pty=False)
        run('python DP_TrafficUtilizationSimulator.py --rate 80 --duration 15 --device 10.20.6.20 --policy PO-AC1-ST3-AS1 >& /dev/null < /dev/null &', pty=False)

if __name__ == '__main__':
    env.user = 'root'  # Default VMs user name
    env.password = 'radware'

    traffic_all()
    time.sleep(900)

#    env.user = 'root'  # Default user name for automation station
#    env.password = 'securitydam'
