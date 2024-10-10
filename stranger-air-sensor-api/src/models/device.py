#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime

from sqlalchemy import Column, Integer, DateTime

from src.models.base import Base


class Device(Base):
    """
    用于表示识别出的一个设备
    """
    __tablename__ = 'devices'

    # 主键ID
    id = Column(Integer, primary_key=True, autoincrement=True)

    
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
