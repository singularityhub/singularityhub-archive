---
id: 2732
name: "trcook/tf"
branch: "master"
tag: "latest"
commit: "11765a016e4218dfda2877f6b4691fbee2bb9646"
version: "0e2c621a7187f66b115a2cbc277445f8"
build_date: "2020-10-21T15:11:41.451Z"
size_mb: 5834
size: 2745720863
sif: "https://datasets.datalad.org/shub/trcook/tf/latest/2020-10-21-11765a01-0e2c621a/0e2c621a7187f66b115a2cbc277445f8.simg"
url: https://datasets.datalad.org/shub/trcook/tf/latest/2020-10-21-11765a01-0e2c621a/
recipe: https://datasets.datalad.org/shub/trcook/tf/latest/2020-10-21-11765a01-0e2c621a/Singularity
collection: trcook/tf
---

# trcook/tf:latest

```bash
$ singularity pull shub://trcook/tf:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://trcook/tf:base


%runscript
    chk_nvidia_uvm=$(grep nvidia_uvm /proc/modules)


    exec /usr/bin/python3 "$@"

%post
    apt-get install -y python3-tk
    # Install TensorFlow GPU version
    pip3 install --upgrade tensorflow-gpu\
    keras\
    protobuf\
    tensorforce\
    snakemake\
    pandas\
    anytree\
    jinja2\
    ruamel.yaml\
    gym\
```

## Collection

 - Name: [trcook/tf](https://github.com/trcook/tf)
 - License: None

