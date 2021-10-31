---
id: 14656
name: "fenz-org/tensorflow"
branch: "master"
tag: "2.1.0-c_anaconda-python-3.7"
commit: "d555787ebafad6beb8d7bcc2100957c0f427e943"
version: "3a2f40385e3e698946a9ade363053dbc94dcadf545508d209bbb53595518a08a"
build_date: "2020-10-24T14:46:31.793Z"
size_mb: 1088.4296875
size: 1141301248
sif: "https://datasets.datalad.org/shub/fenz-org/tensorflow/2.1.0-c_anaconda-python-3.7/2020-10-24-d555787e-3a2f4038/3a2f40385e3e698946a9ade363053dbc94dcadf545508d209bbb53595518a08a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/fenz-org/tensorflow/2.1.0-c_anaconda-python-3.7/2020-10-24-d555787e-3a2f4038/
recipe: https://datasets.datalad.org/shub/fenz-org/tensorflow/2.1.0-c_anaconda-python-3.7/2020-10-24-d555787e-3a2f4038/Singularity
collection: fenz-org/tensorflow
---

# fenz-org/tensorflow:2.1.0-c_anaconda-python-3.7

```bash
$ singularity pull shub://fenz-org/tensorflow:2.1.0-c_anaconda-python-3.7
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.8.2

%post
    export PATH="/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    export PYTHON_VERSION=3.7
    export TENSORFLOW_VERSION=2.1.0
    export CONDA_VERSION=4.8.2
    export CONDA_CHANNEL=anaconda
    export CONDA_PROFILE=base

    echo "conda ${CONDA_VERSION}" >> /opt/conda/conda-meta/pinned
    conda config --system --prepend channels ${CONDA_CHANNEL}
    conda config --system --set auto_update_conda false
    conda config --system --set show_channel_urls true
    conda clean --all -f -y
    conda install -y -c ${CONDA_CHANNEL} \
        scipy=1.4.1 \
        tensorboard=2.1.0 \
        tensorflow=${TENSORFLOW_VERSION}

%environment
    export PATH="/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    export PYTHON_VERSION=3.7
    export USE_DAAL4PY_SKLEARN=YES
    export CONDA_PROFILE=base
    . /opt/conda/etc/profile.d/conda.sh
    conda activate $CONDA_PROFILE
```

## Collection

 - Name: [fenz-org/tensorflow](https://github.com/fenz-org/tensorflow)
 - License: None

