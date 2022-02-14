from ipaddress import ip_address
from task_1 import AsyncPingHosts

def host_range_ping():
    from_addr = ip_address(input('Введите начальный ip или имя хоста: '))
    to_addr = ip_address(input('Введите конечный ip или имя хоста: '))

    addresses = [from_addr + i for i in range(int(to_addr) - int(from_addr) + 1)]

    ping = AsyncPingHosts(addresses)
    ping.host_ping()

    return ping.get_ping_status_table()


if __name__ == '__main__':
    host_range_ping()

