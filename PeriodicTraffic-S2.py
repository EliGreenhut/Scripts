from fabric.api import env, run
from fabric.context_managers import settings

ssh = SSHExtensions('10.20.4.238', 'root', 'radware')
ssh.Send('python DP_TrafficUtilizationSimulator.py --rate 40 --duration 10 --device 10.20.6.20 --policy PO-S2-N-Traf1')

ssh = SSHExtensions('10.20.4.238', 'root', 'radware')
ssh.Send('python DP_TrafficUtilizationSimulator.py --rate 65 --duration 10 --device 10.20.6.20 --policy PO-S2-N-Traf2')


