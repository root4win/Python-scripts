import socket

def check_open_port(host: str, port:int) -> bool:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        response = sock.connect_ex((host, port))
        sock.close()
        return response == 0
    except Exception as e:
        return False
    
def open_port_scanner(host:str, ports:list) -> None:
    bar = "#"
    for port in ports:
        bar += "#"
        print(bar)
        if check_open_port(port):
            print(f"[+] Port {port} is open at host {host}")

if __name__ == "__main__":
    target_host = input("Insert the hostname or IP")
    ports_to_scan = input("Insert the opens to scan (ex: 80, 22, 8080): ").split(",")
    ports_to_scan = [int(port).strip() for port in ports_to_scan]

    open_port_scanner(target_host, ports_to_scan)         