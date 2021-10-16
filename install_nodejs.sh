#!/bin/bash
export NVM_DIR=$HOME/.nvm;
source $NVM_DIR/nvm.sh;

url=https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh

curl ${url} -o- | bash

source ~/.bashrc

[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

nvm install v14.18.0

version= node -v

echo "установка ${version} прошла успешно"

