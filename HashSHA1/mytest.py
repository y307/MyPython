
import hashlib
from builtins import print

h = hashlib.sha1()
h.update(b"0442581665")
print(h)
print(h.hexdigest())
