# scanner.py
import nmap

def scan_host(host):
    nm = nmap.PortScanner()
    nm.scan(host, '1-1024')
    results = []
    for host in nm.all_hosts():
        host_info = f"Scanning {host}"
        results.append(host_info)
        for proto in nm[host].all_protocols():
            proto_info = f"Protocol : {proto}"
            results.append(proto_info)
            ports = nm[host][proto].keys()
            for port in ports:
                port_state = f"Port : {port}\tState : {nm[host][proto][port]['state']}"
                results.append(port_state)
    return "\n".join(results)

if __name__ == "__main__":
    target = input("Enter IP or Host to scan: ")
    print(scan_host(target))

