---
id: 11457
name: "cancan233/sc2"
branch: "master"
tag: "latest"
commit: "6f749d46805569cf126b3809f83865c781802fea"
version: "a0bb047a0fdedbd2212d320753fd5c14"
build_date: "2019-11-01T21:33:25.505Z"
size_mb: 8986.0
size: 4566196255
sif: "https://datasets.datalad.org/shub/cancan233/sc2/latest/2019-11-01-6f749d46-a0bb047a/a0bb047a0fdedbd2212d320753fd5c14.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/cancan233/sc2/latest/2019-11-01-6f749d46-a0bb047a/
recipe: https://datasets.datalad.org/shub/cancan233/sc2/latest/2019-11-01-6f749d46-a0bb047a/Singularity
collection: cancan233/sc2
---

# cancan233/sc2:latest

```bash
$ singularity pull shub://cancan233/sc2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
MAINTAINER Cancan

%post

    apt-get -y update && apt-get install -y build-essential

    apt-get install -y apt-utils

    apt-get install -y gfortran

    apt-get install -y libopenblas-base

    apt-get install -y wget

    apt-get install -y ed

    apt-get install -y zip
    apt-get install -y unzip

    #Set correct locale
    apt-get -y update && apt-get install -y locales
    locale-gen en_GB.UTF-8
    export LANG=en_GB.UTF-8
    export LANGUAGE=en_GB.UTF-8
    export LC_ALL=en_GB.UTF-8

    apt-get install -y git-all
    apt-get -y update

    apt-get install -y libgtk2.0-dev

    echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
        wget --quiet https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh -O ~/anaconda.sh && \
        /bin/bash ~/anaconda.sh -b -p /opt/conda && \
        rm ~/anaconda.sh

    export PATH=/opt/conda/bin:$PATH

    # Starcraft II is installed in local, as we need to change the map during training
    #wget --continue  --tries=0 http://blzdistsc2-a.akamaihd.net/Linux/SC2.4.0.2.zip -O /tmp/sc2.zip
    #unzip -P iagreetotheeula /tmp/sc2.zip -d /opt/
    #rm /tmp/sc2.zip

    #wget --continue http://blzdistsc2-a.akamaihd.net/MapPacks/Melee.zip -O /tmp/melee.zip
    #unzip -P iagreetotheeula /tmp/melee.zip -d /opt/StarCraftII/Maps/
    #rm /tmp/melee.zip

    #wget --continue https://github.com/deepmind/pysc2/releases/download/v1.2/mini_games.zip -O /tmp/mini_games.zip
    #unzip /tmp/mini_games.zip -d /opt/StarCraftII/Maps/
    #rm /tmp/mini_games.zip

    #chmod -R 755 /opt/StarCraftII/Maps/
    
    # install pysc2
    /opt/conda/bin/pip install --upgrade https://github.com/deepmind/pysc2/archive/master.zip
    /opt/conda/bin/conda install -y --quiet -c anaconda tensorflow-gpu
    mkdir /nobackup

%environment

    export PATH=/opt/conda/bin:$PATH
    export SC2PATH=/opt/StarCraftII

%runscript
```

## Collection

 - Name: [cancan233/sc2](https://github.com/cancan233/sc2)
 - License: None

