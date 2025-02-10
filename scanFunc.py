import threading
import concurrent.futures
from scanningMethods import NetworkScanner

def scanning(initialIP, finalIP, scanningSpeed):
    
    ipList = NetworkScanner.listIPaddresses(initialIP, finalIP)

    
    match scanningSpeed:
        case 1:
            maxWorkers = 100  # slow scanning
        case 2:
            maxWorkers = 500  # normal scanning
        case 3:
            maxWorkers = 1000  # quick scanning
        case _:
            maxWorkers = 500  # default 

    
    with concurrent.futures.ThreadPoolExecutor(max_workers=maxWorkers) as executor:
        for ip in ipList:
            target = NetworkScanner(ip)
            if target.isReachable():
                print(f"HOST: {ip}")

                
                with concurrent.futures.ThreadPoolExecutor(max_workers=200) as port_executor:
                    port_futures = {port_executor.submit(target.scanPort, port): port for port in range(0, 65536)}

                    for port_future in concurrent.futures.as_completed(port_futures):
                        try:
                            port_future.result()
                        except Exception as e:
                            print(f"Error scanning port {port_futures[port_future]} on {ip}: {e}")

                print("------------------------------------------------------------------------------------\n")

    print("Scanning process is completed.")
