import yaml
import argparse

data = yaml.load(open("config.yaml", "r"), Loader=yaml.Loader)
parser = argparse.ArgumentParser(description="Config Service Monitor")
parser.add_argument("-a", "--add", help="Add a server", action="store_true")
parser.add_argument("-d", "--delete", help="Delete a server", action="store_true")
parser.add_argument("-l", "--list", help="List all server", action="store_true")
args = parser.parse_args()


def list_servers():
    for idx, server in enumerate(data["servers"]):
        print(f"{idx+1}) name: {server['name']}")
        print(f"   ip: {server['ip']}")


if args.add:
    print("Adding new server")
    name = input("Name: ")
    ip = input("IP: ")
    data["servers"].append({"name": name, "ip": ip})
    yaml.dump(data, open("config.yaml", "w"), Dumper=yaml.Dumper)
if args.delete:
    print("Deleting a server")
    list_servers()
    idx = int(input("Enter number to delete: "))
    if idx > 1 and idx <= len(data["servers"]):
        del data["servers"][idx - 1]
        yaml.dump(data, open("config.yaml", "w"), Dumper=yaml.Dumper)
        print("Deleted")
    else:
        print("Invalid Input")
if args.list:
    list_servers()
