import threading
import concurrent.futures
from scanningMethods import Target

def scanning(initialIP, finalIP, scanningSpeed):
    
    ipList = Target.listIPaddresses(initialIP, finalIP)

    
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
            currentTarget = Target(ip)
            if currentTarget.isReachable():
                print(f"HOST: {ip}")

                
                with concurrent.futures.ThreadPoolExecutor(max_workers=maxWorkers) as port_executor:
                    port_futures = {port_executor.submit(currentTarget.scanPort, port): port for port in range(0, 65536)}

                    for port_future in concurrent.futures.as_completed(port_futures):
                        try:
                            port_future.result()
                        except Exception as e:
                            print(f"Error scanning port {port_futures[port_future]} on {ip}: {e}")

                print("------------------------------------------------------------------------------------\n")

    print("Scanning process is completed.")
