---
id: 6648
name: "arcsUVA/singularity-scripts"
branch: "master"
tag: "tensorflow-1.4.1-py27"
commit: "11924b108ba513b83aa424b3383ee313e3698f09"
version: "07ddd6f26ba9a040c5f18a061bcdc31b"
build_date: "2019-01-28T22:35:36.569Z"
size_mb: 4600
size: 1915093023
sif: "https://datasets.datalad.org/shub/arcsUVA/singularity-scripts/tensorflow-1.4.1-py27/2019-01-28-11924b10-07ddd6f2/07ddd6f26ba9a040c5f18a061bcdc31b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/arcsUVA/singularity-scripts/tensorflow-1.4.1-py27/2019-01-28-11924b10-07ddd6f2/
recipe: https://datasets.datalad.org/shub/arcsUVA/singularity-scripts/tensorflow-1.4.1-py27/2019-01-28-11924b10-07ddd6f2/Singularity
collection: arcsUVA/singularity-scripts
---

# arcsUVA/singularity-scripts:tensorflow-1.4.1-py27

```bash
$ singularity pull shub://arcsUVA/singularity-scripts:tensorflow-1.4.1-py27
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/anaconda:4.4.0
IncludeCmd: yes

%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this will install all necessary packages and prepare the container
    apt-get -y update --fix-missing
    apt-get -y install \
        build-essential \
        dbus \
        wget \
        git \
        mercurial \
        subversion \
        vim \
        nano \
        cmake \
        bzip2 \
        ca-certificates \
        libglib2.0-0 \
        libxext6 \
        libsm6 \
        libxrender1
    rm /etc/machine-id
    dbus-uuidgen --ensure=/etc/machine-id


    export PATH=/opt/conda/bin:$PATH
    pip install --upgrade --ignore-installed https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.1-cp27-none-linux_x86_64.whl
    pip install keras
    conda install pytorch torchvision -c pytorch
    conda clean --index-cache --tarballs --packages --yes

%runscript
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# this text code will run whenever the container
# is called as an executable or with `singularity run`
exec python $@


%help
This container is backed by Anaconda version 4.4.0 and provides the Python 3.6 bindings for:
    * Tensorflow 1.4.1
    * Keras 2.1.5
    * PyTorch 0.1.12


%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
export PATH="/opt/conda/bin:$PATH"
unset CONDA_DEFAULT_ENV
export ANACONDA_HOME=/opt/conda
```

## Collection

 - Name: [arcsUVA/singularity-scripts](https://github.com/arcsUVA/singularity-scripts)
 - License: None

