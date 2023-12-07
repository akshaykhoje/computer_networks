# iwconfig

iwconfig command in Linux is like ifconfig command, in the sense it works with kernel-resident network interface but it is dedicated to wireless networking interfaces only. It is used to set the parameters of the network interface that are particular to the wireless operation like SSID, frequency etc. iwconfig may also be used to display the parameters, and the wireless statistics which are extracted from /proc/net/wireless.



# arp

On Linux operating systems, the arp command manipulates or displays the kernel's IPv4 network neighbour cache. It can add entries to the table, delete one, or display the current content.

ARP stands for Address Resolution Protocol, which is used to find the address of a network neighbor for a given IPv4 address.

arp with no mode specifier prints the current content of the table. It is possible to limit the number of entries printed, by specifying a hardware address type, interface name or host address.

arp -d address deletes an ARP table entry. Root privilege is required to do this. The entry is found by IP address. If a hostname is given, it will be resolved before looking up the entry in the ARP table.

# ip

The ip command in linux is useful for sytem administrators and is a powerful tool for configuring network interfaces that any linux administrator should know. 
It is used to bring interfaces up or down, assign and remove addresses and routes, manage ARP cache, and much more.

ip command is seen replacing the ifconfig command and comes pre-installed in modern Linux distros.

Syntax : 
ip [ OPTIONS ] OBJECT { COMMAND | help }

COMMANDS:

1) Display information about all IP addresses :
ip addr show 
ip address
ip addr

2) Assign IP address to an interface :
ip addr add ADDRESS dev IFNAME
e.g.
sudo ip address add 192.168.121.45/24 dev enp2s0 

3) Assign multiple IP addresses to the same interface :
sudo ip address add 192.168.121.241/24 dev eth0
sudo ip address add 192.168.121.45/24 dev eth0

4) Display information about network interfaces :
ip link show 
# Unlike 'ip addr show', 'ip link show' this will not print info about the IP addresses associated with the device.

5) Alter the status of the interface UP/DOWN:
ip link set dev {DEVICE} {up|down}

6) Displaying and altering the routing table 
''' 
All network devices, whether they are hosts, routers, or other types of network nodes such as network attached printers, need to make decisions about where to route TCP/IP data packets. The routing table provides the configuration information required to make those decisions.
'''
ip route
ip route list
ip route list SELECTOR

7) Add a new route:
ip route add 192.168.121.0/24 via 192.168.121.1
ip route add 192.168.121.0/24 dev <IFNAME>
ip route add default via 192.168.121.1 dev eth0  // adds the default route

8) Delete a route:
'''
To delete an entry from the routing table, use the route add command. The syntax for deleting a route is the same as when adding.
'''
ip route del <route>


# nslookup

On Unix-like operating systems, the nslookup command queries Internet name servers interactively for information.

nslookup, which stands for "name server lookup", finds information about a named domain.

By default, nslookup translates a domain name to an IP address (or vice versa). For instance, to find the IP address of google.com, you could run the command:

# mail

Linux by default provides the feature of sending an email using the “mail” command through its terminal. We can write the subject, message along with the email address of the recipient and send it by just executing a single command. 



# tracepath

tracepath command in Linux is used to traces path to destination discovering MTU along this path.
''' 
MTU stands for Maximum Transmission Unit : it is the maximum size of the packet that can be transmitted from a network interface. All the devices including servers and switches/routers involved in communication should have the same MTU size.
'''

tracepath is similar to traceroute, but it does not require sudo privileges.

SYNTAX:
tracepath <IP Address | website>

FLAGS:
1)  Print IP addresses numerically:
tracepath -n <IP Address | website>

2) Both of host names and IP addresses:
tracepath -b <IP Address | website>

3) Set the initial destination port to use:
tracepath -p 8080 <IP Address | website>


# ifplugstatus

ifplugstatus - A link beat detection tool

This command tells us whether a cable is plugged into our network interface or not.


# traceroute

Traceroute is a tool in Linux that allows you to investigate the routes of network packets. It can help you in identifying the limiting factor of network packet journeys. Traceroute is also useful for troubleshooting sluggish network connections.

Q.) HOW IT WORKS?
  Traceroute works by sending packets of data to the target computer, server or website and recording any intermediate steps through which the packets travel.

OUTPUT of a traceroute command will be the IP addresses and domain names through which the packets pass.

NOTE:
  While using traceroute, some devices may not interact well. This could be due to routers being bugged, ISPs rate-limiting ICMP messages, devices configured not to send ICMP packets (to prevent distributed DoS attacks), etc. Some networks are also configured to block traceroute requests.

