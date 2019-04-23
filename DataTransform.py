class DataTransform:

    def update_port_data(self, port_scanner):
        self.PortScanner = port_scanner
        self.process_data()

    def process_data(self):
        # TODO: Add in error catching. What if scan results is empty??

        # Extract PortScanner data to list instances
        for i in range(len(self.ip_addresses)):
            self.host_state.append(self.PortScanner[self.ip_addresses[i]].state())
            self.host_name.append(self.PortScanner[self.ip_addresses[i]].hostname())
            self.host_protocols.append(self.PortScanner[self.ip_addresses[i]].all_protocols())
            self.host_keys.append(self.PortScanner[self.ip_addresses[i]].keys())

    def __init__(self,port_scanner):
        # Initialize Instances Data
        self.PortScanner = port_scanner
        self.ip_addresses = port_scanner.all_hosts()
        print(port_scanner.all_hosts())
        self.host_state = []
        self.host_name = []
        self.host_protocols = []
        self.host_keys = []

        # Run Process Data Function
        self.process_data()


