---
id: 11921
name: "d-bohn/openpose_aci"
branch: "gpu"
tag: "gpu"
commit: "1ab69b7e10e4021b7c5978a25047402920d40eac"
version: "0d380a7fd661f483f3ede455be1d05dcdf48ad8866ef9e2b8d26ec97ae63d0e0"
build_date: "2021-04-14T18:12:39.106Z"
size_mb: 2628.33984375
size: 2756014080
sif: "https://datasets.datalad.org/shub/d-bohn/openpose_aci/gpu/2021-04-14-1ab69b7e-0d380a7f/0d380a7fd661f483f3ede455be1d05dcdf48ad8866ef9e2b8d26ec97ae63d0e0.sif"
url: https://datasets.datalad.org/shub/d-bohn/openpose_aci/gpu/2021-04-14-1ab69b7e-0d380a7f/
recipe: https://datasets.datalad.org/shub/d-bohn/openpose_aci/gpu/2021-04-14-1ab69b7e-0d380a7f/Singularity
collection: d-bohn/openpose_aci
---

# d-bohn/openpose_aci:gpu

```bash
$ singularity pull shub://d-bohn/openpose_aci:gpu
```

## Singularity Recipe

```singularity
BootStrap: docker
From: exsidius/openpose

%runscript
    cd /openpose
    exec /build/examples/openpose/openpose.bin "$@"
%environment

%post
    # apt-get update --fix-missing
    # apt-get install software-properties-common
    # apt-get update
    
    #need to install correct gpu drivers
    # install nvidia driver (current system version: 390.30)
    # add-apt-repository ppa:graphics-drivers
    # apt-get update --fix-missing
    # apt-get install -y nvidia-390-dev

    #------------------------------------------------------------------------------
    # Create local binding points for our ICS-ACI
    #------------------------------------------------------------------------------
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
```

## Collection

 - Name: [d-bohn/openpose_aci](https://github.com/d-bohn/openpose_aci)
 - License: None

