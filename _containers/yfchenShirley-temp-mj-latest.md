---
id: 15656
name: "yfchenShirley/temp-mj"
branch: "master"
tag: "latest"
commit: "174cbb034732376527422ffe25dc931ebf67a99d"
version: "f3ecd7adcefe4db37feaa512482aba6b"
build_date: "2021-03-10T15:42:53.682Z"
size_mb: 4964.0
size: 2356154399
sif: "https://datasets.datalad.org/shub/yfchenShirley/temp-mj/latest/2021-03-10-174cbb03-f3ecd7ad/f3ecd7adcefe4db37feaa512482aba6b.sif"
url: https://datasets.datalad.org/shub/yfchenShirley/temp-mj/latest/2021-03-10-174cbb03-f3ecd7ad/
recipe: https://datasets.datalad.org/shub/yfchenShirley/temp-mj/latest/2021-03-10-174cbb03-f3ecd7ad/Singularity
collection: yfchenShirley/temp-mj
---

# yfchenShirley/temp-mj:latest

```bash
$ singularity pull shub://yfchenShirley/temp-mj:latest
```

## Singularity Recipe

```singularity
#This is a dockerfile that sets up a full Gym install with test dependencies
Bootstrap: docker

# Here we ll build our container upon the tensorflow container
From: tensorflow/tensorflow:latest-gpu-py3

# Now we'll copy the mjkey file located in the current directory inside the container's root
# directory
%files
        mjkey.txt

# Then we put everything we need to install
%post
        apt -y update && \
        apt install -y keyboard-configuration && \
        apt install -y \
        python3-setuptools \
        python3-dev \
        python3.6-tk \
        python-pyglet \
        python3-opengl \
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

        # Download Gym and Mujoco
        mkdir /Gym && cd /Gym
        git clone https://github.com/openai/gym.git || true && \
        mkdir /Gym/.mujoco && cd /Gym/.mujoco
        wget https://www.roboti.us/download/mujoco200_linux.zip && \
        unzip mujoco200_linux.zip && \
        mv mujoco200_linux mujoco200
        rm mujoco200_linux.zip

        # Export global environment variables
        export MUJOCO_PY_MJKEY_PATH=/Gym/.mujoco/mjkey.txt
        export MUJOCO_PY_MUJOCO_PATH=/Gym/.mujoco/mujoco200/
        #export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mjpro150/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mujoco200/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/bin
        cp /mjkey.txt /Gym/.mujoco/mjkey.txt

        # Install python dependencies
        wget https://raw.githubusercontent.com/openai/mujoco-py/master/requirements.txt
        pip install --upgrade pip
        pip install lockfile
        pip install --no-cache-dir -r requirements.txt
        wget https://raw.githubusercontent.com/openai/mujoco-py/master/requirements.dev.txt
        pip install --no-cache-dir -r requirements.dev.txt
        git clone https://github.com/openai/mujoco-py.git
        cd mujoco-py/
        echo 'mujoco-py<2.1,>=2.0' >> requirements.txt
        python3 setup.py install
        # Install Gym and Mujoco
        cd /Gym/gym
        pip install gym
        # Change permission to use mujoco_py as non sudoer user
        #which python
        #chmod -R 777 /usr/local/lib/python3.6/dist-packages/mujoco_py/

        # Then install miniworld
        #cd /usr/local/
        #git clone https://github.com/maximecb/gym-miniworld.git
        #cd gym-miniworld
        #pip install -e .

# Export global environment variables
%environment
        export SHELL=/bin/bash
        export MUJOCO_PY_MJKEY_PATH=/Gym/.mujoco/mjkey.txt
        export MUJOCO_PY_MUJOCO_PATH=/Gym/.mujoco/mujoco200/
        #export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mjpro150/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mujoco200/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/bin
        export PATH=/Gym/gym/.tox/py3/bin:$PATH

%runscript
        exec /bin/bash "$@"
```

## Collection

 - Name: [yfchenShirley/temp-mj](https://github.com/yfchenShirley/temp-mj)
 - License: None

