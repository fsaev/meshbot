import argparse
import ipaddress
from connect import Connect
import time

from parser import Parser
from admin import AdminInterface
from messager import MessagerInterface

version = "0.1.0"

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Meshbot")
    parser.add_argument(
        "ip",
        type=ipaddress.ip_address,
        help="Target IP address (IPv4 or IPv6)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"IP: {args.ip}")
    c = Connect(str(args.ip))
    p = Parser()
    a = AdminInterface(c)
    m = MessagerInterface(c)
    
    c.queue_message("MeshBot v" + version + " is now online!", channel=1)
    while True:
        # Get next packet from the receive queue and parse it
        packet = c.pop_next_packet()
        if packet:
            parsed_packet = p.parse(packet)
            a.process_packet(parsed_packet)
            m.process_packet(parsed_packet)
        # Tick the send queue to send any pending messages
        c.tick_send_queue()

        time.sleep(1)


if __name__ == "__main__":
    main()