# PF_Parser
A python script that parses an exported log file from PFSense firewall logs, and sorts the comma-seperated values into readable and sortable columns for easier analysis.

# Usage
Export the `/var/log/ipsec.log` file from your PFSense firewall machine. <br></br>
Change the extension from `.log` to `.txt`. <br></br>
Clone the repo (`git clone https://github.com/davidriverascode/PF_Parser`)<br></br>
Go into the repo directory `cd PF_Parser`, and run the script `python3 main.py`<br></br>
Pass the path to the logs text file when prompted<br></br>
After script runs, you should have a better formatted `.csv` file for easier analysis!<br></br>
