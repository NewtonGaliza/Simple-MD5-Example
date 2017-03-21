import hashlib

def md5hasher(data):
     md5hash = hashlib.md5()
     md5hash.update(data.encode("utf8"))
     print(md5hash.digest())
     print(md5hash.hexdigest())

md5hasher("hello world")
