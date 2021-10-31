---
id: 12391
name: "hexmek/container"
branch: "master"
tag: "cat"
commit: "8f707d33436ef69439657f9cc659dfdc8d3c9f6b"
version: "354a4d80fa43181384d4936e6116c5cf"
build_date: "2020-03-08T16:37:35.263Z"
size_mb: 606.0
size: 242745375
sif: "https://datasets.datalad.org/shub/hexmek/container/cat/2020-03-08-8f707d33-354a4d80/354a4d80fa43181384d4936e6116c5cf.sif"
url: https://datasets.datalad.org/shub/hexmek/container/cat/2020-03-08-8f707d33-354a4d80/
recipe: https://datasets.datalad.org/shub/hexmek/container/cat/2020-03-08-8f707d33-354a4d80/Singularity
collection: hexmek/container
---

# hexmek/container:cat

```bash
$ singularity pull shub://hexmek/container:cat
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: testing
MirrorURL: http://httpredir.debian.org/debian


%post
    apt update
    apt upgrade -y
    apt install -y make cmake g++ wget curl  zip python3
    mkdir /opt/CAT
    cd /opt/CAT
    wget -O CAT.zip https://github.com/dutilh/CAT/archive/v5.0.3.zip
    unzip CAT.zip
    mv CAT-5.0.3/* .
    mv CAT_pack/* .

    # diamond
    cd /opt
    wget https://github.com/bbuchfink/diamond/releases/download/v0.9.30/diamond-linux64.tar.gz
    tar xzvf diamond-linux64.tar.gz
    mv diamond /usr/bin/


%environment
    export LC_ALL=C     
    export PATH="/opt/CAT/:$PATH"
```

## Collection

 - Name: [hexmek/container](https://github.com/hexmek/container)
 - License: None

