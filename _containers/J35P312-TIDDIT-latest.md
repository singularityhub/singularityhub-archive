---
id: 9223
name: "J35P312/TIDDIT"
branch: "master"
tag: "latest"
commit: "d6751b416f418f247855643d87b1bc5292dabf05"
version: "0e7cd5ce2a9f780934213d7a68290509"
build_date: "2021-04-01T06:26:49.686Z"
size_mb: 1145.0
size: 602443807
sif: "https://datasets.datalad.org/shub/J35P312/TIDDIT/latest/2021-04-01-d6751b41-0e7cd5ce/0e7cd5ce2a9f780934213d7a68290509.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/J35P312/TIDDIT/latest/2021-04-01-d6751b41-0e7cd5ce/
recipe: https://datasets.datalad.org/shub/J35P312/TIDDIT/latest/2021-04-01-d6751b41-0e7cd5ce/Singularity
collection: J35P312/TIDDIT
---

# J35P312/TIDDIT:latest

```bash
$ singularity pull shub://J35P312/TIDDIT:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: trusty
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%environment
    SHELL=/bin/bash
    PATH=/opt/anaconda/bin:${PATH}


%runscript
    echo "This is what happens when you run the container..."
    PATH=/opt/anaconda/bin:${PATH}
    echo "This is what happens when you run the container..."

%post
    echo "Hello from inside the container"
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt-get update
    apt-get upgrade
    apt-get -y --force-yes install build-essential cmake make zlib1g-dev python python-dev python-setuptools git wget

    cd /root/ && wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    cd /root/ && chmod 700 ./Miniconda3-latest-Linux-x86_64.sh
    cd /root/ && bash ./Miniconda3-latest-Linux-x86_64.sh -b -p /opt/anaconda/ 

    export PATH=/opt/anaconda/bin:${PATH} 


    pip install numpy cython

    git clone https://github.com/SciLifeLab/TIDDIT.git
    mv TIDDIT/* /bin/
    cd /bin/ && ./INSTALL.sh
    chmod +x /bin/TIDDIT.py
```

## Collection

 - Name: [J35P312/TIDDIT](https://github.com/J35P312/TIDDIT)
 - License: [Other](None)

