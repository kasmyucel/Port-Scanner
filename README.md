# 📌 **netScanner**  
This project is one of my introductory projects in cybersecurity during my first year as a computer engineering student. It performs a basic scan of all TCP/IP ports within a given range and outputs whether they are open, along with their port number, protocol, and version.  
## **Installation 🛠️**  
Clone the repository and navigate to the project directory:  

```sh
git clone https://github.com/kasmyucel/Port-Scanner.git
```

## **How to Use It ?**  
Navigate to the directory where you downloaded the files, then run the following command:  

#### **Usage:**  
```sh
python3 netscan.py <start_ip> <end_ip> [--sS <scanning_speed>]
```
#### **Example Commands:**
```sh
python3 netscan.py 192.168.1.1 192.168.1.255
python3 netscan.py 192.168.1.1 192.168.1.255 --sS 3
```
#### **Example Output:**
![NetScan Output](output.png)

## **Planned Improvements 🔧**  
My primary focus will be on performance optimization, as I have noticed occasional delays. Additionally, the version control mechanism could be made more stable, as it sometimes fails to respond. 
##### Contribution 🤝
If you have any other advice or questions, I am always open to this kind of feedback. Please feel free to share with me. As I mentioned at the beginning I am still on my learning path.

## Licence 📜
This project is licensed under the [MIT](LICENSE) license.
