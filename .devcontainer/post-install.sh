#!/bin/bash
set -ex

##
## Create some aliases
##
echo 'alias ll="ls -alF"' >> $HOME/.bashrc
echo 'alias la="ls -A"' >> $HOME/.bashrc
echo 'alias l="ls -CF"' >> $HOME/.bashrc

# Convenience workspace directory for later use
WORKSPACE_DIR=$(pwd)

# Change some Poetry settings to better deal with working in a container and install dependencies


poetry config cache-dir ${WORKSPACE_DIR}/.cache
poetry config virtualenvs.in-project true
poetry install

#Add /workspaces/gx-activation-service as a safe Git Repo.

git config --global --add safe.directory ${WORKSPACE_DIR}

echo "Done!"