#!/usr/bin/env bash

# Create python virtual environment
python -m venv venv

# Install requirements
venv/bin/pip3 install -r  requirements.txt

# Symlink bash script into /usr/local/bin for easy usage
ln -s vscode_ext_install.sh ../vscode-ext-install

