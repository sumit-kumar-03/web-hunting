import subprocess
import sys

def dig_domain(domain, dns_server="8.8.8.8"):
    """
    Executes the dig command for the given domain and DNS server.
    Returns the output as a string.
    """
    try:
        result = subprocess.run(
            ["dig", "+short", domain, f"@{dns_server}"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing dig: {e}")
        return None


