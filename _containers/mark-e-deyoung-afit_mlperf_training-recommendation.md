---
id: 8081
name: "mark-e-deyoung/afit_mlperf_training"
branch: "master"
tag: "recommendation"
commit: "78b08ded39c7b245f00375b0c022a81f1eb99b84"
version: "4cbebf25cf7329bf5605abcea6b8d84b"
build_date: "2020-05-06T17:22:39.702Z"
size_mb: 6224
size: 3342721055
sif: "https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/recommendation/2020-05-06-78b08ded-4cbebf25/4cbebf25cf7329bf5605abcea6b8d84b.simg"
url: https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/recommendation/2020-05-06-78b08ded-4cbebf25/
recipe: https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/recommendation/2020-05-06-78b08ded-4cbebf25/Singularity
collection: mark-e-deyoung/afit_mlperf_training
---

# mark-e-deyoung/afit_mlperf_training:recommendation

```bash
$ singularity pull shub://mark-e-deyoung/afit_mlperf_training:recommendation
```

## Singularity Recipe

```singularity
Bootstrap: docker
# https://hub.docker.com/r/nvidia/cuda
From: nvidia/cuda:9.1-cudnn7-devel

%environment
	PATH="/usr/local/anaconda/bin:$PATH"
	MLPERF_DATA_DIR="/data"

%post

    # install debian packages
    apt-get update
    apt-get install -y eatmydata
    eatmydata apt-get install -y wget bzip2 \
      ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 \
      git git-annex uuid-runtime unzip
    apt-get clean

    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
    # set anaconda path
    export PATH="/usr/local/anaconda/bin:$PATH"

    # install required packages
    conda install pip
    conda install pytorch torchvision cudatoolkit=9.0 -c pytorch
    pip install mlperf-compliance numpy pyyaml mkl mkl-include setuptools cmake cffi typing pandas tqdm scipy
    conda clean --tarballs

    # make /data and /code for mounts to external directories
    if [ ! -d /data ]; then mkdir /data; fi
    if [ ! -d /code ]; then mkdir /code; fi

% runscript
	echo "Singularity: PyTorch"
	exec /bin/bash
```

## Collection

 - Name: [mark-e-deyoung/afit_mlperf_training](https://github.com/mark-e-deyoung/afit_mlperf_training)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

