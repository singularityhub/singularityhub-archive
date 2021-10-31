---
id: 765
name: "ldynia/containerized-workshop"
branch: "master"
tag: "latest"
commit: "67c280dbd009c4b85addd68bcbbe927e5a9afbe6"
version: "8be74919d7ac1a44daa75dfcbbf35fa5"
build_date: "2017-11-09T15:40:54.524Z"
size_mb: 246
size: 27406367
sif: "https://datasets.datalad.org/shub/ldynia/containerized-workshop/latest/2017-11-09-67c280db-8be74919/8be74919d7ac1a44daa75dfcbbf35fa5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ldynia/containerized-workshop/latest/2017-11-09-67c280db-8be74919/
recipe: https://datasets.datalad.org/shub/ldynia/containerized-workshop/latest/2017-11-09-67c280db-8be74919/Singularity
collection: ldynia/containerized-workshop
---

# ldynia/containerized-workshop:latest

```bash
$ singularity pull shub://ldynia/containerized-workshop:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.6

%runscript

exec echo "The runscript is the containers default runtime command!"

%labels
AUTHOR ludd@cbs.dtu.dk

%post

# OS Update & Upgrade
apk update && apk upgrade

# Install packages
apk add \
  git \
  python \
  py-pip

# Clone git repo and remove git repo
git clone https://github.com/ldynia/containerized-workshop
mv /containerized-workshop/app /app
rm -rf /containerized-workshop

# Execute script as a global program
ln -s /app/main.py /usr/local/bin/fsa-analyzer
chmod +x /usr/local/bin/fsa-analyzer

echo "The post section is where you can install, and configure your container."
```

## Collection

 - Name: [ldynia/containerized-workshop](https://github.com/ldynia/containerized-workshop)
 - License: None

