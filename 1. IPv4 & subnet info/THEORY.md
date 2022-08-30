## Calculate the IP address subnet information(Network, broadcast, first IP, last IP) for class C subnets

#### Subnets can be conveniently referred as sub-networks of a network.

Each block in an IPv4 address is 8 bits. There are 4 blocks in an IPv4 address. Thus an IPv4 address is 32 bits(4 bytes) where each block is an octet.
Suppose IP address is 168.210.255.206, it's binary equivalent is 10101000.11010010.11100001.11001110
i.e. 168=128+32+8

Subnetting : IPv4 address -> about 4.2 billion IP addresses. Well today this number is too short for IPs across the internet. Thus developers introduced the conecpt of subnetting.
Subnetting uses the host section of the IP address to break it down into smaller networks or subnets.
Generally, an IP address is made up of network bits and host bits. It gives us a way to break up networks into subnets, and allows devices to determine whether another device/IP address is on the same local network or not.

```
IP address : 192.168.0.101
subnet mask : 255.255.255.0

- Whenever a bit in a binary subnet mask is 1, then the same bit in a binary IP address is part of the network, not the host.
- Since the octet 255 is 11111111 in binary, that whole octet in the IP address is part of the network. So the first three octets, 192.168.0, is the network portion of the IP address, and 101 is the host portion.
- In other words, if the device at 192.168.0.101 wants to communicate with another device, using the subnet mask it knows that anything with the IP address 192.168.0.xxx is on the same local network.

==> Thus the network ID of the address 192.168.0.101 with a subnet mask of 255.255.255.0 is 192.168.0.0
```

                                            CIDR Notation - Classless Inter-Domain Routing

```
192.168.0.101/24  is equivalent of 192.168.0.101 with subnet mask 255.255.255.0
```
To figure out CIDR notation, convert the subnet mask into binary equivalent and the no. of 1s in it gives the slash number.


                                              CLASSFUL ADDRESSING
                                          
```
Class A : Network.Host.Host.Host   
          -> IP address range : 1.0.0.0 to 127.255.255.255
          -> default subnet mask 255.0.0.0 (or /8 in CIDR)
          -> Networks =  2**7 = 128 ; Usable(host) addresses = (2**24 - 2) / network
          The range 127.0.0.0 to 127.255.255.255 within class A range is reserved for host loopback address.
```
```            
Class B : Network.Network.Host.Host  
          -> IP address range : 128.0.0.0 to 191.255.255.255
          -> default subnet mask 255.255.255.0 ( or /16 in CIDR)
          -> Networks = 2**14 = 16384 ; Usable(host) addresses =  (2**16 -2) / network 
```
```          
Class C : Network.Network.Network.Host    
          -> IP address range : 192.0.0.0 to 223.255.255.255 
          -> default subnet mask 255.255.255.0 ( or /24 in CIDR)
          -> Networks = 2**21 = 2,097,152  ; Usable(host) addresses =  (2**8 -2) / network                                     
```
```
Class D : 
          Reserved for multicasts. 
          -> IP address range : 224.0.0.0 to 239.255.255.255
```
```
Class E : 
          Experimental and anything over 240.0.0.0
```       
Classfull IP address haven't been used since they were replaced by CIDR in 1993.
<<<<<<< HEAD

'''

In short
```
Class A    0-127        network,node,node,node          Net.node.node.node         "8 bits used for the network"
Class B    128-191      network,network,node,node       Net.subnet.node.node      "16 bits used for the network"
Class C    192-223      network,network,network,node    Net.subnet.subnet.node    "24 bits used for the network"
```


```

## CREATING A SUBNET

* The technique used to create subnets is to use a mask.
* The mask effectively hides the Node component and leaves the network and sub network components.

NOTE :
* The network part of the IPv4 address is only used for routing IP packets on the public internet
* Once the packet enters the private network then the Node address is used and the public Network address is not used.
* Now a network administrator can interpret the node address any way they want, and so it is possible to split the node address into subnet and Node. So we could have
```
Net.Subnet.Node.Node or Net.Subnet.Subnet.Node.

```
IP : 11.1.1.21
Mask used for creating subnet : 255.255.255.0
```

NOTE THAT THE IP USED HERE IS A "CLASS A" IP ADDRESS.

```
000001011.00000001.00000001.00010101 = 11.1.1.21
11111111.11111111.11111111.00000000 = 255.255.255.0
```
<<<<<<< HEAD

### Questions
```
You have been allocated a class A network address of 21.0.0.0. You need create at least 10 networks and each network will support a maximum of 100 hosts. Would the following two subnet masks Work.

255.255.0.0 and or 255.255.255.0
```
Yes you only need 8 bits for 100 hosts and both subnet masks would give you that.
A subnet mask of 255.255.255.0 would give you lots of networks (2 16) and 254 hosts.
A subnet of 255.255.0.0 would give you lots of hosts (approx 216) and 256 networks.
=======
CIDR notation is the IP address/<no. of 1s in the mask>
>>>>>>> e4deb9eca46f2271101801fc45d41aab72a30c1b



Subnets simplified : http://www.steves-internet-guide.com/subnetting-subnet-masks-explained/
<<<<<<< HEAD
=======


>>>>>>> e4deb9eca46f2271101801fc45d41aab72a30c1b
