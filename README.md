
<h1>Python Based Port Scanner Script</h1>

<h2>Description</h2>
<br> This Project was designed In order to demonstrate the practical applications of a Python-based script with the capability of carrying out network reconnaissance. The program is capable of taking a user-specified host IP address for the purposes of a scan in order to identify potentially vulnerable ports and by externsion the services operating on them. The program is also capable of taking a list of host addresses from an input .txt file and performing a subsequent scan on each listed address therein, thus automating the scanning process. Currently the prorgram must be given a specific port to scan in the form of a command line argument when running the script in a terminal, however the goal is to optionally allow for a range of ports to be scannned in a single instance. Finally the program can carry out limited logging to a file for the purposes of usage history tracking with dated entries for increased accuracy. </br>

<h2>Typical Usage Instructions:</h2>
Located at the bottom of the readme is a screenshot of the working script just after being ran which includes the detailed usage instructions.                       
Typical usage is: "python {filename}.py {-H for a specific target IP} OR {-T filename with the list of addresses} {-P and the port number to scan}"   
This should look like: "python Scanner.py -H 8.8.8.8 -P 80" to use the logfile function simply add after that "-L {your outputfile.txt}" 


<h2>A note from myself:</h2>
<br> As my first personal project this was an exciting way to not only test my own programming proficiency but to also create a piece of work closely tied to an industry that I am passionate about. My hope is that this project and others like it in the future can have a place to be seen like a portfolio of sorts. Finally It must be noted that THIS PROJECT IS STILL IN DEVELOPMENT and hopefully this has been an interesting read for you, cheers! -Taylor</br>

<h2>Environments Used </h2>

- <b>Windows 11</b>
- <b>Visual Studio Code</b> 

<h2>Working Program:</h2>
<p align="center">
Launched Program In Terminal Environment:<br/>
<img src="https://i.imgur.com/jwRdsuN.png" height="80%" width="80%" alt="Launched Program"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
