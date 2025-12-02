# PF_Parser
A python script that parses an exported csv file from PFSense firewall logs, and sorts the comma-seperated values into readable and sortable columns for easier analysis.

![Python](https://img.shields.io/badge/Python-3.0+-blue)

# How to use
Firstly, one must download the security log file from their PFSense firewall. For more details, please refer to their documentation: https://docs.netgate.com/pfsense/en/latest/monitoring/logs/index.html. Once you have the .log file, follow the next steps. <br></br>
In your terminal: <br></br>
Clone the repo `git clone https://github.com/davidriverascode/PF_Parser` <br></br>
Go into the repo `cd PF_Parser` <br></br>
Run the script `python3 main.py` <br></br>
Pass the file path to your log file when prompted. Will most likely be something like `C:/Users/<insert your username>/Downloads/filter.log` <br></br>
Enjoy!
