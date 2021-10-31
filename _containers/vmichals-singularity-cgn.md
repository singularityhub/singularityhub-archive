---
id: 7459
name: "vmichals/singularity"
branch: "master"
tag: "cgn"
commit: "0526a72be22466c3413e13c54f8e73128e72018b"
version: "6eba3375d5b8d1f24c1f9a915945559f"
build_date: "2019-07-18T17:12:50.557Z"
size_mb: 2336
size: 1071136799
sif: "https://datasets.datalad.org/shub/vmichals/singularity/cgn/2019-07-18-0526a72b-6eba3375/6eba3375d5b8d1f24c1f9a915945559f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/vmichals/singularity/cgn/2019-07-18-0526a72b-6eba3375/
recipe: https://datasets.datalad.org/shub/vmichals/singularity/cgn/2019-07-18-0526a72b-6eba3375/Singularity
collection: vmichals/singularity
---

# vmichals/singularity:cgn

```bash
$ singularity pull shub://vmichals/singularity:cgn
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%post
    apt -y update
    apt -y upgrade
    apt -y install software-properties-common
    apt -y install vim unzip wget sudo
    apt -y install build-essential libssl-dev libffi-dev python3-dev
    apt -y install libsm6
    apt -y install python3-pip python3-tk
    apt -y install git
    pip3 install --no-cache-dir numpy opencv-python Pillow
    pip3 install --no-cache-dir torch torchvision matplotlib ipython ipdb
    pip3 install --no-cache-dir scikit-learn scikit-image
    pip3 install --no-cache-dir sklearn pandas tqdm imageio
    pip3 install --no-cache-dir pandas retrying tables h5py
    pip3 install --no-cache-dir torchsummary tensorboardX gitpython dnspython
    pip3 install --no-cache-dir git+https://github.com/epistimio/orion.git@develop


%environment

%runscript
```

## Collection

 - Name: [vmichals/singularity](https://github.com/vmichals/singularity)
 - License: None

