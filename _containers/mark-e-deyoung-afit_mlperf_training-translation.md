---
id: 8043
name: "mark-e-deyoung/afit_mlperf_training"
branch: "master"
tag: "translation"
commit: "eaf1758ac31a8b96c233869fbd6ae755d34b5d18"
version: "0b4c4b1e430cb22b8a5e5bb011a644f8"
build_date: "2020-05-06T17:54:26.367Z"
size_mb: 4406
size: 2308608031
sif: "https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/translation/2020-05-06-eaf1758a-0b4c4b1e/0b4c4b1e430cb22b8a5e5bb011a644f8.simg"
url: https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/translation/2020-05-06-eaf1758a-0b4c4b1e/
recipe: https://datasets.datalad.org/shub/mark-e-deyoung/afit_mlperf_training/translation/2020-05-06-eaf1758a-0b4c4b1e/Singularity
collection: mark-e-deyoung/afit_mlperf_training
---

# mark-e-deyoung/afit_mlperf_training:translation

```bash
$ singularity pull shub://mark-e-deyoung/afit_mlperf_training:translation
```

## Singularity Recipe

```singularity
Bootstrap: docker
# https://hub.docker.com/r/nvidia/cuda
From: nvidia/cuda:9.0-cudnn7-devel

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
    conda install python=3.6
    conda install pip
    pip install --ignore-installed \
      --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.9.0-cp36-cp36m-linux_x86_64.whl
    pip install mlperf-compliance
    conda clean --tarballs

    # make /data and /code for mounts to external directories
    if [ ! -d /data ]; then mkdir /data; fi
    if [ ! -d /code ]; then mkdir /code; fi

% runscript
	echo "Singularity: TensorFlow 1.9.0"
	exec /bin/bash
```

## Collection

 - Name: [mark-e-deyoung/afit_mlperf_training](https://github.com/mark-e-deyoung/afit_mlperf_training)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

