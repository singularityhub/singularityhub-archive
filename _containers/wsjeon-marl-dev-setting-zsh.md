---
id: 12006
name: "wsjeon/marl-dev-setting"
branch: "master"
tag: "zsh"
commit: "f9f432e41af003ccee32e66a0c0ec05fa20813ac"
version: "4f6d48337ce5c3109375e2e78ee2a278ac05e3cf746b9d16735d923e2fd609f0"
build_date: "2020-01-17T22:11:20.097Z"
size_mb: 3522.0
size: 3536572416
sif: "https://datasets.datalad.org/shub/wsjeon/marl-dev-setting/zsh/2020-01-17-f9f432e4-4f6d4833/4f6d48337ce5c3109375e2e78ee2a278ac05e3cf746b9d16735d923e2fd609f0.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/wsjeon/marl-dev-setting/zsh/2020-01-17-f9f432e4-4f6d4833/
recipe: https://datasets.datalad.org/shub/wsjeon/marl-dev-setting/zsh/2020-01-17-f9f432e4-4f6d4833/Singularity
collection: wsjeon/marl-dev-setting
---

# wsjeon/marl-dev-setting:zsh

```bash
$ singularity pull shub://wsjeon/marl-dev-setting:zsh
```

## Singularity Recipe

```singularity
# Header
Bootstrap: shub
From: wsjeon/singularity-development-setting:zsh

# Section
%post
    # Ray rllib
    apt-get install -y libxrender1
    pip install --progress-bar off psutil
    pip install --progress-bar off -U https://s3-us-west-2.amazonaws.com/ray-wheels/latest/ray-0.8.0.dev2-cp36-cp36m-manylinux1_x86_64.whl
    pip install --progress-bar off requests

    # PyTorch
    pip install --progress-bar off torch
    # pip install --progress-bar off tensorboardX

    # # SMAC
    # git clone https://github.com/oxwhirl/smac.git /SMAC
    # pip install /SMAC

    # # StarCraftII
    # mkdir -p /StarCraftII
    # export SC2PATH=/StarCraftII
    # wget -q -O SC2.zip http://blzdistsc2-a.akamaihd.net/Linux/SC2.4.7.1.zip
    # unzip -P iagreetotheeula SC2.zip
    # rm -rf SC2.zip

    # # SMAC maps
    # mkdir -p $SC2PATH/Maps
    # ln -s /SMAC/smac/env/starcraft2/maps/SMAC_Maps $SC2PATH/Maps

    # # Multi-agent particle environments
    # git clone https://github.com/wsjeon/multiagent-particle-envs.git /MPE
    # cd /MPE
    # pip install --progress-bar off -e .
    
    # # Multi-agent particle environments modified by MAGAIL authors
    # git clone https://github.com/wsjeon/multiagent-particle-envs-v2.git /MPE_v2
    # cd /MPE_v2
    # pip install --progress-bar off -e .
    
    # # Multi-agent particle environments modified by MAAC authors
    # git clone https://github.com/wsjeon/multiagent-particle-envs-maac.git /MPE_MAAC
    # cd /MPE_MAAC
    # pip install --progress-bar off -e .

    # # MADDPG
    # git clone https://github.com/openai/maddpg.git /maddpg
    # cd /maddpg
    # pip install --progress-bar off -e .
    
    # OpenAI Baselines
    git clone https://github.com/openai/baselines.git /baselines
    cd /baselines
    pip install --progress-bar off -e .
    
    # # Multi-agent GAIL
    # git clone https://github.com/wsjeon/multiagent-gail.git /multiagent-gail
    # cd /multiagent-gail
    # pip install --progress-bar off -e .

    # Dependencies
    pip install --progress-bar off opencv-python
    pip install --progress-bar off pandas
    pip install --progress-bar off lz4
    pip install --progress-bar off setproctitle
    pip install --progress-bar off box2d-py
    pip install --progress-bar off click
    pip install --progress-bar off matplotlib
    pip install --progress-bar off seaborn
    pip install --progress-bar off wandb

    mkdir -p /etc/pki/tls/certs
    ln -s /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt

%environment
    export SHELL=/bin/zsh

%runscript
    exec /bin/zsh "$@"
```

## Collection

 - Name: [wsjeon/marl-dev-setting](https://github.com/wsjeon/marl-dev-setting)
 - License: None

