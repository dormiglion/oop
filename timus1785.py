n = int(input())
data = {
    "few": 4,
    "several": 9,
    "pack": 19,
    "lots": 49,
    "horde": 99,
    "throng": 249,
    "swarm": 499,
    "zounds": 999,
    "legion": 2000
}
for i in data:
    if n <= data[i]:
        print(i)
        break