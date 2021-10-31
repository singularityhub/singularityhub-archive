---
id: 15655
name: "yfchenShirley/Mjtf-test"
branch: "master"
tag: "latest"
commit: "b627d6c1a92f906c42ef6f51be3b1f98073c0eaf"
version: "362cab23d116966f2992d557f0637c74"
build_date: "2021-03-10T11:54:44.493Z"
size_mb: 4850.0
size: 2331738143
sif: "https://datasets.datalad.org/shub/yfchenShirley/Mjtf-test/latest/2021-03-10-b627d6c1-362cab23/362cab23d116966f2992d557f0637c74.sif"
url: https://datasets.datalad.org/shub/yfchenShirley/Mjtf-test/latest/2021-03-10-b627d6c1-362cab23/
recipe: https://datasets.datalad.org/shub/yfchenShirley/Mjtf-test/latest/2021-03-10-b627d6c1-362cab23/Singularity
collection: yfchenShirley/Mjtf-test
---

# yfchenShirley/Mjtf-test:latest

```bash
$ singularity pull shub://yfchenShirley/Mjtf-test:latest
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
        wget https://www.roboti.us/download/mjpro150_linux.zip  && \
        unzip mjpro150_linux.zip && \
        wget https://www.roboti.us/download/mujoco200_linux.zip && \
        unzip mujoco200_linux.zip && \
        mv mujoco200_linux mujoco200

        # Export global environment variables
        export MUJOCO_PY_MJKEY_PATH=/Gym/.mujoco/mjkey.txt
        export MUJOCO_PY_MUJOCO_PATH=/Gym/.mujoco/mujoco150/
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mjpro150/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mujoco200/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/bin
        cp /mjkey.txt /Gym/.mujoco/mjkey.txt

        # Install python dependencies
        wget https://raw.githubusercontent.com/openai/mujoco-py/master/requirements.txt
        pip install --upgrade pip
        pip install lockfile
        pip install -r requirements.txt
        # Install Gym and Mujoco
        cd /Gym/gym
        pip install gym
        # Change permission to use mujoco_py as non sudoer user
        #which python
        #chmod -R 777 /home/p285442/.mujoco/mujoco_py/

        # Then install miniworld
        #cd /usr/local/
        #git clone https://github.com/maximecb/gym-miniworld.git
        #cd gym-miniworld
        #pip install -e .

# Export global environment variables
%environment
        export SHELL=/bin/bash
        export MUJOCO_PY_MJKEY_PATH=/Gym/.mujoco/mjkey.txt
        export MUJOCO_PY_MUJOCO_PATH=/Gym/.mujoco/mujoco150/
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mjpro150/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mujoco200/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/bin
        export PATH=/Gym/gym/.tox/py3/bin:$PATH

%runscript
        exec /bin/bash "$@"
```

## Collection

 - Name: [yfchenShirley/Mjtf-test](https://github.com/yfchenShirley/Mjtf-test)
 - License: None

