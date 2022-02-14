from sys import exit, platform
from ipaddress import ip_address, IPv4Address, IPv6Address
from asyncio import ProactorEventLoop, set_event_loop, run, gather, create_subprocess_shell, subprocess
from itertools import repeat


