# checks consistency replica state for all nodes in the given hosts file
# run as python check_consistency [hosts_path]

import requests
import sys
import os

def get_nodes(hosts_path=None):
    """Parses a hosts file to a dict of nodes such that dct[id] = node."""
    if hosts_path is None:
        hosts_path = os.getenv("HOSTS_PATH", "../hosts.txt")

    if not os.path.isfile(hosts_path):
        raise ValueError(f"Could not find hosts file at {hosts_path}")
    with open(hosts_path) as f:
        lines = [x.strip().split(",") for x in f.readlines()]
        nodes = []
        for l in lines:
            nodes.append({ "id": l[0], "hostname": l[1], "ip": l[2], "port": l[3] })
        return nodes

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("run as python check_consistency.py [abs_path_to_hosts_file]")
        sys.exit(1)
    hosts_path = sys.argv[1]
    nodes = get_nodes(hosts_path)
    states = []
    seq_num = -1

    for n in nodes:
        url = f"http://{n['hostname']}:400{n['id']}/data"
        data = requests.get(url).json()

        if len(data["REPLICATION_MODULE"]["pend_reqs"]) > 0:
            print(f"{n['hostname']} still has requests pending")
            sys.exit(1)

        states.append(data["REPLICATION_MODULE"]["rep_state"])
        n_seq_num = data["REPLICATION_MODULE"]["seq_num"]
        if n_seq_num > seq_num:
            seq_num = n_seq_num

    if all(x == states[0] for x in states) and seq_num == len(states[0]) - 1:
        print(f"Nodes are consistent for state with length {len(states[0])}")
    else:
        print("Error: nodes are not consistent")

    