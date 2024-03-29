### MX Recon

**TL;DR**  
I often do an nslookup and check MXToolbox for some info.  
So why not make a python script amiright  
it prints the mx, spf, and dmarc records but also organizes details for tags that are and are not declared, outputs into a txt file. 
______________________________________________________________  

**instructions**  

initial setup:  
* download the files.  
* change directory to download location.
* run 'pip install -r requirements.txt' to install dependencies. 

usage:  
1. run the script  
2. enter a domain name (example.com) at the prompt
3. press any key to exit
your example.com.txt report is now ready in the script's folder  

![instructions](https://github.com/cpardue/python3/blob/main/mx_recon/instructions.png?raw=true)
______________________________________________________________  

**Progress Report**  
Currently accepts input for a domain name, runs MX, SPF, DMARC checks and writes to a file named <domain>.txt, including minor details such as hardfail, softfail, p=none, etc. <br>
  Added file output to domain.com.txt.<br>
  Added a mini digest of cloud email gateway hosts for mx host identification.<br>
  Added SPF details parsing.<br>
  Added DMARC details parsing.<br>
  Added console logging for info and debug.<br>
  
Give it a try. If you like it, steal it and make it your own. 
______________________________________________________________  
  
**Some functionality ideas:**  
* check SPF final action to gauge SPF health - DONE  
* check DMARC percentage and policy action to gauge DMARC health - DONE 
* check MX Hostnames against known mail providers (Google, Cisco, Outlook, Proofpoint, etc) - DONE  
* save results to a file - DONE  
* check SPF hostnames against MX hostnames to gauge SPF health - Abandoned  
* logging enabled for troubleshooting - DONE
* argparse for accepting cli arguments - Pending  
* read csv list of domains, output multiple results files - Pending  




<p align=center>
<a href="https://www.buymeacoffee.com/cpardue0" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</p>
