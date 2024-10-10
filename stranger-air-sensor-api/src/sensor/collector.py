#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scapy.all import sniff
from scapy.layers.dot11 import Dot11ProbeReq


# 用于抓包上报
# 定义数据包处理函数
def packet_callback(packet):
    if not packet.haslayer(Dot11ProbeReq):
        return
    print(packet.show())


# 开始嗅探
# iface 参数指定网络接口，例如 "eth0"，"wlan0"
# prn 参数指定数据包处理函数
# count 参数指定嗅探的数据包数量，0 表示无限制
sniff(iface="en0", prn=packet_callback, count=0)
