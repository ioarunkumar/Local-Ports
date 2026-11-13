
import psutil

print("\n=== RUNNING LOCALHOST & OPEN PORTS ===\n")

connections = psutil.net_connections(kind="inet")

for conn in sorted(connections, key=lambda c: c.laddr.port):
    if conn.status == "LISTEN":
        ip = conn.laddr.ip
        port = conn.laddr.port

        try:
            process = psutil.Process(conn.pid).name()
        except (psutil.NoSuchProcess, psutil.AccessDenied, TypeError):
            process = "Unknown"

        print(f"{ip:<20} PORT: {port:<6} PROCESS: {process}")

print("\n=== SCAN COMPLETED ===")
