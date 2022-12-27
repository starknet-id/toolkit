#!/usr/bin/env python3
from starkware.crypto.signature.signature import get_random_private_key

private_key = get_random_private_key()
print("decimal:", private_key)
print("hex:", hex(private_key))
