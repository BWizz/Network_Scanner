# Import Modules
from DataTransform import DataTransform
from DBControl import DBControl
from GenReport import GenReport
from CreatePortScanner import CreatePortScanner


# Define Functions
def enter_ip_address():
    text = input("Please Enter IP Address: \n")  # Python 3
    return text


def enter_port_range():
    text = input("Please Enter Port Number or Range: \n")  # Python 3
    return text


def main():
    # Prompt User to Enter Inputs From Command Line
    ip_address = enter_ip_address()
    ports = enter_port_range()

    # Initialize port_scanner object
    port_scanner = CreatePortScanner()

    # Scan Network
    print('Network Scanning In Progress')
    port_scanner.scan(ip_address, ports)

    # Format Data
    print('Data formatting In Progress')
    data_transform = DataTransform(port_scanner)

    # Create Database
    print('Data Base Creation In Progress')
    data_base_file_name = DBControl.import_data(data_transform)

    # Generate Report
    print('Report Creation In Progress')
    GenReport.gen_report(data_base_file_name)
    print('Network Scan Complete')

# Run Code
main()

