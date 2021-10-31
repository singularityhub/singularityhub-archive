---
id: 7933
name: "mark-e-deyoung/afit_mlperf_training"
branch: "master"
tag: "sentiment_analysis"
commit: "eaf1758ac31a8b96c233869fbd6ae755d34b5d18"
version: "27ce3b7d45c396726f54e3ad64304663"
build_date: "2020-05-06T17:46:38.167Z"
size_mb: 3993
size: 2138406943
sif: "https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/sentiment_analysis/2020-05-06-eaf1758a-27ce3b7d/27ce3b7d45c396726f54e3ad64304663.simg"
url: https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/sentiment_analysis/2020-05-06-eaf1758a-27ce3b7d/
recipe: https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/sentiment_analysis/2020-05-06-eaf1758a-27ce3b7d/Singularity
collection: mark-e-deyoung/afit_mlperf_training
---

# mark-e-deyoung/afit_mlperf_training:sentiment_analysis

```bash
$ singularity pull shub://mark-e-deyoung/afit_mlperf_training:sentiment_analysis
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
      git git-annex uuid-runtime
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
    pip install paddlepaddle-gpu
    conda clean --tarballs

    # make /data and /code for mounts to external directories
    if [ ! -d /data ]; then mkdir /data; fi
    if [ ! -d /code ]; then mkdir /code; fi

% runscript
	echo "Singularity: paddlepaddle"
	exec /bin/bash
```

## Collection

 - Name: [mark-e-deyoung/afit_mlperf_training](https://github.com/mark-e-deyoung/afit_mlperf_training)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

