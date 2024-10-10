#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scapy.all import rdpcap
from scapy.layers.dot11 import Dot11Beacon, Dot11Elt, Dot11

ssid = beacon[Dot11Elt].info.decode() if beacon[Dot11Elt].ID == 0 else None
bssid = beacon[Dot11].addr2
cap = beacon.sprintf("{Dot11Beacon:%Dot11Beacon.cap%}")
timestamp = beacon[Dot11Beacon].timestamp
beacon_interval = beacon[Dot11Beacon].beacon_interval

s.add(ssid)

print(f"SSID: {ssid}")
print(f"BSSID: {bssid}")
print(f"Capabilities: {cap}")
print(f"Timestamp: {timestamp}")
print(f"Beacon Interval: {beacon_interval}")
print("=" * 50)

# Load the .cap file
packets = rdpcap('./airportSniffsYHvPs.cap')

# Iterate through packets and print summary
for packet in packets:
    if not packet.haslayer(Dot11Beacon):
        continue
    parse_beacon_packet(packet)
