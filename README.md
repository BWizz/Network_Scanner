# Network_Scanner
Network scanner, database creator and report generator using Python, nmap, sqlite3, and docx. 

## System Information

This application was developed in Python 3.7.3 and uses the following additional modules:
  1. python-nmap from nmap.org

  2. Python-docx




## Example Usage

- To run the application call main.py
- From the command line, the program will request the user to enter an IP address range.
  - Example Entry: 192.168.2.* or 192.168.2.0/24
- Next the command line will request the user to enter a port or port range.
  - Example Entry: 20 or 20-40
- Next the software will run a network scan and ping all devices using the IP and port range entered.
- The application will format the data and generate a sqlite database
- The application will generate a word document report containing a table with IP Address and Host names of all devices it found.



## TODO's
This project was developed to help a friend with a school assignment and never ment as a final project but I figured I would share it regardless. The following items are needed to ensure the software is robust:
- Class level error catching, and handling.
  - Currently a empty result of the nmap scan will cause a software error.
  - During multple scans, if the word document is left open, there applicaton will not be able to modify it and therefore a software error will rise.
- Check the user inputs for improper entry
  - Incorrect ip address or port entries will cause a software error.



