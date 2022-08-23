from functools import total_ordering
from netaddr import *
import ipaddress
import pandas
from tabulate import tabulate



print("Enter your IP-subnet address in CIDR format : ")
str = input()
user = IPNetwork(str)

def ip_address(ip):
  '''returns ip-address of the user-input'''
  ip_addr = ip.ip
  return ip_addr

def subnet_mask(ip):
  '''returns the subnet-mask of the user-input'''
  mask=ip.netmask
  return mask

def broadcast(ip):
  '''returns the broadcast address of the user-input'''
  bca = ip.broadcast
  return bca

def network(ip):
  '''returns the broadcast address of the user-input'''
  nw = ip.network
  return nw

def hosts(str):
  '''returns available user_count'''
  lis = list(ipaddress.ip_network(str).hosts())
  total_count = len(lis)
  return total_count
  
user_ip=ip_address(user)

subnet = subnet_mask(user)

net_id = network(user)

broadcast_add = broadcast(user)

host_count = hosts(str)

data = {
    'Attribute':['IP-subnet', 'IP-address', 'subnet-mask', 'Network', 'Broadcast', 'Available hosts'],
    'Value':[str, user_ip, subnet, net_id, broadcast_add, host_count]
    }
df = pandas.DataFrame(data)
print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

