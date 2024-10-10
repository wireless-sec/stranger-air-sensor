#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

sqlite3_database_path = 'stranger-air-sensor.db'

# 连接到 SQLite 数据库
conn = sqlite3.connect(sqlite3_database_path)

