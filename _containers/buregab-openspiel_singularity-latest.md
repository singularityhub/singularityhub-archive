---
id: 14646
name: "buregab/openspiel_singularity"
branch: "master"
tag: "latest"
commit: "83ab187e4dfa0d30c16d1b24da8ae20f79cddf0a"
version: "a0bc00cb7542f4604d5f9485cf78019c"
build_date: "2020-10-30T21:14:32.786Z"
size_mb: 7694.0
size: 2230251551
sif: "https://datasets.datalad.org/shub/buregab/openspiel_singularity/latest/2020-10-30-83ab187e-a0bc00cb/a0bc00cb7542f4604d5f9485cf78019c.sif"
url: https://datasets.datalad.org/shub/buregab/openspiel_singularity/latest/2020-10-30-83ab187e-a0bc00cb/
recipe: https://datasets.datalad.org/shub/buregab/openspiel_singularity/latest/2020-10-30-83ab187e-a0bc00cb/Singularity
collection: buregab/openspiel_singularity
---

# buregab/openspiel_singularity:latest

```bash
$ singularity pull shub://buregab/openspiel_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%environment
    export PATH="/usr/local/miniconda3/bin:$PATH"
    export PYTHONPATH=$PYTHONPATH:/usr/local/open_spiel
    export PYTHONPATH=$PYTHONPATH:/usr/local/open_spiel/build/python

%post
    apt-get -y update
    apt-get -y install wget bzip2 parallel xvfb ffmpeg xorg-dev libsdl2-dev cmake unzip syslog-ng-core vsftpd git
    DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

    # Installing miniconda
    # wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    # bash Miniconda3-latest-Linux-x86_64.sh -b -p /usr/local/miniconda3
    # rm Miniconda3-latest-Linux-x86_64.sh

    ##### INSTALL THE DEPENDENCIES YOU NEED HERE #####

    ##################################################

    cd /usr/local
    git clone https://github.com/deepmind/open_spiel.git
    cd open_spiel
    yes | apt-get install sudo -y

    yes | ./install.sh -y
    yes | pip3 install --upgrade pip
    yes | pip3 install -r requirements.txt
    yes | pip3 install --upgrade cmake
    yes | pip3 install wandb
    yes | pip3 install jupyter
    yes | ./open_spiel/scripts/build_and_run_tests.sh
```

## Collection

 - Name: [buregab/openspiel_singularity](https://github.com/buregab/openspiel_singularity)
 - License: None

