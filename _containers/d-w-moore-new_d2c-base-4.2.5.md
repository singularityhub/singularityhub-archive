---
id: 7957
name: "d-w-moore/new_d2c"
branch: "master"
tag: "base-4.2.5"
commit: "dceaa16a21385542d9bde63e9c19524e06d4e9c7"
version: "8e40d25be78eb614ab3b2354459330a9"
build_date: "2019-03-27T08:48:37.842Z"
size_mb: 761
size: 333639711
sif: "https://datasets.datalad.org/shub/d-w-moore/new_d2c/base-4.2.5/2019-03-27-dceaa16a-8e40d25b/8e40d25be78eb614ab3b2354459330a9.simg"
url: https://datasets.datalad.org/shub/d-w-moore/new_d2c/base-4.2.5/2019-03-27-dceaa16a-8e40d25b/
recipe: https://datasets.datalad.org/shub/d-w-moore/new_d2c/base-4.2.5/2019-03-27-dceaa16a-8e40d25b/Singularity
collection: d-w-moore/new_d2c
---

# d-w-moore/new_d2c:base-4.2.5

```bash
$ singularity pull shub://d-w-moore/new_d2c:base-4.2.5
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%post
  export IRODS_VERSION=4.2.5
  apt-get update
  apt-get install -y \
    wget \
    sudo \
    apt-transport-https
  wget -qO - https://packages.irods.org/irods-signing-key.asc | \
    sudo apt-key add -
  echo "deb [arch=amd64] https://packages.irods.org/apt/ xenial main" | \
    sudo tee /etc/apt/sources.list.d/renci-irods.list
  apt-get update
  apt-get install -y \
    irods-icommands=${IRODS_VERSION} \
    libxml2
  apt-get install -y python curl gcc autoconf python-dev libgmp3-dev
  curl https://bootstrap.pypa.io/get-pip.py | python
  pip install python-irodsclient
  wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
  chmod +x jq-linux64
```

## Collection

 - Name: [d-w-moore/new_d2c](https://github.com/d-w-moore/new_d2c)
 - License: None

