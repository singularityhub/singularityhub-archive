---
id: 7656
name: "jjhelmus/sample_singularity_containers"
branch: "master"
tag: "gpu_cuda90_27"
commit: "59f17a08f90c63313298f371526ae12466275d18"
version: "9e84f058d2942c95ecb717c184a984b7"
build_date: "2019-03-27T08:48:37.109Z"
size_mb: 9411
size: 5067026463
sif: "https://datasets.datalad.org/shub/jjhelmus/sample_singularity_containers/gpu_cuda90_27/2019-03-27-59f17a08-9e84f058/9e84f058d2942c95ecb717c184a984b7.simg"
url: https://datasets.datalad.org/shub/jjhelmus/sample_singularity_containers/gpu_cuda90_27/2019-03-27-59f17a08-9e84f058/
recipe: https://datasets.datalad.org/shub/jjhelmus/sample_singularity_containers/gpu_cuda90_27/2019-03-27-59f17a08-9e84f058/Singularity
collection: jjhelmus/sample_singularity_containers
---

# jjhelmus/sample_singularity_containers:gpu_cuda90_27

```bash
$ singularity pull shub://jjhelmus/sample_singularity_containers:gpu_cuda90_27
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:16.04

%environment
    export LANG=C.UTF-8
    export LC_ALL=C.UTF-8

%files
    sitecustomize.py /opt

%post
    . /environment

    # install necessary system libraries and utilities
    apt-get update --fix-missing
    apt-get install -y wget bzip2 libglib2.0-0 libxext6 libsm6 libxrender1

    # install miniconda
    mkdir -p /opt
    MINICONDA_URL=https://repo.anaconda.com/miniconda/Miniconda3-4.5.12-Linux-x86_64.sh
    wget --quiet $MINICONDA_URL -O /opt/miniconda.sh
    /bin/bash /opt/miniconda.sh -b -p /opt/conda
    rm /opt/miniconda.sh
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh
    echo ". /etc/profile.d/conda.sh" >> /etc/bash.conda
    echo "conda activate base" >> /etc/bash.conda

    # activate the base environment
    . /opt/conda/etc/profile.d/conda.sh

    # install anaconda
    conda install -y -q python=2.7 anaconda=2018.12

    # update conda
    conda install -y -q conda=4.6 anaconda=custom

    # install selected packages
    conda install -y -q -c defaults -c conda-forge -c engility \
        mpi4py \
        pydotplus \
        altair \
        hdbscan \
        datreant=1.0 \
        pymatgen \
        tpot \
        seaborn \
        nb_conda \
        libiconv \
        ipyparallel \
        mkl=2019.1=144 \
        libgcc-ng=8 \
        blas=*=mkl \
        tensorflow-gpu \
        theano \
        lasagne=2 \
        keras-gpu \
        pytorch \
        torchvision \
        blaze \
        libxslt \
        caffe-gpu \
        cudatoolkit=9.0 

    # mv sitecustomize.py file
    SP_DIR=`/opt/conda/bin/python -c "import site; print(site.getsitepackages()[0])"`
    mv /opt/sitecustomize.py $SP_DIR

%runscript
    /bin/bash --noprofile --rcfile /etc/bash.conda
```

## Collection

 - Name: [jjhelmus/sample_singularity_containers](https://github.com/jjhelmus/sample_singularity_containers)
 - License: None

