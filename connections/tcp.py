import subprocess
import sys


def netcat_connect(host, port, timeout=5):
    """
    Uses the nc (netcat) command to check if a host:port is alive/reachable.

    Args:
        host (str): The hostname or IP address to check
        port (int): The port number to check
        timeout (int): Connection timeout in seconds (default: 5)

    Returns:
        bool: True if connection successful, False otherwise
    """
    try:
        # Use nc with timeout and exit immediately after connection
        # -z: scan for listening daemons, without sending any data
        # -w: timeout for connects and final net reads
        result = subprocess.run(
            [
                "nc",
                "-z",
                "-w",
                str(timeout),
                host,
                str(port),
            ],
            capture_output=True,
            text=True,
            timeout=timeout + 1,  # Give subprocess a bit more time than nc timeout
        )

        if result.returncode == 0:
            print(f"✓ Connection to {host}:{port} successful")
            return True
        else:
            print(f"✗ Connection to {host}:{port} failed")
            return False

    except subprocess.TimeoutExpired:
        print(f"✗ Connection to {host}:{port} timed out after {timeout} seconds")
        return False
    except FileNotFoundError:
        print("Error: netcat (nc) command not found. Please install netcat.")
        return False
    except Exception as e:
        print(f"Error checking connection: {e}")
        return False
