---
id: 10613
name: "abersailbot/simulator"
branch: "master"
tag: "latest"
commit: "f205da7e976765c9e93f6dbe62acbea9b356f771"
version: "35d8da45e6d2a68f7e7e0ebcc12fb71c"
build_date: "2020-05-03T00:26:02.155Z"
size_mb: 645.0
size: 249413663
sif: "https://datasets.datalad.org/shub/abersailbot/simulator/latest/2020-05-03-f205da7e-35d8da45/35d8da45e6d2a68f7e7e0ebcc12fb71c.sif"
url: https://datasets.datalad.org/shub/abersailbot/simulator/latest/2020-05-03-f205da7e-35d8da45/
recipe: https://datasets.datalad.org/shub/abersailbot/simulator/latest/2020-05-03-f205da7e-35d8da45/Singularity
collection: abersailbot/simulator
---

# abersailbot/simulator:latest

```bash
$ singularity pull shub://abersailbot/simulator:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:18.04

%help
    Container for Sails and Boatd

%labels
    MAINTAINER Colin Sauze

%environment
    #define environment variables here
    
%post  
    apt-get update
    apt-get -y install software-properties-common
    apt-get update
    apt-get install -y libjansson-dev python3-gi-cairo python3-gi gir1.2-gtk-3.0 build-essential python3-pip git pkg-config build-essential libjansson-dev netcat psmisc python3-yaml python3-numpy
    pip3 install python-sailsd python-boatdclient

    cd /opt
    git clone --recursive https://github.com/abersailbot/simulator.git

    #we need boatd from git, but it needs to be in a system path so manually install it
    cd /opt/simulator/boatd
    python3 setup.py install

    #compile sailsd
    cd /opt/simulator/sailsd
    make
    make install
    cd ..

    #change boatdclient to port 2223
    ./set_port.sh

%runscript
    cd /opt/simulator/
    ./run.sh
```

## Collection

 - Name: [abersailbot/simulator](https://github.com/abersailbot/simulator)
 - License: None

