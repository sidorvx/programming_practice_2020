from collections import defaultdict
from sys import stdin

clients = defaultdict(lambda: defaultdict(int))

for line in stdin.readlines():
    client, item, number = line.split()
    clients[client][item] += int(number)

clients_sorted = sorted(clients)

for client in clients_sorted:
    print(client)
    for item in sorted(clients[client]):
        print(item, clients[client][item])
