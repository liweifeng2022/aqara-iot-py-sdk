import hashlib



header = "abcede"

md5 = hashlib.md5()
md5.update(header.encode('utf-8'))
md5_str = md5.hexdigest()

print(md5_str)