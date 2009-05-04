import string
import hashlib

def getKid(url):
    key = "%s" % hashlib.md5(url).hexdigest()
    kid = string.atoi(key[:10],16)
    return kid

if __name__ == '__main__':
    import sys
    print getKid(sys.argv[1])