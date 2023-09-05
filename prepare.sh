#!/bin/bash

sudo apt install --yes postgresql
sudo apt install --yes python3-pip
sudo apt install --yes python3-tk
sudo apt install --yes python3-zbar
sudo apt install --yes git
pip install -r requirements.txt

echo "Requirements instalados, crie a tabela no PostgreSQL"
