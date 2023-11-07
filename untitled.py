from dotenv import load_dotenv
load_dotenv("ganache_mnem.env")
from bip44 import Wallet
import os

mnemonic = os.getenv("MNEMONIC")
print(mnemonic)