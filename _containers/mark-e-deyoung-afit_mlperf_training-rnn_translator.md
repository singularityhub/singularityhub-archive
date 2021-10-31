---
id: 7934
name: "mark-e-deyoung/afit_mlperf_training"
branch: "master"
tag: "rnn_translator"
commit: "eaf1758ac31a8b96c233869fbd6ae755d34b5d18"
version: "9fcceb8de6c03d09169a41a50de2de88"
build_date: "2020-05-06T17:42:34.855Z"
size_mb: 4987
size: 2704371743
sif: "https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/rnn_translator/2020-05-06-eaf1758a-9fcceb8d/9fcceb8de6c03d09169a41a50de2de88.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mark-e-deyoung/afit_mlperf_training/rnn_translator/2020-05-06-eaf1758a-9fcceb8d/
recipe: https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/rnn_translator/2020-05-06-eaf1758a-9fcceb8d/Singularity
collection: mark-e-deyoung/afit_mlperf_training
---

# mark-e-deyoung/afit_mlperf_training:rnn_translator

```bash
$ singularity pull shub://mark-e-deyoung/afit_mlperf_training:rnn_translator
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
    conda install pytorch torchvision cudatoolkit=9.0 -c pytorch
    pip install sacrebleu numpy mlperf-compliance
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