SYNTAX:
traceroute {<website> | <IP address>}

Use IPv6
traceroute -6 {<website> | <IP address>}

1) TESTING PORTS:
If there is a need to test a specific port, the port can be specified using the “-p” flag. For UDP tracing, traceroute will start with the given value and increase with each probe. For ICMP tracing, the value will determine the initial ICMP sequence value. For TCP and others, this will be the constant destination port to connect.

traceroute -p <port> <IP address>
traceroute -p 80 192.168.0.1

2) TIMEOUT LIMIT:
traceroute -w 6.0 linuxhint.com    ; a timeout of 6 seconds

3) Use TCP SYN for probing:
sudo traceroute -T <IP address | website>

4) Routing packets through a gateway:
traceroute -I -g 192.168.0.1 <IP address | website>

# host

On Unix-like operating systems, the host command is a DNS lookup utility, finding the IP address of a domain name. It also performs reverse lookups, finding the domain name associated with an IP address.

host performs DNS lookups, converting domain names to IP addresses and vice versa. When no arguments or options are given, host prints a summary of its command line arguments and options.

host <url>

# netstat

NETSTAT - derived from NETwork and STATistics.

Netstat is a command-line tool used by system administrators to evaluate network configuration and activity.

It shows open ports on the host device and their corresponding addresses, the routing table, and masquerade connections.

1) Display routing table:
netstat -nr 

2) Display interface statistics
netstat -i 
netstat -ai      // Display all of the kernel interfaces

3) Display network connection:
'''
To view active or passive sockets, Netstat has a range of options. Active TCP, UDP, RAW, and Unix socket connections are specified by the –t, –u, –w, and –x options, respectively.
'''
netstat -ta 

4) Display Network services:
'''
Run the following command to see a list of networks, their current states, and their associated ports.
'''
netstat -pnltu

5) Display all TCP listening ports:
netstat -lt

6) Display all UDP listening ports:
netstat -lu 

7) Display all UNIX listening ports:
netstat -lx 

8) Show statistics:
netstat -s 

# curl

curl is a command-line utility for transferring data from or to a server designed to work without user interaction. With curl, you can download or upload data using one of the supported protocols including HTTP, HTTPS, SCP, SFTP, IMAP, POP3 and FTP . curl provides a number of options allowing you to resume transfers, limit the bandwidth, proxy support, user authentication, and much more.

If no protocol is specified, curl tries to guess the protocol you want to use, and it will default to HTTP.

Download multiple files
curl -O <url>

Check if a website uses HTTP/2
curl -I --http2 -s https://linuxize.com/ | grep HTTP


# wget

GNU Wget is a command-line utility for downloading files from the web. With Wget, you can download files using HTTP, HTTPS, and FTP protocols. Wget provides a number of options allowing you to download multiple files, resume downloads, limit the bandwidth, recursive downloads, download in the background, mirror a website, and much more.

During the download, wget shows the progress bar alongside the file name, file size, download speed, and the estimated time to complete the download. Once the download is complete, you can find the downloaded file in your current working directory .


# ping

ping command is used for troubleshooting, testing and diagnosing network connectivity issues. 

It works by sending one or more ICMP(Internet Control Message Protocol) Echo Request packages to a specified destination IP on the network and waits for a reply. When the destination receives the package, it responds with an ICMP echo reply. You can also find the round-trip delay in communicating with the destination and check whether there is a packet loss.

A remote destination's upstate/downstate can be determined using ping command WHEN NOT BEHIND A PROXY. It is so because, 'ping' needs a direct network connection on the IP level to do this work. A proxy works on a higher layer of the TCP/IP network model, where there is no direct access to the IP protocol. This can be changed though with certain firewall settings or 'httping' command can be used as an alternative.

USE:
ping <website>

1) Specify the #pings 
ping -c [number] <website>

2) Use IPv4 address:
ping -4 DESTINATION
ping4 DESTINATION

3) Use IPv6 address:
ping -6 DESTINATION
ping6 DESTINATION


# route

On Unix-like operating systems, the route command displays or modifies the IP routing table.

In computer networking, a router is a device responsible for forwarding network traffic. When datagrams arrive at a router, the router must determine the best way to route them to their destination.

On Linux, BSD, and other Unix-like systems, the route command is used to view and make changes to the kernel routing table. The command syntax is different on different systems; here, with specific command syntax, we'll be discussing the Linux version.

# ifconfig

