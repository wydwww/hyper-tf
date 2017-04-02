# This is a brief implementation to make sure
# That only one read / write operation happens at the same time

from kazoo.client import KazooClient
import argparse,time

def lock(kz, mutex_path="/tf/mutex/"):
    data, stat = kz.get(mutex_path)
    while data == "1":
        sleep(1)
    kz.set(data, "1")
    return

def unlock(kz, mutex_path="/tf/mutex/"):
    data, stat = kz.get(mutex_path)
    kz.set(data, "0")
    return 
