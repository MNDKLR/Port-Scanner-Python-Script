########################### Modules ###########################
import os
import sys
import argparse
import socket
import logging
import threading
from   datetime  import datetime
####################### Splash & Usage Guide ######################
def start_banner():
    print_and_log("""
         :::::::::   ::::::::  ::::::::: :::::::::::           ::::::::   ::::::::      :::     ::::    ::: ::::    ::: :::::::::: ::::::::: 
        :+:    :+: :+:    :+: :+:    :+:    :+:              :+:    :+: :+:    :+:   :+: :+:   :+:+:   :+: :+:+:   :+: :+:        :+:    :+: 
       +:+    +:+ +:+    +:+ +:+    +:+    +:+              +:+        +:+         +:+   +:+  :+:+:+  +:+ :+:+:+  +:+ +:+        +:+    +:+  
      +#++:++#+  +#+    +:+ +#++:++#:     +#+              +#++:++#++ +#+        +#++:++#++: +#+ +:+ +#+ +#+ +:+ +#+ +#++:++#   +#++:++#:    
     +#+        +#+    +#+ +#+    +#+    +#+                     +#+ +#+        +#+     +#+ +#+  +#+#+# +#+  +#+#+# +#+        +#+    +#+   
    #+#        #+#    #+# #+#    #+#    #+#              #+#    #+# #+#    #+# #+#     #+# #+#   #+#+# #+#   #+#+# #+#        #+#      #+#   
   ###         ########  ###    ###    ###               ########   ########  ###     ### ###    #### ###    #### ########## ###        ###  
  ### :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ###
 ### :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: By Taylor McManiman ::::::::::::::::::::::::::::::::::::::::::::::::::: ###
### :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ###\n
User Guide / Description:                         
========================================================================= 
A Basic Port Scanner & Network Reconnaissance tool Written 
In Python.
=========================================================================
(1 Required): [-H] {Target Host} OR  [-T] {Input File Containing Hosts}
(2 Required): [-S] {Start Port}  AND [-E] {End Port}
(3 Optional): [-L] {LogFile}""") 
pass
######################## Arguments Parsing ########################
def parse_arguments():
    parser = argparse.ArgumentParser(description="Subnet Port Scanner By TM")
    parser.add_argument("-H", "--host", help="target host to scan.")
    parser.add_argument("-T", "--target_file", help="target file to scan for hosts.")
    parser.add_argument("-S", "--start_port", type=int, help="start port of the range.")
    parser.add_argument("-E", "--end_port", type=int, help="end port of the range.")
    parser.add_argument("-L", "--logfile", help="output logfile.")
    return parser.parse_args()
######################## Reading from file ########################
def read_file(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]
######################### Logging to file #########################
def print_and_log(message):
    print(message)
    if args.logfile:
        logging.info(message)
########################### IP Scanning ###########################
def scan_host(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
        scan.settimeout(5)
        try:
            scan.connect((host, port))
            success_message = f"Host: {host}   Port: {port}  Status: [OPEN]"
            print_and_log(success_message) 
            with thread_lock:
                scan_summary[host].append(port)
        except Exception as e:
            failiure_message = f"Host: {host}  Port: {port}  Status: [CLOSED]"
            print_and_log(failiure_message)
############################### Main ###############################
args = parse_arguments()
os.system('cls')
start_banner()

threads = [] 

if not args.host and not args.target_file: 
    print("============================== ERROR: ===================================")
    print("  Either -H or -T argument must be provided  ")
    print("=========================================================================")
    print("\n")
    sys.exit(1)

target_hosts = []

if args.host:
    target_hosts = [args.host]
    time_start = datetime.now()
    print_and_log("============================= SCANNING... ===============================")

elif args.target_file:
    target_hosts = read_file(args.target_file)
    time_start = datetime.now()
    print_and_log("============================= SCANNING... ===============================")

if args.logfile:
    logging.basicConfig(filename=args.logfile, level=logging.INFO, format='%(message)s')
    log = logging.getLogger()

thread_lock = threading.Lock()  
scan_summary = {host: [] for host in target_hosts}  

try: 
    for host in target_hosts:
        for port in range(args.start_port, args.end_port + 1):  
            t = threading.Thread(target=scan_host, args=(host, port))  
            t.start()
            threads.append(t)
except KeyboardInterrupt:
    print("Program Interrupted By User")
for t in threads:
    t.join()

print_and_log("=============================== SUMMARY: ================================")
for host, ports in scan_summary.items():
    if ports:
        print_and_log("Host: {} Open Ports: [{}]".format(host, ", ".join(map(str, ports))))
        print_and_log("=========================================================================")
    else:
        print_and_log("Host: {} Open Ports: [NONE]".format(host))
        print_and_log("=========================================================================")

time_end = datetime.now()
runtime = time_end - time_start
print_and_log("Scan Began: [{}]".format(time_start))
print_and_log("Scan Ended: [{}] ".format(time_end))
print_and_log("Runtime:    [{}] ".format(runtime))
print_and_log("=========================================================================")
print_and_log("\n")
