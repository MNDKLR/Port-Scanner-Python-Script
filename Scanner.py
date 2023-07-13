######################################### Import Modules: ###############################################
import datetime 
import argparse
import socket
# modules for use in the program later.
###################################### Reading From File: ####################################################
def read_file(filename): 
    with open(filename, "r") as f:
        return (line.strip() for line in f.readlines())    
# Opens target file in "read" mode in a variable "f".    
# Returns the contents of the file with the whitespace removed. 
###################################### Appending To File: ####################################################
def log_to_file(logfile, data):
    with open(logfile, "a") as f:                         
        f.write(data + "\n")       
# opens the logfile in "Append" mode through the variable "f".                      
# uses the write() fucntion to append the file with the program output and a newline for readability. 
######################################## Port Scanning: ######################################################
def scan_host(host, port):
    with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as scan:
        scan.settimeout (5)
        try:
            scan.connect((host, int(port)))
            return  True
        except:
            return False
# Uses socket module to establish a TCP connecion to the user specified host with the connect() function.
# Uses a timeout to ensure the program is responsive.
############################################ Arguments #######################################################
def parse_arguments():
    parser = argparse.ArgumentParser(description="Subnet Port Scanner By TM")
    group = parser.add_mutually_exclusive_group()
    group.add_argument ("-H", "--host",        help="target host to scan."          )
    group.add_argument ("-T", "--target_file", help="target file to scan for hosts.")
    parser.add_argument("-P", "--port",        help="target port."                  )
    parser.add_argument("-L", "--logfile",     help="output logfile."               )              
    return parser.parse_args()
# Command line arguments are defined here, while also establishing a group variable containing the-
# exclusive arguments which prevents the user from specifying -H and -T at the same time thus ensuring-
# -the OR aspect of the two arguments. 
# The parser variable is returned and the supplied argeuments can then be converted into usable objects -H,-T, etc. 
########################################### Usage Guide ###################################################### 
def usage_guide(): 
    print("#################################################################################################")
    print("#                                                                                               #")
    print("#     usage: %prog (-H <target host> | -T <target or filename>)                                 #") 
    print("#                   -P <target port>                                                            #")
    print("#                  [-L <logfile name>]                                                          #")
    print("#                                                                                               #")
    print("#     1. To Use this script enter: python {filename}.py followed by the above arguments.        #")
    print("#     2. (.|.): Denotes Mandatory Argument -H OR -T.                                            #")
    print("#     3. [...]: Denotes Optional Argument, In this case the user logfile.                       #")
    print("#                                                                                               #")
    print("#################################################################################################")
# Usage guide in terminal run, fairly self-explanatory.
############################################# Main Code: #####################################################
def main():
    args = parse_arguments()
    if not args.port: 
        usage_guide()
        return
    # port will not be specified at first run, resulting in the usage dialogue being displayed.
    if args.port:
         print("\n")
         print("############ NEW RUN ##############"               ) 
         print("# " + "Date:" + str(datetime.datetime.now()) + " #")
         print("###################################"               )
    # when the user makes the first input the port MUST be included otherwise the program wont work.
    # tying the port to the above dialogue ensures that when the program is used correctly the message will-
    # -display. 
    if args.host:   
        target_hosts = [args.host]
    # if -H is specified target host variable is = to that user specified value. 
    # [] ensures that -H option is a single value and prevents each char from being scanned-
    # -as individual values like ("hello world") instead of (h,e,l,l,o,w,o,r,l,d) (found out the hard way...)
    if args.target_file:
        target_hosts = read_file(args.target_file)
    # same above however if the user decides to use -T then the value of target hosts changes to that of-
    # -the specified input file. 
    if args.logfile:
            log_to_file(args.logfile, "\n")
            log_to_file(args.logfile, "############ NEW RUN ##############           ")
            log_to_file(args.logfile, "# Date:" + str(datetime.datetime.now()) + " # ")
            log_to_file(args.logfile, "###################################           ")
    # if the user specifies a logfile the above banner is created inside that file using the log to file-
    # -function. 
    for host in target_hosts:
        if scan_host(host, args.port):
            status = "Open"
        else:
            status = "Closed"
        message = "Host: {}  Port: {}  Status: {}".format(host, args.port, status)
        print(message)
        if args.logfile:
            log_to_file(args.logfile, message)
    # For every host address held by the target host variable the loop will iterate over each and attempt a-
    # - connection with the specified port and address using scan host. A status is then assigned and is then-
    # - printed in a message that is formatted to automatically input the values for readabilityâ€™s sake. 
    # once again if -L is present this is then also logged to that file. 
if __name__ == "__main__":
    main()
# Basic conditional that ensures the program can only ru if it is the "main" program (not imported).
