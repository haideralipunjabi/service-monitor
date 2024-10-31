import subprocess
import yaml
import requests
import pathlib
import os

BASE = pathlib.Path(__file__).parent.resolve()
data = yaml.load(open(os.path.join(BASE, "config.yaml"), "r"), Loader=yaml.Loader)
for server in data["servers"]:
    response = subprocess.call(
        ["ping", "-c", "1", server["ip"]],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
    if response != 0:
        requests.get(
            f"https://api.telegram.org/bot{data['telegram']['api_key']}/sendMessage?chat_id={data['telegram']['chat_id']}&text={server['name']} is down"
        )
