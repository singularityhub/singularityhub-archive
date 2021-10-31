---
id: 15166
name: "vmichals/ODE-RL"
branch: "main"
tag: "latest"
commit: "47e14b6f72149ac8ce288581b0ba27a0f0b3bdd4"
version: "6dd5584798909150673a26da442d6f31"
build_date: "2020-12-24T06:06:57.609Z"
size_mb: 7157.0
size: 2995826719
sif: "https://datasets.datalad.org/shub/vmichals/ODE-RL/latest/2020-12-24-47e14b6f-6dd55847/6dd5584798909150673a26da442d6f31.sif"
url: https://datasets.datalad.org/shub/vmichals/ODE-RL/latest/2020-12-24-47e14b6f-6dd55847/
recipe: https://datasets.datalad.org/shub/vmichals/ODE-RL/latest/2020-12-24-47e14b6f-6dd55847/Singularity
collection: vmichals/ODE-RL
---

# vmichals/ODE-RL:latest

```bash
$ singularity pull shub://vmichals/ODE-RL:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

# Now we'll copy the mjkey file located in the current directory inside the container's root
# directory
#%files
#
#    mjkey.txt mjkey.txt

%post

    apt -y update
    apt -y upgrade

    # create mount point for host dir containing mjkey.txt (we don't want to rebuild the image when key is renewed)
 #   mkdir /licenses

    DEBIAN_FRONTEND=noninteractive apt install -y keyboard-configuration \
    build-essential libffi-dev libssl-dev libhdf5-dev \
    libjpeg-dev libboost-all-dev libsdl2-dev libsm6 \
    libosmesa6-dev libglew2.0 libglfw3 patchelf xvfb \
    libhdf5-dev openjdk-8-jdk rsync git vim sudo \
    software-properties-common wget unzip locales
    
    apt clean
    rm -rf /var/lib/apt/lists/*

    sudo echo "LC_ALL=en_US.UTF-8" >> /etc/environment
    sudo echo "LANG=en_US.UTF-8" > /etc/locale.conf
    sudo echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
    sudo locale-gen && sudo update-locale LANG=en_US.UTF-8

    # install miniconda
    if [ ! -d /opt/conda ]; then
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
        bash ~/miniconda.sh -b -p /opt/conda
        rm ~/miniconda.sh
    fi
    # set conda path
    export PATH="/opt/conda/bin:$PATH"

    conda install python==3.6.9
    conda install h5py ipython matplotlib numpy plotly=4.0.0 tqdm pip opencv 
    conda install ipdb gitpython moviepy -c conda-forge
    conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
    #conda install imageio==2.4.1
    conda install imageio
    conda install tensorboard 
    conda install scikit-learn
    pip install --no-cache-dir pygame notebook
    # install hydra for configuration
    pip install --no-cache-dir hydra-core --upgrade
    pip install --no-cache-dir phyre
    pip install --no-cache-dir torchdiffeq
    pip install --no-cache-dir tensorflow

    # Download Gym and Mujoco
    mkdir /Gym && cd /Gym
    # git clone https://github.com/openai/gym.git || true && \
    #mkdir /Gym/.mujoco && cd /Gym/.mujoco
    #wget https://www.roboti.us/download/mjpro150_linux.zip  && \
    #unzip mjpro150_linux.zip && \
    #wget https://www.roboti.us/download/mujoco200_linux.zip && \
    #unzip mujoco200_linux.zip && \
    #mv mujoco200_linux mujoco200

    # Export global environment variables
    #export MUJOCO_PY_MJKEY_PATH=/Gym/.mujoco/mjkey.txt
    #export MUJOCO_PY_MUJOCO_PATH=/Gym/.mujoco/mujoco200/
    #export MUJOCO_PY_MJPRO_PATH=/Gym/.mujoco/mjpro150/
    #export MJKEY_PATH=/Gym/.mujoco/mjkey.txt
    ##export MJLIB_PATH=/Gym/.mujoco/mjpro150/bin
    #export MJLIB_PATH=/Gym/.mujoco/mujoco200/bin/libmujoco200.so #:$MJLIB_PATH
    #export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mjpro150/bin
    #export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mujoco200/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/bin
    #cp /mjkey.txt /Gym/.mujoco/mjkey.txt
    # Install python dependencies
    #wget https://raw.githubusercontent.com/openai/mujoco-py/master/requirements.txt
    #echo "installing python dependencies of mujoco_py"
    #pip install --no-cache-dir -r requirements.txt
    # Install Gym and Mujoco
    #echo "installing gym and mujoco_py"
    echo "installing gym"
    #cd /Gym/gym
    #pip install --no-cache-dir -e '.[classic_control]'
    pip install --no-cache-dir gym
    pip install --no-cache-dir gym[box2d]
    pip install --no-cache-dir gym[classic_control]
    # Change permission to use mujoco_py as non sudoer user
    #chmod -R 777 /opt/conda/lib/python3.6/site-packages/mujoco_py/
    #pip install --no-cache-dir --upgrade minerl

    # install deepmind control suite (workaround enum34 issues)
    #git clone git://github.com/deepmind/dm_env.git
    #sed -i '/enum34/d' dm_env/requirements.txt
    #git clone git://github.com/deepmind/dm_control.git
    #sed -i '/enum34/d' dm_control/requirements.txt

    # workaround for pip sending --install-options to dependencies and errors 
    # halting the recipe build:
    # 1) let pip install all dependencies and error out on setup of dm_control 
    #    because of incorrect default headers-dir.
    # 2) use || to execute pip install w/o dependencies and correct headers-dir
    #    after the failure.
    #pip install --no-cache-dir ./dm_control \
    #|| pip install --no-cache-dir --no-deps --upgrade \
    #--install-option="--headers-dir=/Gym/.mujoco/mujoco200/include" ./dm_control

    # install orion for hyperparameter tuning
    #pip install --no-cache-dir git+https://github.com/epistimio/orion.git@develop

    # debugging tools
    #pip install --no-cache-dir pydevd pudb

    # osim-rl
    #conda install -c kidzik opensim
    #pip install --no-cache-dir git+https://github.com/stanfordnmbl/osim-rl.git

    conda clean --all -y

    # delete key and instead create symlink to key in bound license directory
    #rm /Gym/.mujoco/mjkey.txt
    #ln -s /licenses/mjkey.txt /Gym/.mujoco/mjkey.txt

# Export global environment variables
%environment
    export LC_ALL=en_US.utf8
    export PATH=/opt/conda/bin:$PATH
    export SHELL=/bin/sh
    #export MUJOCO_PY_MJKEY_PATH=/Gym/.mujoco/mjkey.txt
    #export MUJOCO_PY_MUJOCO_PATH=/Gym/.mujoco/mujoco200/
    #export MUJOCO_PY_MJPRO_PATH=/Gym/.mujoco/mjpro150/
    #export MJKEY_PATH=/Gym/.mujoco/mjkey.txt
    #export MJLIB_PATH=/Gym/.mujoco/mjpro150/bin
    #export MJLIB_PATH=/Gym/.mujoco/mujoco200/bin/libmujoco200.so #:$MJLIB_PATH
    #export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mjpro150/bin
    #export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/Gym/.mujoco/mujoco200/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/bin
    export PATH=/Gym/gym/.tox/py3/bin:$PATH

%runscript
    exec /bin/sh "$@"
```

## Collection

 - Name: [vmichals/ODE-RL](https://github.com/vmichals/ODE-RL)
 - License: None

