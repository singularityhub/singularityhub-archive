---
id: 10291
name: "mweiss17/SEVN"
branch: "master"
tag: "latest"
commit: "765e3527213ad111352f94e6c38c5154f311fbce"
version: "03ba29fa4b0e54c06f4aee023ab141cae39de7604a2d73ecd54fd9120c5ab636"
build_date: "2019-09-28T23:28:27.185Z"
size_mb: 3196.4921875
size: 3351764992
sif: "https://datasets.datalad.org/shub/mweiss17/SEVN/latest/2019-09-28-765e3527-03ba29fa/03ba29fa4b0e54c06f4aee023ab141cae39de7604a2d73ecd54fd9120c5ab636.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/mweiss17/SEVN/latest/2019-09-28-765e3527-03ba29fa/
recipe: https://datasets.datalad.org/shub/mweiss17/SEVN/latest/2019-09-28-765e3527-03ba29fa/Singularity
collection: mweiss17/SEVN
---

# mweiss17/SEVN:latest

```bash
$ singularity pull shub://mweiss17/SEVN:latest
```

## Singularity Recipe

```singularity
#This is a dockerfile that sets up a full SEVN install
Bootstrap: docker

# Here we ll build our container upon the ubuntu container
From: ubuntu:18.04

# Export global environment variables
%environment
        export PYTHONPATH="/usr/local/:$PYTHONPATH"
        export SHELL=/bin/bash
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/bin
        export PATH=/gym/.tox/py3/bin:$PATH

# Then we put everything we need to install
%post
        apt -y update && \
        apt -y upgrade && \
        apt install -y \
        python3-setuptools \
        python3-dev \
        python3-opengl \
        python3-pip \
        libjpeg-dev \
        libboost-all-dev \
        libsdl2-dev \
        libosmesa6-dev \
        patchelf \
        ffmpeg \
        xvfb \
        wget \
        git \
        unzip && \
        apt clean && \
        rm -rf /var/lib/apt/lists/*

        # export env vars
        . /environment

        # create default mount points
        echo "Creating mount points"
        mkdir /scratch
        mkdir /data
        mkdir /dataset
        mkdir /tmp_log
        mkdir /final_log

	
        pip3 install ipdb tensorflow torch==1.2
        cd scratch/

        # Download Gym
        git clone https://github.com/openai/gym.git || true && \
        cd gym
        pip3 install -e .
        cd ..

        # install SEVN and dependencies
        git clone https://github.com/openai/baselines.git
        cd baselines
        pip3 install -e .
        cd ..
        git clone https://github.com/mweiss17/SEVN.git
        cd SEVN
        pip3 install -e .
        cd ..
        git clone https://github.com/simonchamorro/NAVI-STR
        cd NAVI-STR
        pip3 install -e .
        cd ..
        mv NAVI-STR NAVI_STR

        # Install pytorch-a2c-ppo-acktr
        git clone https://github.com/simonchamorro/pytorch-a2c-ppo-acktr-gail.git
        cd pytorch-a2c-ppo-acktr-gail
        mkdir trained_models/
        mkdir trained_models/ppo/
	pip3 install -e .

%runscript
        exec /bin/bash "$@"
```

## Collection

 - Name: [mweiss17/SEVN](https://github.com/mweiss17/SEVN)
 - License: None

