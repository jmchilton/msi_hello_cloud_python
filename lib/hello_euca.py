from libcloud.compute.base import NodeImage, NodeSize
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.types import NodeState
from libcloud.compute.ssh import SSHClient

import yaml

def main():
    with open("options.yaml") as in_handle:
        options = yaml.load(in_handle)["cloud_settings"]
    driver = get_driver(Provider.EUCALYPTUS)
    api_host = options["api_host"]
    access_key = options["ec2_access_key"]
    secret_key = options["ec2_secret_key"]
    driver_args = { "secret": secret_key,
                    "secure": False,
                    "host": api_host,
                    "port": 8773,
                    "path": "/services/Cloud" }
    conn = driver(access_key, **driver_args)
    print conn.list_nodes()

if __name__ == "__main__":
    main()
