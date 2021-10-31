---
id: 1157
name: "expfactory/expfactory-robots"
branch: "master"
tag: "latest"
commit: "2875e4ebecdd06a51753f42dca96bc98f514f08e"
version: "5845289eece103e00c2a51e50b3f54c8"
build_date: "2018-09-06T00:24:38.690Z"
size_mb: 980
size: 400375839
sif: "https://datasets.datalad.org/shub/expfactory/expfactory-robots/latest/2018-09-06-2875e4eb-5845289e/5845289eece103e00c2a51e50b3f54c8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/expfactory/expfactory-robots/latest/2018-09-06-2875e4eb-5845289e/
recipe: https://datasets.datalad.org/shub/expfactory/expfactory-robots/latest/2018-09-06-2875e4eb-5845289e/Singularity
collection: expfactory/expfactory-robots
---

# expfactory/expfactory-robots:latest

```bash
$ singularity pull shub://expfactory/expfactory-robots:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

# sudo singularity build expfactory-robots.simg Singularity

%setup
    mkdir -p ${SINGULARITY_ROOTFS}/code
    mkdir -p ${SINGULARITY_ROOTFS}/data

%files
. /code

%labels
    MAINTAINER vsochat@stanford.edu

%post
    apt-get update && apt-get install -y git wget python3-pip \
                   python3-dev xvfb libfontconfig fonts-liberation \
                   gconf-service libappindicator1 libasound2 libnspr4 \
                   libnss3 libxss1 lsb-release xdg-utils
    cd /opt && git clone https://www.github.com/expfactory/expfactory
    wget "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
    cd /opt/expfactory && python3 setup.py install
    python3 -m pip install selenium pyvirtualdisplay

    cd /opt && dpkg -i google-chrome-stable_current_amd64.deb
    apt-get -f install
    apt-get install -y -f
    rm google-chrome-stable_current_amd64.deb

    cd /code && chmod u+x /code/start.py

%runscript
    exec python3 /code/start.py "$@"
```

## Collection

 - Name: [expfactory/expfactory-robots](https://github.com/expfactory/expfactory-robots)
 - License: [Mozilla Public License 2.0](https://api.github.com/licenses/mpl-2.0)

