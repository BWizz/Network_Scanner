# Example on how to extract info from each IP
import nmap
def enter_ip_address():
    text = input("Please Enter IP Address: \n")  # Python 3
    return text


def enter_port_range():
    text = input("Please Enter Port Number or Range: \n")  # Python 3
    return text


# Prompt User to Enter Inputs From Command Line
ip_address = enter_ip_address()
ports = enter_port_range()
nm = nmap.PortScanner()
nm.scan(ip_address,ports)
for host in nm.all_hosts():
     print('----------------------------------------------------')
     print('Host : %s (%s)' % (host, nm[host].hostname()))
     print('State : %s' % nm[host].state())
     for proto in nm[host].all_protocols():
         print('----------')
         print('Protocol : %s' % proto)
         lport = nm[host][proto].keys()
         print(lport)

         for port in lport:
             print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))