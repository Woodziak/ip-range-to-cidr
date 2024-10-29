import ipaddress

def ip_range_to_cidr(start_ip, end_ip):
    cidrs=[ipaddr for ipaddr in ipaddress.summarize_address_range(ipaddress.IPv4Address(start_ip), ipaddress.IPv4Address(end_ip))]
    return cidrs

while(True):
    # Example usage
    start_ip = input("Enter the starting IP address: ")
    end_ip = input("Enter the ending IP address: ")

    try:
        cidr_list = ip_range_to_cidr(start_ip, end_ip)
        print("The CIDR subnets for the given range are:")
        network_strings = [str(network) for network in cidr_list]
        print(network_strings)
    except ValueError as e:
        print(f"Error: {e}")