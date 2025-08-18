from dns.dns_server import get_ip_from_domain
from dns.dig import dig_domain
from connections.tcp import netcat_connect
from connections.http import send_http_get
from enums import SERVICES


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python execute.py <service_name> <input>")
        sys.exit(1)

    service_name = sys.argv[1]
    input_value = sys.argv[2]
    second_input = sys.argv[3] if len(sys.argv) > 3 else None

    if service_name not in SERVICES:
        print(
            f"Unknown service: {service_name}. Available services: {', '.join(SERVICES)}"
        )
        sys.exit(1)

    ## Execute the service based on the input

    if service_name == "dns":
        domain = input_value
        if second_input:
            dns_server = second_input
        else:
            dns_server = "8.8.8.8"  # Default DNS server
        print("Starting DNS service...")
        ip = get_ip_from_domain(domain)
        if ip:
            print(f"IP address of {domain}: {ip}")
        else:
            print("Could not resolve domain.")

    elif service_name == "dig":
        domain = input_value
        print("Starting dig service...")
        output = dig_domain(domain)
        if output:
            print(output)
        else:
            print("No output from dig command.")

    elif service_name == "netcat":
        host = input_value
        port = int(second_input) if second_input else 80
        print("Starting netcat service...")
        netcat_connect(host, port)

    elif service_name == "http":
        domain = input_value
        print("Starting HTTP service...")
        send_http_get(domain)
