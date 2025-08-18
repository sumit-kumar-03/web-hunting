import socket

def get_ip_from_domain(domain, dns_server="8.8.8.8"):
    """
    Sends a DNS query to the specified public DNS server to fetch the IP address of the domain.
    Default DNS server is Google's 8.8.8.8.
    """
    try:
        # Use socket.gethostbyname for simple DNS resolution
        ip = socket.gethostbyname(domain)
        return ip
    except Exception as e:
        print(f"Error resolving domain {domain}: {e}")
        return None

