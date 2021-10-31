---
id: 10055
name: "pmitev/Teoroo-singularity"
branch: "master"
tag: "cuda9.2_u18.04_conda"
commit: "47e74caea6414d957e76cab16b915304839a3cba"
version: "16fb1dddb6a139b494586bc34b3ba2b2"
build_date: "2019-06-27T16:06:52.065Z"
size_mb: 7414
size: 3132117023
sif: "https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/cuda9.2_u18.04_conda/2019-06-27-47e74cae-16fb1ddd/16fb1dddb6a139b494586bc34b3ba2b2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pmitev/Teoroo-singularity/cuda9.2_u18.04_conda/2019-06-27-47e74cae-16fb1ddd/
recipe: https://datasets.datalad.org/shub/pmitev/Teoroo-singularity/cuda9.2_u18.04_conda/2019-06-27-47e74cae-16fb1ddd/Singularity
collection: pmitev/Teoroo-singularity
---

# pmitev/Teoroo-singularity:cuda9.2_u18.04_conda

```bash
$ singularity pull shub://pmitev/Teoroo-singularity:cuda9.2_u18.04_conda
```

## Singularity Recipe

```singularity
Bootstrap:  docker
From: nvidia/cuda:9.2-cudnn7-runtime-ubuntu18.04

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
                            gawk mc vim gnuplot cython sqlite pandoc gfortran libnvidia-compute-390 && rm -rf /var/lib/apt/lists/*

# install anaconda
if [ ! -d /usr/local/anaconda ]; then
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /root/anaconda.sh && \
   bash /root/anaconda.sh -b -p /usr/local/anaconda 
fi

# set anaconda path
export PATH="/usr/local/anaconda/bin:$PATH"

conda install -c anaconda tensorflow-gpu==1.13.1
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

