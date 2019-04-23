from nmap import PortScanner


class CreatePortScanner(PortScanner):

    def __init__(self):
        PortScanner.__init__(self)
