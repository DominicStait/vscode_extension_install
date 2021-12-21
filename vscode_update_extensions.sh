#!/usr/bin/env bash

for EXT in $(ls ~/.vscode/extensions); do
    extension_name=$(echo $EXT | rev | cut -d "-" -f 2- | rev)
    vscode-ext-install $extension_name
done