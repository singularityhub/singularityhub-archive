---
id: 13098
name: "wsjeon/singularity-asaf"
branch: "master"
tag: "latest"
commit: "b1f775b9a95d2a005a2e67333449635c8670460a"
version: "2bb334f407b8764627d25105958fe364da04825421a895571ef0abed12600cc6"
build_date: "2020-05-22T18:38:41.695Z"
size_mb: 3939.17578125
size: 4130525184
sif: "https://datasets.datalad.org/shub/wsjeon/singularity-asaf/latest/2020-05-22-b1f775b9-2bb334f4/2bb334f407b8764627d25105958fe364da04825421a895571ef0abed12600cc6.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/wsjeon/singularity-asaf/latest/2020-05-22-b1f775b9-2bb334f4/
recipe: https://datasets.datalad.org/shub/wsjeon/singularity-asaf/latest/2020-05-22-b1f775b9-2bb334f4/Singularity
collection: wsjeon/singularity-asaf
---

# wsjeon/singularity-asaf:latest

```bash
$ singularity pull shub://wsjeon/singularity-asaf:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: pytorch/pytorch:1.5-cuda10.1-cudnn7-devel

%files
        mjkey.txt

%post
        export PATH=$PATH:/opt/conda/bin
        apt -y update && \
        apt install -y keyboard-configuration && \
        apt install -y \
        python3-dev \
        python-pyglet \
        python3-opengl \
        libhdf5-dev \
        libjpeg-dev \
        libboost-all-dev \
        libsdl2-dev \
        libgl1-mesa-dev \
        libgl1-mesa-glx \
        libglew-dev \
        libosmesa6-dev \
        net-tools \
        xpra \
        xserver-xorg-dev \
        patchelf \
        ffmpeg \
        xvfb \
        libhdf5-dev \
        openjdk-8-jdk \
        wget \
        git \
        unzip && \
        apt clean && \
        rm -rf /var/lib/apt/lists/*
        pip install h5py lockfile setuptools

        # Download Mujoco, Mujoco_Py, Alfred.
        cd /
        git clone https://github.com/wsjeon/mujoco-py-1.50.1.68 mujoco-py || true && \
        git clone --branch dev https://github.com/julienroyd/alfred || true && \
        mkdir -p /.mujoco && cd /.mujoco
        wget https://www.roboti.us/download/mjpro150_linux.zip  && \
        unzip mjpro150_linux.zip && \
        wget https://www.roboti.us/download/mujoco200_linux.zip && \
        unzip mujoco200_linux.zip && \
        mv mujoco200_linux mujoco200

        # Export global environment variables
        export MUJOCO_PY_MJKEY_PATH=/mjkey.txt
        export MUJOCO_PY_MJPRO_PATH=/.mujoco/mjpro150/
        export MUJOCO_PY_MUJOCO_PATH=/.mujoco/mujoco200/
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/.mujoco/mjpro150/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/.mujoco/mujoco200/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/bin

        # Install python dependencies
        wget https://raw.githubusercontent.com/openai/mujoco-py/master/requirements.txt
        pip install -r requirements.txt

        # Install Gym, Mujoco, Alfred.
        cd /mujoco-py
        pip install --no-cache-dir -r requirements.txt
        pip install --no-cache-dir -r requirements.dev.txt
        /opt/conda/bin/python setup.py build install
        cd ..
        pip install 'gym[box2d,mujoco]'
        pip install -e /alfred

        # Install additional dependencies.
        pip install wandb readchar nop

        # Initialize mujoco_py
        /opt/conda/bin/python -c 'import mujoco_py'

        # Remove key from container
        rm /mjkey.txt

# Export global environment variables
%environment
        export SHELL=/bin/bash

        # Mujoco
        export MUJOCO_PY_MJKEY_PATH=$HOME/.mujoco/mjkey.txt
        export MUJOCO_PY_MJPRO_PATH=/.mujoco/mjpro150/
        export MUJOCO_PY_MUJOCO_PATH=/.mujoco/mujoco200/
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/.mujoco/mjpro150/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/.mujoco/mujoco200/bin
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/bin

        # Alfred
        export PYTHONPATH=$PYTHONPATH:/alfred

%runscript
        # Alfred
        alias alprep='python -m alfred.prepare_schedule'
        alias allaunch='python -m alfred.launch_schedule'
        alias alclean='python -m alfred.clean_interrupted'
        alias alplot='python -m alfred.make_plot_arrays'
        alias alretrain='python -m alfred.create_retrainbest'
        alias albench='python -m alfred.benchmark'
        alias alsync='python -m alfred.sync_wandb'
        alias alcopy='python -m alfred.copy_config'
        alias alupdate='python -m alfred.update_config_unique'

        exec /bin/bash "$@"
```

## Collection

 - Name: [wsjeon/singularity-asaf](https://github.com/wsjeon/singularity-asaf)
 - License: None

