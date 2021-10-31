---
id: 14657
name: "fenz-org/tensorflow"
branch: "master"
tag: "2.1.0-c_intel-python-3.7"
commit: "d555787ebafad6beb8d7bcc2100957c0f427e943"
version: "aee2626fa241c49f09ea18db6d7c5ad894e52c6f5d849783d6bbe824dc1fb0cb"
build_date: "2020-10-26T21:58:02.370Z"
size_mb: 1575.30859375
size: 1651830784
sif: "https://datasets.datalad.org/shub/fenz-org/tensorflow/2.1.0-c_intel-python-3.7/2020-10-26-d555787e-aee2626f/aee2626fa241c49f09ea18db6d7c5ad894e52c6f5d849783d6bbe824dc1fb0cb.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/fenz-org/tensorflow/2.1.0-c_intel-python-3.7/2020-10-26-d555787e-aee2626f/
recipe: https://datasets.datalad.org/shub/fenz-org/tensorflow/2.1.0-c_intel-python-3.7/2020-10-26-d555787e-aee2626f/Singularity
collection: fenz-org/tensorflow
---

# fenz-org/tensorflow:2.1.0-c_intel-python-3.7

```bash
$ singularity pull shub://fenz-org/tensorflow:2.1.0-c_intel-python-3.7
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
    export CONDA_CHANNEL=intel
    export CONDA_PROFILE=base

    echo "conda ${CONDA_VERSION}" >> /opt/conda/conda-meta/pinned
    conda config --system --prepend channels ${CONDA_CHANNEL}
    conda config --system --set auto_update_conda false
    conda config --system --set show_channel_urls true
    conda clean --all -f -y
    conda install -y -c ${CONDA_CHANNEL} \
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

