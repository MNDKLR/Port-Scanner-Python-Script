########################### Modules ###########################
import os
import sys
import argparse
import socket
import logging
from datetime import datetime
########################### Splash & Usage Guide ###########################
def start_banner():
    print(""" \n
         :::::::::   ::::::::  ::::::::: :::::::::::           ::::::::   ::::::::      :::     ::::    ::: ::::    ::: :::::::::: ::::::::: 
        :+:    :+: :+:    :+: :+:    :+:    :+:              :+:    :+: :+:    :+:   :+: :+:   :+:+:   :+: :+:+:   :+: :+:        :+:    :+: 
       +:+    +:+ +:+    +:+ +:+    +:+    +:+              +:+        +:+         +:+   +:+  :+:+:+  +:+ :+:+:+  +:+ +:+        +:+    +:+  
      +#++:++#+  +#+    +:+ +#++:++#:     +#+              +#++:++#++ +#+        +#++:++#++: +#+ +:+ +#+ +#+ +:+ +#+ +#++:++#   +#++:++#:    
     +#+        +#+    +#+ +#+    +#+    +#+                     +#+ +#+        +#+     +#+ +#+  +#+#+# +#+  +#+#+# +#+        +#+    +#+   
    #+#        #+#    #+# #+#    #+#    #+#              #+#    #+# #+#    #+# #+#     #+# #+#   #+#+# #+#   #+#+# #+#        #+#      #+#   
   ###         ########  ###    ###    ###               ########   ########  ###     ### ###    #### ###    #### ########## ###        ###  
  ### :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ###
 ### :::::::::::::::::::::::::::::::::::::::::::::::::::: By Taylor McManiman ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ###
### :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ### \n
User Guide / Description:                         
======================================================================== 
A Basic Port Scanner & Network Reconnaissance tool Written 
In Python.
========================================================================
(1 Required): [-H] { Target Host} OR  [-T] {Input File Containing Hosts}
(2 Required): [-S] { Start Port } AND [-E] {End Port}
(3 Optional): [-L] {Output LogFile}""") 
pass
########################### Arguments Parsing ###########################
def parse_arguments():
    parser = argparse.ArgumentParser(description="Subnet Port Scanner By TM")
    parser.add_argument("-H", "--host", help="target host to scan.")
    parser.add_argument("-T", "--target_file", help="target file to scan for hosts.")
    parser.add_argument("-S", "--start_port", type=int, help="start port of the range.")
    parser.add_argument("-E", "--end_port", type=int, help="end port of the range.")
    parser.add_argument("-L", "--logfile", help="output logfile.")
    return parser.parse_args()
########################### Reading from file ###########################
def read_file(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]
    ########################### Logging to file ###########################
def print_and_log(message):
    print(message)
    if args.logfile:
        logging.info(message)
########################### IP Scanning ###########################
def scan_host(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
            scan.settimeout(5)
            try:
                scan.connect((host, port))
                open_ports.append(port)
                success_message = f"Host: {host}  Port: {port}  Status: [OPEN] "
                print_and_log(success_message)
            except Exception as e:
                failiure_message = f"Host: {host}  Port: {port}  Status: [CLOSED] "
                print_and_log(failiure_message)
    return open_ports
########################### Main ###########################

args = parse_arguments()
os.system('cls')
start_banner()
time_start = datetime.now()
print("========================================================================")
if not args.host and not args.target_file: 
    print("============================== ERROR: ==================================")
    print("  Either -H or -T argument must be provided  ")
    print("========================================================================")
    print("\n")
    sys.exit(1)

target_hosts = []
if args.host and not args.target_file:
    target_hosts = [args.host]

if args.target_file and not args.host:
    target_hosts = read_file(args.target_file)

if args.logfile:
    logging.basicConfig(filename=args.logfile, level=logging.INFO, format='%(message)s')
    log = logging.getLogger()
scan_summary = {}

try: 
    for host in target_hosts:
        open_ports = scan_host(host, args.start_port, args.end_port)
        scan_summary[host] = open_ports
except KeyboardInterrupt:
    print("Program Interrupted By User")

print("============================ SCAN RESULTS: ============================")
time_end = datetime.now()
runtime = time_end - time_start
for host, ports in scan_summary.items():
    if ports:
        print("Host: {} Open Ports: [{}]".format(host, ", ".join(map(str, ports))))
    else:
        print("Host: {} Open Ports: [NONE]".format(host))
print("Scan Duration: [{}] ".format(runtime))
print("========================================================================")
print("\n")