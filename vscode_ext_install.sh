#!/usr/bin/env bash

INSTALL_DIR="/usr/local/bin/vscode_extension_install/"

$INSTALL_DIR/venv/bin/python3 $INSTALL_DIR/vscode_ext_install.py "$@"