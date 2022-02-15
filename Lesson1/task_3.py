from task_2 import host_range_ping
from tabulate import tabulate

def host_range_ping_tab():
    headers = ['Address', 'Status']
    # 10.0.0.1
    print(tabulate(host_range_ping(), headers, tablefmt="grid"))


    print(host_range_ping())

if __name__ == '__main__':
    host_range_ping_tab()
