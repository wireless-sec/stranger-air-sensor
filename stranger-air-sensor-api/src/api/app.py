#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

# 示例数据
users = [
    {'id': 1, 'name': 'John Doe'},
    {'id': 2, 'name': 'Jane Doe'}
]


@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201


if __name__ == '__main__':
    app.run(debug=True)
