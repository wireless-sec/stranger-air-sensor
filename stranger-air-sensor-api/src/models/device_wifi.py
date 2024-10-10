#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Integer, Column, ForeignKey, DateTime, func

from src.models.base import Base


class DeviceWifi(Base):
    """
    用于记录设备都连接过哪些wifi
    """
    __tablename__ = 'device_wifi'

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime, default=func.now())
    update_time = Column(DateTime, default=func.now(), onupdate=func.now())

    # 哪台设备
    device_id = Column(Integer, ForeignKey('devices.id'))

    # 连接过哪个wifi
    wifi_id = Column(Integer, ForeignKey('wifis.id'))
