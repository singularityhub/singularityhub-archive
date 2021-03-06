---
id: 933
name: "biokit/bioconvert"
branch: "master"
tag: "latest"
commit: "46ba86268f1e797bff1a2ccb0f32198ee4c4c33f"
version: "b161ba2004320fd7bacddea190626992"
build_date: "2021-04-13T10:21:11.032Z"
size_mb: 3394
size: 1013059615
sif: "https://datasets.datalad.org/shub/biokit/bioconvert/latest/2021-04-13-46ba8626-b161ba20/b161ba2004320fd7bacddea190626992.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/biokit/bioconvert/latest/2021-04-13-46ba8626-b161ba20/
recipe: https://datasets.datalad.org/shub/biokit/bioconvert/latest/2021-04-13-46ba8626-b161ba20/Singularity
collection: biokit/bioconvert
---

# biokit/bioconvert:latest

```bash
$ singularity pull shub://biokit/bioconvert:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:latest


%labels
  maintainer Bertrand Neron <bneron@pasteur.fr>
  package.name
  package.version 0.1.0
  package.homepage https://pypi.python.org/pypi/bioconvert/0.1.0
  package.source.url
  package.source.mdm5
  package.license GPLv3

%post
  ######### install system #########
  export BIOCONVERT_VERSION="0.1.0"


  apt-get update -y
  apt-get install -y wget bzip2
  apt-get install -y libgl1-mesa-glx

  # install anaconda
  if [ ! -d /usr/local/anaconda ]; then
      # wget https://repo.continuum.io/miniconda/Miniconda3-4.3.14-Linux-x86_64.sh\
      # for now, we use 4.2.12 to have python3.5 by default so no need to
      # create a new env saving space in the process. The reason for using 3.5
      # is inherent to the packages used at the moment.
      wget https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh\
           -O ~/anaconda.sh && \
      bash ~/anaconda.sh -b -p /usr/local/anaconda && \
      rm ~/anaconda.sh
  fi

  # set anaconda path
  export PATH=$PATH:/usr/local/anaconda/bin
  conda update conda

  conda config --add channels r
  conda config --add channels defaults
  conda config --add channels conda-forge
  conda config --add channels bioconda

  # The main packages for sequana:
  conda install --file https://raw.githubusercontent.com/biokit/bioconvert/master/requirements.txt
  conda install --file https://raw.githubusercontent.com/biokit/bioconvert/master/requirements_tools.txt
  #conda install -y graphviz==2.38 pygraphviz

  

  ######### install bioconvert #########
  pip install bioconvert==$BIOCONVERT_VERSION

  # add this directory for Institut Pasteur cluster usage
  if [ ! -d /pasteur ]; then mkdir /pasteur; fi

  # Uses agg as backend instead of qt (less dependencies)
  echo "backend:tkagg" > matplotlibrc

  ######## clean image ########
  apt-get autoremove -y
  apt-get clean -y
  conda clean -y --all

%environment
  export PATH=$PATH:/usr/local/anaconda/bin


%runscript
  exec /usr/local/anaconda/bin/bioconvert "$@"
```

## Collection

 - Name: [biokit/bioconvert](https://github.com/biokit/bioconvert)
 - License: [Other](None)

