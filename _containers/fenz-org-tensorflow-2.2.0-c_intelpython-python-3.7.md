---
id: 14655
name: "fenz-org/tensorflow"
branch: "master"
tag: "2.2.0-c_intelpython-python-3.7"
commit: "d555787ebafad6beb8d7bcc2100957c0f427e943"
version: "18a09a54b7a03ab6fb4719766c34547bc34fcfcfb38e12c01407da716fd21659"
build_date: "2020-10-26T22:19:29.014Z"
size_mb: 2266.14453125
size: 2376224768
sif: "https://datasets.datalad.org/shub/fenz-org/tensorflow/2.2.0-c_intelpython-python-3.7/2020-10-26-d555787e-18a09a54/18a09a54b7a03ab6fb4719766c34547bc34fcfcfb38e12c01407da716fd21659.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/fenz-org/tensorflow/2.2.0-c_intelpython-python-3.7/2020-10-26-d555787e-18a09a54/
recipe: https://datasets.datalad.org/shub/fenz-org/tensorflow/2.2.0-c_intelpython-python-3.7/2020-10-26-d555787e-18a09a54/Singularity
collection: fenz-org/tensorflow
---

# fenz-org/tensorflow:2.2.0-c_intelpython-python-3.7

```bash
$ singularity pull shub://fenz-org/tensorflow:2.2.0-c_intelpython-python-3.7
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.8.2

%post
    export PATH="/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    export PYTHON_VERSION=3.7
    export TENSORFLOW_VERSION=2.2.0
    export CONDA_VERSION=4.8.2
    export CONDA_CHANNEL=intel
    export CONDA_PROFILE=IDP

    echo "conda ${CONDA_VERSION}" >> /opt/conda/conda-meta/pinned
    conda config --system --prepend channels ${CONDA_CHANNEL}
    conda config --system --set auto_update_conda false
    conda config --system --set show_channel_urls true
    conda clean --all -f -y
    conda create -y -c ${CONDA_CHANNEL} -n $CONDA_PROFILE \
        python=${PYTHON_VERSION} \
        intelpython3_full \
        tensorflow=${TENSORFLOW_VERSION}

%environment
    export PATH="/opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    export PYTHON_VERSION=3.7
    export USE_DAAL4PY_SKLEARN=YES
    export CONDA_PROFILE=IDP
    . /opt/conda/etc/profile.d/conda.sh
    conda activate $CONDA_PROFILE
```

## Collection

 - Name: [fenz-org/tensorflow](https://github.com/fenz-org/tensorflow)
 - License: None

