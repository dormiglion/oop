import math

l, h, w = input().split()
l = int(l) / 100
h = int(h) / 100
w = int(w) / 60

if h < 0.5 * l:
    t = 0
else:
    t = (2 * (h - 0.5*l) / 9.81) ** 0.5

c = t * w * 2 * math.pi

if math.cos(c) >= 0:
    print("butter")
else:
    print("bread")
