import socket

import ifaddr as ifaddr

adapters = ifaddr.get_adapters()
for adapter in adapters:
    print('--------------------------------------------------')
    print(f'adapter: [{adapter.nice_name}]')
    for ip in adapter.ips:
        print(f'ip:[{ip.ip}] prefix[{ip.network_prefix}]')
print('*****************************')
# a = socket.getaddrinfo(socket.gethostname(), None)
# for b in a:
#     print(b[4][0])
#     print(b[0] == socket.AddressFamily.AF_INET)

a = [address_info[4][0] for address_info in socket.getaddrinfo(socket.gethostname(), None) if address_info[0] == socket.AddressFamily.AF_INET]
print(a)