#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 这个脚本可以发现你附近出现了新的人（视野之外）

# 判断是否是开启了mac地址虚拟化

from scapy.all import sniff, Dot11ProbeReq




def handle_probe_request(packet):
    if packet.haslayer(Dot11ProbeReq):
        ssid = packet.info.decode('utf-8') if packet.info else '<Broadcast>'
        mac_address = packet.addr2
        print(f"Probe Request from {mac_address} for SSID {ssid}")


# 使用无线接口（如 wlan0mon）捕获 Probe Request 数据包
sniff(iface='wlan0mon', prn=handle_probe_request, filter='type mgt subtype probe-req', store=0)
