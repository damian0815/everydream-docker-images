#!/bin/bash
echo "Worker Started"
echo $1
echo $2
echo $3
if [[ $PUBLIC_KEY ]]
then
    mkdir -p ~/.ssh
    chmod 700 ~/.ssh
    cd ~/.ssh
    echo $PUBLIC_KEY >> authorized_keys
    chmod 700 -R ~/.ssh
    cd /
    service ssh start
    echo "SSH Service Started"
fi

# Update and start worker
cd /workermode
pip install -r requirements.txt
curl -O https://raw.githubusercontent.com/entmike/docker-images/main/real-esrgan/workermode/workermode.py

python workermode.py --api $1 --agent $2 --owner ${3:-398901736649261056}
