---
id: 8092
name: "mark-e-deyoung/afit_mlperf_training"
branch: "master"
tag: "rnn_translator_cuda8cudnn7"
commit: "93714630801207478eacd3210cff7f77b7a6c84a"
version: "c3188fa2af0cbb79f7aae6712038a427"
build_date: "2020-05-06T17:44:25.538Z"
size_mb: 4293
size: 2299346975
sif: "https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/rnn_translator_cuda8cudnn7/2020-05-06-93714630-c3188fa2/c3188fa2af0cbb79f7aae6712038a427.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mark-e-deyoung/afit_mlperf_training/rnn_translator_cuda8cudnn7/2020-05-06-93714630-c3188fa2/
recipe: https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/rnn_translator_cuda8cudnn7/2020-05-06-93714630-c3188fa2/Singularity
collection: mark-e-deyoung/afit_mlperf_training
---

# mark-e-deyoung/afit_mlperf_training:rnn_translator_cuda8cudnn7

```bash
$ singularity pull shub://mark-e-deyoung/afit_mlperf_training:rnn_translator_cuda8cudnn7
```

## Singularity Recipe

```singularity
Bootstrap: docker
# https://hub.docker.com/r/nvidia/cuda
From: nvidia/cuda:8.0-cudnn7-devel

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
    conda install pytorch torchvision cudatoolkit=8.0 -c pytorch
    pip install sacrebleu numpy mlperf-compliance
    conda clean --tarballs

    # make /data and /code for mounts to external directories
    if [ ! -d /data ]; then mkdir /data; fi
    if [ ! -d /code ]; then mkdir /code; fi

% runscript
	echo "Singularity: PyTorch (CUDA 8.0 cuDNN 7"
	exec /bin/bash
```

## Collection

 - Name: [mark-e-deyoung/afit_mlperf_training](https://github.com/mark-e-deyoung/afit_mlperf_training)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

