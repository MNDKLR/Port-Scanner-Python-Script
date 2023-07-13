########################### Modules ###########################
import os
import datetime
import argparse
import socket
########################### Splash & Usage Guide ###########################
def start_banner():
    print("\n")
    print("         :::::::::   ::::::::  ::::::::: :::::::::::           ::::::::   ::::::::      :::     ::::    ::: ::::    ::: :::::::::: ::::::::: ")
    print("        :+:    :+: :+:    :+: :+:    :+:    :+:              :+:    :+: :+:    :+:   :+: :+:   :+:+:   :+: :+:+:   :+: :+:        :+:    :+: ")
    print("       +:+    +:+ +:+    +:+ +:+    +:+    +:+              +:+        +:+         +:+   +:+  :+:+:+  +:+ :+:+:+  +:+ +:+        +:+    +:+  ")
    print("      +#++:++#+  +#+    +:+ +#++:++#:     +#+              +#++:++#++ +#+        +#++:++#++: +#+ +:+ +#+ +#+ +:+ +#+ +#++:++#   +#++:++#:    ")
    print("     +#+        +#+    +#+ +#+    +#+    +#+                     +#+ +#+        +#+     +#+ +#+  +#+#+# +#+  +#+#+# +#+        +#+    +#+    ")
    print("    #+#        #+#    #+# #+#    #+#    #+#              #+#    #+# #+#    #+# #+#     #+# #+#   #+#+# #+#   #+#+# #+#        #+#      #+#   ")
    print("   ###         ########  ###    ###    ###               ########   ########  ###     ### ###    #### ###    #### ########## ###        ###  ")
    print("  ###" + " :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ###")
    print(" ### "+ ":::::::::::::::::::::::::::::::::::::::::::::::::::: By Tayor McManiman :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ###")
    print("### :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ### \n")
    print("Mandatory Usage Argurments:")
    print("1 [-H]: {Target Host} / [-T]: {Input File With List of Hosts}")
    print("2 [-P]: {Target Port}\n")
    print("Optional Usage Arguments:")
    print("3 [-L]: {Logfile Name} \n")
########################### Arguments Parsing ###########################
def parse_arguments():
    parser = argparse.ArgumentParser(description="Subnet Port Scanner By TM")
    parser.add_argument("-H", "--host", help="target host to scan.")
    parser.add_argument("-T", "--target_file", help="target file to scan for hosts.")
    parser.add_argument("-P", "--port", help="target port.")
    parser.add_argument("-L", "--logfile", help="output logfile.")
    return parser.parse_args()
########################### New Instance Runtime ###########################
def process_banner():
    print("\n")
    print("############ NEW RUN ##############")
    print("# " + "Date:" + str(datetime.datetime.now()) + " #")
    print("###################################")
########################### Host List Target File ###########################
def read_file(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]
########################### Host IP Scanning ###########################
def scan_host(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
        scan.settimeout(5)
        try:
            scan.connect((host, int(port)))
            return True
        except:
            return False
########################### Main Code ###########################
def log_to_file(logfile, data):
    with open(logfile, "a") as f:
        f.write(data + "\n")
########################### Main Code ###########################
args = parse_arguments()
os.system('cls')
start_banner()
target_hosts = []

if args.host and not args.target_file:
    target_hosts = [args.host]
    os.system('cls')
    start_banner()

if args.target_file and not args.host:
    target_hosts = read_file(args.target_file)
    os.system('cls')
    start_banner()

if args.logfile:
    log_to_file(args.logfile, "\n")
    log_to_file(args.logfile, "############ NEW RUN ##############")
    log_to_file(args.logfile, "# Date:" + str(datetime.datetime.now()) + " #")
    log_to_file(args.logfile, "###################################")

for host in target_hosts:
    if scan_host(host, args.port):
        status = "Open"
    else:
        status = "Closed"
    message = "Host: {}  Port: {}  Status: {}".format(host, args.port, status)
    print(message)

    if args.logfile:
        log_to_file(args.logfile, message)