import nmap
ns = nmap.PortScanner()
print(ns.nmap_version()) # checks version
ns.scan('192.168.146.1','1-1024','-v') #scanning ports
print(ns.scaninfo())
print(ns.csv())
print(ns.all_hosts())

#get state of the server
print(ns['192.168.146.1'].state())

#find protocols running on the server
#print(ns['192.168.146.1'].allprotocols())

#find ports
print(ns['192.168.146.1']['tcp'].keys())

print(ns['192.168.146.1'].has_tcp(80)) #check if the port exists