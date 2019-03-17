# BFTList-client
Code for running both centralized and distributed BFTList clients. Note that this code has been implemented as mere help tool, gving little time to follow best practices during development.

## Setup
```
git clone git@github.com:practicalbft/BFTList-client.git && cd BFTList-client
chmod +x *.sh
python3.7 -m venv env
source ./env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Make sure that BFTList is running either locally or on PlanetLab and simply supply the absolute path to the corresponding `hosts.txt` to the scripts below.

## Running the interactive client shell
```
./start_shell.sh [absolute_path_to_hosts_file]
```

## Running clients locally
```
./run_clients_local.sh [absolute_path_to_hosts_file] [nbr_of_clients] [reqs_per_client]
```

## Running clients distributed
`// TODO`

## Checking node consistency

