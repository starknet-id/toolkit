#!/usr/bin/env python3
from starkware.crypto.signature.signature import private_to_stark_key
import sys

argv = sys.argv
priv_key = argv[1]

if priv_key.startswith("0x"):
    priv_key = int(priv_key, 16)
else:
    priv_key = int(priv_key)

pub_key = private_to_stark_key(priv_key)
print("decimal:", pub_key)
print("hex:", hex(pub_key))
