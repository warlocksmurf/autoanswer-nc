from pwn import *

def main():
    ip_port = input("Enter target IP and port (format: IP:PORT): ")
    try:
        HOST, PORT = ip_port.split(":")
        PORT = int(PORT)
    except ValueError:
        print("Invalid format. Use IP:PORT.")
        return

    answers = input("Enter answers separated by commas: ").split(",")
    answers = [ans.strip() for ans in answers]

    conn = remote(HOST, PORT)

    for ans in answers:
        conn.recvline()
        conn.sendline(ans)

    conn.interactive()

if __name__ == "__main__":
    main()
