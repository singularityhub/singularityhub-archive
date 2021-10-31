---
id: 5572
name: "xrobin/singularity-robo3t"
branch: "master"
tag: "latest"
commit: "0bc793cbe86b97aa4e1ee1d23d6962be63a86248"
version: "9544ac76edd75f873139eb031b910d6b"
build_date: "2019-05-02T09:38:03.479Z"
size_mb: 456
size: 172957727
sif: "https://datasets.datalad.org/shub/xrobin/singularity-robo3t/latest/2019-05-02-0bc793cb-9544ac76/9544ac76edd75f873139eb031b910d6b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/xrobin/singularity-robo3t/latest/2019-05-02-0bc793cb-9544ac76/
recipe: https://datasets.datalad.org/shub/xrobin/singularity-robo3t/latest/2019-05-02-0bc793cb-9544ac76/Singularity
collection: xrobin/singularity-robo3t
---

# xrobin/singularity-robo3t:latest

```bash
$ singularity pull shub://xrobin/singularity-robo3t:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%post
    # install some system deps
    apt-get -y update
    apt-get -y install wget libgl1 libglib2.0-0 libqt5gui5

    file_string=robo3t-1.3.1-linux-x86_64-7419c406
    wget https://download-test.robomongo.org/linux/$file_string.tar.gz
    tar -xf $file_string.tar.gz
    mkdir -p /opt
    mv $file_string /opt/robo3t-1.3.1-linux-x86_64
    rm $file_string.tar.gz
    
    apt-get -y remove wget
    apt-get -y autoremove
    apt-get clean

%apphelp Robo3T
    "Robo3T version 1.3.1"

%apprun Robo3T
    /opt/robo3t-1.3.1-linux-x86_64/bin/robo3t

%runscript
    exec /opt/robo3t-1.3.1-linux-x86_64/bin/robo3t "$@"
```

## Collection

 - Name: [xrobin/singularity-robo3t](https://github.com/xrobin/singularity-robo3t)
 - License: None

