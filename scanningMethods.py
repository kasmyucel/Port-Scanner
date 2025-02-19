import socket
import os
import subprocess
import ipaddress

class Target:
    commonPorts = {
        20: "FTP (Data Transfer)", 21: "FTP (Command Control)", 22: "SSH", 23: "Telnet", 25: "SMTP",
        53: "DNS", 67: "DHCP (Server)", 68: "DHCP (Client)", 69: "TFTP", 80: "HTTP", 110: "POP3",
        119: "NNTP", 123: "NTP", 135: "Microsoft RPC", 137: "NetBIOS Name Service", 138: "NetBIOS Datagram Service",
        139: "NetBIOS Session Service", 143: "IMAP", 161: "SNMP", 162: "SNMP Trap", 179: "BGP", 194: "IRC",
        389: "LDAP", 443: "HTTPS", 445: "Microsoft SMB", 465: "SMTPS", 514: "Syslog", 587: "SMTP (Mail Submission)",
        636: "LDAPS", 873: "Rsync", 989: "FTPS (Data)", 990: "FTPS (Control)", 993: "IMAPS", 995: "POP3S",
        1080: "SOCKS Proxy", 1433: "MSSQL", 1521: "Oracle Database", 1723: "PPTP", 2049: "NFS",
        2181: "Apache Zookeeper", 3306: "MySQL", 3389: "RDP", 3690: "Subversion", 4369: "Erlang Port Mapper Daemon",
        5432: "PostgreSQL", 5900: "VNC", 5984: "CouchDB", 6379: "Redis", 6667: "IRC", 8000: "Common Web Services",
        8080: "HTTP Proxy", 8443: "HTTPS Alternative", 9200: "Elasticsearch", 11211: "Memcached", 27017: "MongoDB"
    }
    
    def __init__(self, targetIP):
        self.targetIP = str(targetIP)
    
    def isReachable(self):
        
        command = ['ping', '-c', '1', self.targetIP] if os.name != 'nt' else ['ping', '-n', '1', self.targetIP]
        with open(os.devnull, 'w') as devnull:
            result = subprocess.run(command, stdout=devnull, stderr=devnull)
        return result.returncode == 0  
    
    def scanPort(self, port):
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.2)
            result = sock.connect_ex((self.targetIP, port))
            if result == 0:
                banner = self.getBanner(sock)
                protocol = self.getProtocol(port)
                print(f"PORT {port:5} --> {protocol:25} STATE: OPEN     VERSION: {banner}")
    
    def getBanner(self, sock):
        try:
            sock.send(b'\n')
            return sock.recv(1024).decode().strip()
        except:
            return "UNKNOWN"
    
    @classmethod
    def getProtocol(cls, port):
        return cls.commonPorts.get(port, "UNKNOWN")
    
    def listIPaddresses(startIP, endIP):
        
        start = ipaddress.IPv4Address(startIP)
        end = ipaddress.IPv4Address(endIP)
        return [ipaddress.IPv4Address(ip) for ip in range(int(start), int(end) + 1)]  