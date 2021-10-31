---
id: 10074
name: "pmitev/Teoroo-singularity"
branch: "master"
tag: "u18.04_cuda9.2"
commit: "831f347c21237b076f600b76ab5ca61c95d38936"
version: "67581b40bdc80c48da049b6974aaec2b"
build_date: "2019-06-28T13:58:10.817Z"
size_mb: 6060
size: 2318389279
sif: "https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/u18.04_cuda9.2/2019-06-28-831f347c-67581b40/67581b40bdc80c48da049b6974aaec2b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pmitev/Teoroo-singularity/u18.04_cuda9.2/2019-06-28-831f347c-67581b40/
recipe: https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/u18.04_cuda9.2/2019-06-28-831f347c-67581b40/Singularity
collection: pmitev/Teoroo-singularity
---

# pmitev/Teoroo-singularity:u18.04_cuda9.2

```bash
$ singularity pull shub://pmitev/Teoroo-singularity:u18.04_cuda9.2
```

## Singularity Recipe

```singularity
Bootstrap:  docker
From: ubuntu:18.04

%runscript
  export PATH=/usr/local/bin:$PATH
  export XDG_RUNTIME_DIR=/tmp/.jupyter_$(uuidgen)
  jupyter notebook --ip 0.0.0.0 --no-browser

%environment
  export PYTHONNOUSERSITE=True
  PATH=/usr/local/anaconda/bin:$PATH

%post
#  echo 'PYTHONNOUSERSITE=True' >> $SINGULARITY_ENVIRONMENT
  export DEBIAN_FRONTEND=noninteractive

  apt-get update && apt-get install -y locales python3-dev  python3-pip  python3-tk wget git\
                            build-essential bash-completion less uuid-runtime libopenblas-dev csh openssh-client rsh-client \
                            gawk mc vim gnuplot cython sqlite pandoc gfortran && rm -rf /var/lib/apt/lists/*

# install anaconda
if [ ! -d /usr/local/anaconda ]; then
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /root/anaconda.sh && \
   bash /root/anaconda.sh -b -p /usr/local/anaconda 
fi

# set anaconda path
export PATH="/usr/local/anaconda/bin:$PATH"

conda install -c anaconda tensorflow-gpu==1.13.1 cudatoolkit==9.2
conda install -c conda-forge jupyter keras ase phonopy
conda install -c matsci pymatgen

pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --system
            
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --system
            
pip install jupyter-tensorboard                                                                                                                               
jupyter tensorboard enable --system

conda clean --tarballs
```

## Collection

 - Name: [pmitev/Teoroo-singularity](https://github.com/pmitev/Teoroo-singularity)
 - License: None

