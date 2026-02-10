import argparse
import ipaddress
from connect import Connect
import time

from parser import Parser

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
    seq = 0
    while True:
        # Get next packet from the receive queue and parse it
        packet = c.pop_next_packet()
        if packet:
            p.parse(packet)

        # Tick the send queue to send any pending messages
        c.tick_send_queue()

        time.sleep(1)


if __name__ == "__main__":
    main()