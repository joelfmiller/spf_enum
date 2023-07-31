import dns.resolver
import re
import ipaddress
import sys

def get_spf_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'SPF')
        for rdata in answers:
            return rdata.strings[0].decode('utf-8')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass

    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        for rdata in answers:
            data = rdata.strings
            for record in data:
                record_str = record.decode('utf-8')
                if record_str.startswith('v=spf1'):
                    return record_str.strip('"')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        pass

    return None

def extract_networks_from_spf(spf_record):
    if not spf_record:
        return []

    networks = []
    pattern = r'(?i)ip[46](:|%3[ae])([^\s]*)'
    matches = re.findall(pattern, spf_record)

    for match in matches:
        try:
            network = ipaddress.ip_network(match[1])
            networks.append(network)
        except ValueError:
            pass

    return networks

def enumerate_includes(domain, included_networks=None, level=0):
    if included_networks is None:
        included_networks = set()

    indent = '  ' * level
    print(f"{indent}[+] Fetching SPF record for: {domain}")

    spf_record = get_spf_record(domain)
    if not spf_record:
        return included_networks

    networks = extract_networks_from_spf(spf_record)
    included_networks.update(networks)

    for network in networks:
        print(f"{indent}  [-] {network}")

    includes = re.findall(r'(?i)\binclude:(\S+)', spf_record)
    for include in includes:
        #enumerate_includes(include, level + 1)
        included_networks.update(enumerate_includes(include, included_networks, level + 1))

    return included_networks

def separate_ipv4_ipv6(networks):
    ipv4_networks = [network for network in networks if isinstance(network, ipaddress.IPv4Network)]
    ipv6_networks = [network for network in networks if isinstance(network, ipaddress.IPv6Network)]
    return ipv4_networks, ipv6_networks

def main():
    if len(sys.argv) > 1:
        # Use the domain provided as a command-line argument
        domain = sys.argv[1]
    else:
        # Prompt for the domain name if no argument is provided
        domain = input("Enter the domain name: ")

    included_networks = enumerate_includes(domain)
    ipv4_networks, ipv6_networks = separate_ipv4_ipv6(included_networks)

    #print("\nIPv4 Networks found in the SPF record:")
    #for network in ipv4_networks:
    #    print(network)

    #print("\nIPv6 Networks found in the SPF record:")
    #for network in ipv6_networks:
    #    print(network)

    total_hosts_ipv4 = sum(network.num_addresses for network in ipv4_networks)
    total_hosts_ipv6 = sum(network.num_addresses for network in ipv6_networks)
    total_hosts = total_hosts_ipv4 + total_hosts_ipv6

    print(f"\n[+] Total number of IPv4 hosts: {total_hosts_ipv4}")
    print(f"[+] Total number of IPv6 hosts: {total_hosts_ipv6}")
    print(f"[+] Total number of hosts in the SPF record: {total_hosts}")

if __name__ == "__main__":
    main()
