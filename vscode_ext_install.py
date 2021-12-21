from bs4 import BeautifulSoup
import requests
from sys import argv
import os
import json
from uuid import uuid4

CA_BUNDLE = "/etc/pki/tls/certs/ca-bundle.crt"
MARKETPLACE_URL = "https://marketplace.visualstudio.com/items?itemName="
VSCODE_VERSION = os.popen("code --version | head -n1").read().strip("\n")
HEADERS = {
    "User-Agent": "VSCode " + str(VSCODE_VERSION),
    "X-Market-Client-Id": "VSCode " + str(VSCODE_VERSION),
    "X-Market-User-Id": str(uuid4()),
}


def main(ext_name):
    """
    Find the latest version of the extension, download it into /tmp
    then attempt to install it into VSCode.
    """
    publisher_name, extension_name = ext_name.split(".")
    r = requests.get(MARKETPLACE_URL + ext_name, verify=CA_BUNDLE)
    soup = BeautifulSoup(r.text, "html.parser")
    content = soup.find("div", attrs={"class": "rhs-content"}).script.string
    version = json.loads(content)["Resources"]["Version"]

    filename = "/tmp/" + ext_name + ".vsix"
    download_url = (
        f"https://marketplace.visualstudio.com/"
        f"_apis/public/gallery/publishers/{publisher_name}"
        f"/vsextensions/{extension_name}/{version}/vspackage"
    )

    with requests.get(
        download_url, headers=HEADERS, verify=CA_BUNDLE, stream=True
    ) as dl:
        with open(filename, "wb") as file:
            for chunk in dl.iter_content(chunk_size=8192):
                file.write(chunk)

    os.system("code --install-extension " + filename)
    os.system("rm -f " + filename)


if __name__ == "__main__":
    if len(argv) == 2:
        ext_name = argv[1]
    else:
        print(
            "Please pass a single extension id in the format of publisher.extensionname"
        )
        exit(1)
    main(ext_name)
