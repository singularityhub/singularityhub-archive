---
id: 12806
name: "Wreck-It-Ralph/BA_Singularity"
branch: "master"
tag: "latest"
commit: "fed1aac6b3389539bce8c1c94ca87cbdff5d9682"
version: "5f33ac8e55fe3d2cb9f055e5a7b4bb09"
build_date: "2020-04-27T14:41:27.994Z"
size_mb: 6029.0
size: 3824050207
sif: "https://datasets.datalad.org/shub/Wreck-It-Ralph/BA_Singularity/latest/2020-04-27-fed1aac6-5f33ac8e/5f33ac8e55fe3d2cb9f055e5a7b4bb09.sif"
url: https://datasets.datalad.org/shub/Wreck-It-Ralph/BA_Singularity/latest/2020-04-27-fed1aac6-5f33ac8e/
recipe: https://datasets.datalad.org/shub/Wreck-It-Ralph/BA_Singularity/latest/2020-04-27-fed1aac6-5f33ac8e/Singularity
collection: Wreck-It-Ralph/BA_Singularity
---

# Wreck-It-Ralph/BA_Singularity:latest

```bash
$ singularity pull shub://Wreck-It-Ralph/BA_Singularity:latest
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
    pip3 install numpy torch==1.4.0 matplotlib tensorboard torchvision
```

## Collection

 - Name: [Wreck-It-Ralph/BA_Singularity](https://github.com/Wreck-It-Ralph/BA_Singularity)
 - License: None

