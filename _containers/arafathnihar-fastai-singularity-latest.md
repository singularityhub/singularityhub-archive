---
id: 12182
name: "arafathnihar/fastai-singularity"
branch: "master"
tag: "latest"
commit: "7841ba2f9bb82b587257d0513895f5f879d49e18"
version: "4f9095083f7f631551ba1af6361d8434"
build_date: "2020-07-26T23:06:56.583Z"
size_mb: 3110.0
size: 1976098847
sif: "https://datasets.datalad.org/shub/arafathnihar/fastai-singularity/latest/2020-07-26-7841ba2f-4f909508/4f9095083f7f631551ba1af6361d8434.sif"
url: https://datasets.datalad.org/shub/arafathnihar/fastai-singularity/latest/2020-07-26-7841ba2f-4f909508/
recipe: https://datasets.datalad.org/shub/arafathnihar/fastai-singularity/latest/2020-07-26-7841ba2f-4f909508/Singularity
collection: arafathnihar/fastai-singularity
---

# arafathnihar/fastai-singularity:latest

```bash
$ singularity pull shub://arafathnihar/fastai-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:10.2-base-ubuntu18.04

%post
    apt-get update -y
    apt-get upgrade -y
    apt-get dist-upgrade -y
    apt-get install -y --no-install-recommends git gcc python3 python3-dev python3-setuptools python3-wheel python3-pip 
    pip3 install fastai jupyter notebook jupyter_contrib_nbextensions

    #clean up
    apt --purge autoremove -y
    apt clean
    rm -rf /var/lib/apt/lists/*

%runscript
    echo "Open a terminal in your machine and type the following command to port forward"
    echo "ssh -N -L 9999:$(hostname -i):9999 $(id -un)@rider.case.edu"

    FOLDER="course-v3"
    URL="https://github.com/fastai/course-v3.git"
    if [ ! -d "$FOLDER" ] ; then
        git clone $URL $FOLDER
    fi
    cd course-v3/nbs
    jupyter notebook --no-browser --ip=$(hostname -i) --port=9999

%help
    Please follow the steps :
        sudo singularity build fastai.sif fastai.def
        singularity run --nv fastai.sif
```

## Collection

 - Name: [arafathnihar/fastai-singularity](https://github.com/arafathnihar/fastai-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

