#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, DateTime, func, String

from src.models.base import Base


class Wifi(Base):
    """
    用于记录当前已知wifi
    """
    __tablename__ = 'device_wifi'

    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(DateTime, default=func.now())
    update_time = Column(DateTime, default=func.now(), onupdate=func.now())

    # wifi的ssid
    ssid = Column(String, unique=True)

    # 最后一次发现它存活的时间，注意，这个时间是由最后一次接收到它的信号的时间决定的
    last_active_time = Column(DateTime, default=func.now())
