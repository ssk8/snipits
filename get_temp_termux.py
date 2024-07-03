#! /data/data/com.termux/files/usr/bin/python
import httpx
import termux

r = httpx.get('http://192.168.1.101:8080/json')

termux.Notification.notify("Temperature", f"{r.json()['temp_c']:.01f}{r.json()['unit_c']}")
