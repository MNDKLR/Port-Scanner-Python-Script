
<h1>Python Based Port Scanner Script</h1>

<p align="center">
Launched Program In Terminal Environment:<br/>
<img src="https://i.imgur.com/UqlEdCS.png" height="80%" width="80%" alt="Launched Program"/>
</p>

<h2>Description</h2>
<br> This Project was designed In order to demonstrate the practical applications of a Python-based script with the capability of carrying out network reconnaissance. The program is capable of taking a user-specified host IP address for the purposes of a scan in order to identify potentially vulnerable ports and by extension the services operating on them. The program is also capable of taking a list of host addresses from an input .txt file and performing a subsequent scan on each listed address therein, thus automating the scanning process. The program is also capable of scanning ports in a range decided entirely by the user for example port 1 to port 1000. Finally should the user desire an optional logfile for the purposes of review they are able to do so using built-in command line arguments whlst also specifying the directory they would like the new file to be created in.  </br>

<h2>IMPORTANT NOTE:</h2>       
<b>In regards to covert network reconnaissance it is likely that this program is easily picked up by an IDS . This is due to the methods used to conduct the port scans which are not stealthy by any means and therefore in absolutely no circumstance should this script be used for real reconnaissance which I hope goes without saying as there are potentially hundreds of tools that do a much better job :) This code is strictly a bit of educational fun.</b>

<h2>Typical Usage Instructions:</h2>
Located at the bottom of the readme is a screenshot of the working script just after being ran which includes the detailed usage instructions.                       
Typical usage is: "python {filename}.py {-H for a specific target IP} OR {-T filename with the list of addresses} then {-S For the starting port number} and {-E for the end port number}."   
This should look like: "python Scanner.py -H 8.8.8.8 -S 1 -E 100" to use the logfile function simply add after that the argument and the directory of the logfile to be created in including the filename with .txt 
for example: " -L 'C:\this\is\a\fake\directory\logfile.txt' ".  


<h2>Another note from myself:</h2>
<br> As my first personal project this was an exciting way to not only test my own programming proficiency but to also create a piece of work closely tied to an industry that I am passionate about. My hope is that this project and others like it in the future can have a place to be seen like a portfolio. Finally It must be noted that THIS PROJECT IS STILL IN DEVELOPMENT but more importantly I hope this has been an interesting read for you, cheers! -Taylor</br>

<h2>Environments Used </h2>

- <b>Windows 11</b>
- <b>Visual Studio Code</b> 

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
