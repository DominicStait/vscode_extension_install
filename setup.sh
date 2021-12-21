#!/usr/bin/env bash

# Create python virtual environment
python3 -m venv venv

# Install requirements
./venv/bin/pip3 install -r  requirements.txt

# Symlink bash scripts into /usr/local/bin for easy usage
ln -s $(pwd)/vscode_ext_install.sh ../vscode-ext-install
ln -s $(pwd)/vscode_update_extensions.sh ../vscode-update-extensions