ifconfig stands for "interface configuration." It is used to view and change the configuration of the network interfaces on your system.

Syntax:
ifconfig [-a] [-v] [-s] <interface> [[<AF>] <address>]

It displays the information about all network interfaces currently in operation.
Here, enp2s0, lo and wlp3s0 are the active network interfaces.

enp2s0 -> It is the first ethernet interface. Additional ethernet interfaces would be named enp2s1, enp2s2, etc.
lo     -> It is the loopback interface. This is a special network interface that the system uses to communicate with itself.
wlp3s0 -> It is the name of the first wireless network on the system. Additional wireless interfaces would be named wlp3s1, wlp3s2, etc.

COMMANDS:

1) ifconfig -a 
This produces output similar to running ifconfig, but if there are any inactive interfaces on the system, their configuration is also shown.

2) Enabling and disabling an interface
sudo ifconfig enp2s0 up   (activate)
sudo ifconfig enp2s0 down (deactivate)

3) Configure an interface
'''Assign a static IP address to an interface'''
sudo ifconfig [interface] [IP]
e.g.
sudo ifconfig wlp3s0 69.72.169.1

4) Assign a network mask to an interface 
sudo ifconfig [interface] netmask [mask]
e.g. 
sudo ifconfig enp2s0 netmask 255.255.255.0

5) Assign a broadcast address to an interface 
sudo ifconfig [interface] broadcast [address]
e.g. 
sudo ifconfig enp2s0 broadcast 172.16.25.98

6) Combine the above commands into one :
sudo ifconfig enp2s0 192.168.2.5 netmask 255.255.255.0 broadcast 192.168.2.7


ifconfig is used to configure the system's kernel-resident network interfaces. It is used at boot time to set up interfaces as necessary. After that, it is usually only needed when debugging, or when system tuning is needed.

--------------------------------------------------
NOTE : 
ifconfig can only assign a static IP address to a network interface. If you want to assign a dynamic IP address using DHCP, use the dhclient command.
---------------------------------------------------

REFERENCES :
- https://www.reddit.com/r/linuxquestions/comments/rvj03f/whats_wlp3s0_and_why_isnt_it_wlan0_anymore/

- https://en.wikipedia.org/wiki/Consistent_Network_Device_Naming

# whois

A whois lookup will tell you a lot of information about who owns an internet domain.
The whois system is a listing of records that contains details about both the ownership of domains and the owners. The Internet Corporation for Assigned Names and Numbers (ICANN) regulates domain name registration and ownership, but the list of records is held by many companies, known as registries.
Anyone can query the list of records. When you do, one of the registries will handle your request and send you details from the appropriate whois record.


Registry: A company that manages a list containing a set of domain names (there are many of these).
Registrant: The legal owner of the domain; it’s registered to this person.
Registrar: A registrant uses a registrar to make his or her registration.

A whois record contains all the contact information associated with the person, company, or other entity that registered the domain name. Some registrations contain more information than others, and some registries return differing amounts of information.

A typical whois record will contain the following information:

    The name and contact information of the registrant: The owner of the domain.
    The name and contact information of the registrar: The organization that registered the domain name.
    The registration date.
    When the information was last updated.
    The expiration date.



# nload

nload is a console application which monitors network traffic and  bandwidth  usage in real time. It visualizes the in- and outgoing traffic using two graphs and provides additional info like the total amount of transferred data and min/max network usage.

When running nload, you can switch between the devices (which you gave nload either on the command line or which were auto-detected) by pressing the left and right ar‐ row  keys. If the -m command line parameter is given, the arrow keys switch as many devices back and forth as there are shown on the screen. If you want to quit, do so by pressing 'q' or 'Ctrl+C'.


# dig

On Unix-like operating systems, the dig command performs network DNS lookups.

dig (which stands for domain information groper) is a flexible tool for interrogating DNS name servers. It performs DNS lookups and displays the answers that are returned from the name server(s) that were queried. Most DNS administrators use dig to troubleshoot DNS problems because of its flexibility, ease of use and clarity of output. Other lookup tools tend to have less functionality than dig.

Although dig is normally used with command-line arguments, it also has a batch mode of operation for reading lookup requests from a file. A summary of its command-line arguments and options is printed when the -h option is given. Unlike earlier versions, the BIND 9 implementation of dig allows multiple lookups to be issued from the command line.

  

# telnet

In Linux, the telnet command is used to establish the connections between different machines.This command allows us to manage the remote devices using the CLI (command-line interface).  It uses TCP port 23 which is assigned to the telnet protocol.


