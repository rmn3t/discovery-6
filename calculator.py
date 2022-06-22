import ipaddress
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(' -n', ' --network', help-"The network in the format x.x.x.x/x.")
    args = parser.parse_args()


class IPCalculator:

    def __init__(self, network):
        self.network = ipaddress.IPv4Network(network)

    def get_network(self):
        """ Returns the Network. """

        return str(self.network)

    def get_first_ip(self):
        """Calculates the first IP address. """

        first_ip = list(self.network.hosts())[0]
        return str(first_ip)

    def get_last_ip(self):
        """Calculates the last IP address. """

        last_ip = list(self.network.hosts())[-1]
        return str(last_ip)

    def get_broadcast_address(self):
        """Calculates the broadcast address. """

        return self.network.broadcast_address

    def get_network_address(self):
        """Calculates the last address. """

        return self.network.broadcast_address

    def get_netmask(self):
        """Calculates the netmask. """

        return self.network.netmask




