---
id: 13114
name: "Wreck-It-Ralph/openAI_gym_Singularity"
branch: "master"
tag: "latest"
commit: "2a7d30f66d67d1e5060d7cd78fdba625de61b843"
version: "b0e5f7261edf3342f6377723083670e4"
build_date: "2020-05-23T11:29:09.702Z"
size_mb: 6175.0
size: 3892523039
sif: "https://datasets.datalad.org/shub/Wreck-It-Ralph/openAI_gym_Singularity/latest/2020-05-23-2a7d30f6-b0e5f726/b0e5f7261edf3342f6377723083670e4.sif"
url: https://datasets.datalad.org/shub/Wreck-It-Ralph/openAI_gym_Singularity/latest/2020-05-23-2a7d30f6-b0e5f726/
recipe: https://datasets.datalad.org/shub/Wreck-It-Ralph/openAI_gym_Singularity/latest/2020-05-23-2a7d30f6-b0e5f726/Singularity
collection: Wreck-It-Ralph/openAI_gym_Singularity
---

# Wreck-It-Ralph/openAI_gym_Singularity:latest

```bash
$ singularity pull shub://Wreck-It-Ralph/openAI_gym_Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

%post
    # Downloads the latest package lists (important).
    apt-get update -y
    # Runs apt-get while ensuring that there are no user prompts that would
    # cause the build process to hang.
    # python3-tk is required by matplotlib.
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        python3 \
        python3-tk \
        python3-pip \
        python3-setuptools \
        python3-dev
    # Reduce the size of the image by deleting the package lists we downloaded,
    # which are useless now.
    rm -rf /var/lib/apt/lists/*
    # Install Python modules.
    pip3 install -U wheel --user
    pip3 install numpy torch==1.4.0 matplotlib tensorboard torchvision gym
```

## Collection

 - Name: [Wreck-It-Ralph/openAI_gym_Singularity](https://github.com/Wreck-It-Ralph/openAI_gym_Singularity)
 - License: None

