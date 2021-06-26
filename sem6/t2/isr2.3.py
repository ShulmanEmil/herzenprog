import random
from hashlib import sha3_512
import binascii

genesis_block = bytearray([0 for i in range(0, 64)])
baseblock = genesis_block

blockchain = []

def history_list(blockchain):
  for i in blockchain:
    block = gen.send(random_gen.__next__())
    print("link=" + binascii.hexlify(block[0:64]).decode("iso-8859-1"))
    print("data=" + block[64:192].decode("iso-8859-1"))
    print("digest=" + binascii.hexlify(block[192:256]).decode("iso-8859-1"))
    print("======================")

def randomblock():
  while True:
    ml = sha3_512()
    ml.update(str(random.randint(0, 1e18)).encode("iso-8859-1"))
    yield bytearray(ml.hexdigest().encode("iso-8859-1"))

def signedblock(baseblock):
  block = yield
  while True:
    block_data = baseblock + block
    digest = sha3_512()
    digest.update(block_data)
    baseblock = digest.digest()
    yield block_data + digest.digest()

random_gen = randomblock()
gen = signedblock(genesis_block)
next(gen)
limit = 6
for i in range(0, limit):
  blockchain += [gen.send(random_gen.__next__())]

history_list(blockchain)
