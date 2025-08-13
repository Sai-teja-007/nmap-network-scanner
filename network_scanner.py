import subprocess
import sys
import datetime

def run_nmap(target):
    filename = f"nmap_full_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    print(f"[+] Scanning target: {target}")
    print(f"[+] Full report will be saved to: {filename}")

    
    command = [
        "nmap", "-p-", "-A", "-T4", target
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        with open(filename, "w") as file:
            file.write(result.stdout)
        print("[+] Scan completed successfully!")
        print(f"[+] Report saved as {filename}")
    except Exception as e:
        print(f"[!] Error running Nmap: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 full_network_scanner.py <target_ip_or_domain>")
        sys.exit(1)

    target = sys.argv[1]
    run_nmap(target)
