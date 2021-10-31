---
id: 8899
name: "jcreinhold/synthtorch"
branch: "master"
tag: "latest"
commit: "a18de3636c6592839e746cf49dae20d7e5b91aa3"
version: "c08b0605ce0a9aa6a3f579364256d1b1"
build_date: "2021-01-14T21:12:21.898Z"
size_mb: 4980
size: 2861781023
sif: "https://datasets.datalad.org/shub/jcreinhold/synthtorch/latest/2021-01-14-a18de363-c08b0605/c08b0605ce0a9aa6a3f579364256d1b1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jcreinhold/synthtorch/latest/2021-01-14-a18de363-c08b0605/
recipe: https://datasets.datalad.org/shub/jcreinhold/synthtorch/latest/2021-01-14-a18de363-c08b0605/Singularity
collection: jcreinhold/synthtorch
---

# jcreinhold/synthtorch:latest

```bash
$ singularity pull shub://jcreinhold/synthtorch:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%environment

    # use bash as default shell
    SHELL=/bin/bash
    export SHELL

    # add CUDA paths
    CPATH="/usr/local/cuda/include:$CPATH"
    PATH="/usr/local/cuda/bin:$PATH"
    LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"
    CUDA_HOME="/usr/local/cuda"
    export CPATH PATH LD_LIBRARY_PATH CUDA_HOME

    # make conda environment accessible
    PATH=/opt/conda/bin:$PATH
    export PATH

%post

    # load environment variables
    . /environment

    # make environment file executable
    chmod +x /environment

    # default mount paths, files
    mkdir /scratch /data /work-zfs
    touch /usr/bin/nvidia-smi

    # install environment and package
    /opt/conda/bin/conda update -n base conda --yes
    /opt/conda/bin/conda install --override-channels -c pytorch -c defaults numpy=1.15.4 matplotlib pytorch torchvision cudatoolkit=9.0 --yes
    /opt/conda/bin/conda install --override-channels -c conda-forge -c defaults numpy=1.15.4 nibabel scikit-image --yes
    /opt/conda/bin/pip install git+git://github.com/jcreinhold/niftidataset.git
    /opt/conda/bin/pip install git+git://github.com/jcreinhold/synthqc.git
    /opt/conda/bin/pip install git+git://github.com/NVIDIA/apex.git
    /opt/conda/bin/pip install git+git://github.com/jcreinhold/synthtorch.git

%runscript
    exec python $@

%apprun train
    exec nn-train $@

%apprun predict
    exec nn-predict $@
```

## Collection

 - Name: [jcreinhold/synthtorch](https://github.com/jcreinhold/synthtorch)
 - License: [Other](None)

