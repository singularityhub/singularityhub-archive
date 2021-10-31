---
id: 8835
name: "bioconvert/bioconvert"
branch: "master"
tag: "0_3_0"
commit: "7e521c6fd7c8a03b4e2fc87ffe87c8a716cb364d"
version: "4386e41ea39bfdf0f022fba9d34a6712"
build_date: "2021-04-07T19:51:39.162Z"
size_mb: 2636
size: 776433695
sif: "https://datasets.datalad.org/shub/bioconvert/bioconvert/0_3_0/2021-04-07-7e521c6f-4386e41e/4386e41ea39bfdf0f022fba9d34a6712.simg"
url: https://datasets.datalad.org/shub/bioconvert/bioconvert/0_3_0/2021-04-07-7e521c6f-4386e41e/
recipe: https://datasets.datalad.org/shub/bioconvert/bioconvert/0_3_0/2021-04-07-7e521c6f-4386e41e/Singularity
collection: biokit/bioconvert
---

# bioconvert/bioconvert:0_3_0

```bash
$ singularity pull shub://bioconvert/bioconvert:0_3_0
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:latest

###############################################
# do not change. This is a tagged version 0.1.
###############################################

%labels
  maintainer Bertrand Neron <bneron@pasteur.fr>
  package.name
  package.version 0.3.0
  package.homepage https://pypi.python.org/pypi/bioconvert/0.3.0
  package.source.url
  package.source.mdm5
  package.license GPLv3

%post
  ######### install system #########
  export BIOCONVERT_VERSION="0.3.0"


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
  if [ ! -d /etc/localtime ]; then mkdir /etc/localtime; fi

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

 - Name: [bioconvert/bioconvert](https://github.com/bioconvert/bioconvert)
 - License: [Other](None)

