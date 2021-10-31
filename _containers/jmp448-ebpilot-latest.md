---
id: 13412
name: "jmp448/ebpilot"
branch: "master"
tag: "latest"
commit: "1c1a9ed89ea1c5855c5572266cc0d90e9897793f"
version: "89a1f2e0262cc83756e845286ba9f1f1"
build_date: "2020-06-23T17:12:08.222Z"
size_mb: 1750.0
size: 753381407
sif: "https://datasets.datalad.org/shub/jmp448/ebpilot/latest/2020-06-23-1c1a9ed8-89a1f2e0/89a1f2e0262cc83756e845286ba9f1f1.sif"
url: https://datasets.datalad.org/shub/jmp448/ebpilot/latest/2020-06-23-1c1a9ed8-89a1f2e0/
recipe: https://datasets.datalad.org/shub/jmp448/ebpilot/latest/2020-06-23-1c1a9ed8-89a1f2e0/Singularity
collection: jmp448/ebpilot
---

# jmp448/ebpilot:latest

```bash
$ singularity pull shub://jmp448/ebpilot:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.13.2-py3-jupyter

%environment
  # use bash as default shell
  SHELL=/bin/bash
  export SHELL

%setup
  # runs on host - the path to the image is $SINGULARITY_ROOTFS

%post
  # post-setup script

  # load environment variables
  . /environment

  # use bash as default shell
  echo 'SHELL=/bin/bash' >> /environment

  # make environment file executable
  chmod +x /environment

  # default mount paths
  mkdir /data 

  # additional packages
  apt-get update
  apt-get install -y python-tk
  apt-get install -y libsm6 libxext6
  pip install selenium
  pip install moviepy
  pip install lmdb
  pip install opencv-contrib-python
  pip install cryptography
  
  pip install gpflow==1.3.0

%runscript
  # executes with the singularity run command
  # delete this section to use existing docker ENTRYPOINT command

%test
  # test that script is a success
```

## Collection

 - Name: [jmp448/ebpilot](https://github.com/jmp448/ebpilot)
 - License: None

