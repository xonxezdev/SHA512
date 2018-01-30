import sys, hashlib, time
W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[32m'
O = '\x1b[33m'
B = '\x1b[1m'
RR = '\x1b[3m'
print RR+"Author : Rizal Solehudin "+W
hash = hashlib.sha512(raw_input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O))).hexdigest()
print '%s%s  %s' % (W, RR, W)
print '%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash)
print '%s' % W
sys.exit()