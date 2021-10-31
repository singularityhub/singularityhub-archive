---
id: 1683
name: "phgenomics-singularity/ngmaster"
branch: "master"
tag: "v0.5.1"
commit: "7f563326a27cbc97a0d676aef5f959520c93b97b"
version: "ae5a5d6cf191cda43868a8bceebed012"
build_date: "2018-02-09T22:11:07.129Z"
size_mb: 572
size: 215863327
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/ngmaster/v0.5.1/2018-02-09-7f563326-ae5a5d6c/ae5a5d6cf191cda43868a8bceebed012.simg"
url: https://datasets.datalad.org/shub/phgenomics-singularity/ngmaster/v0.5.1/2018-02-09-7f563326-ae5a5d6c/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/ngmaster/v0.5.1/2018-02-09-7f563326-ae5a5d6c/Singularity
collection: phgenomics-singularity/ngmaster
---

# phgenomics-singularity/ngmaster:v0.5.1

```bash
$ singularity pull shub://phgenomics-singularity/ngmaster:v0.5.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:trusty-20170817

%help
A Singularity image for NGMASTER v0.5.1

%labels
Maintainer Anders Goncalves da Silva
Build 1.0
NGMASTER version 0.5.1
isPCR version 33

%post
  NGMASTER_VERSION=0.5.1
  isPCR_VERSION=33

  sudo locale-gen en_US.UTF-8
  sudo update-locale

  sudo apt-get --yes update
  sudo apt-get --yes install build-essential autoconf automake wget git zlib1g-dev libbz2-dev libncurses5-dev curl unzip

  sudo apt-get --yes install software-properties-common

  # add python3 support
  sudo add-apt-repository --yes ppa:jonathonf/python-3.6
  sudo apt-get --yes update
  sudo apt-get --yes install python3.6


  # getting pip and setuptools
  curl https://bootstrap.pypa.io/get-pip.py | sudo python3.6
  sudo pip3.6 install setuptools

  echo "Installing isPCR"

  export MACHTYPE='unix'
  export OLDHOME=${HOME}
  isPCR_VERSION=33
  isPCR_DL="http://hgwdev.cse.ucsc.edu/~kent/src/isPcr${isPCR_VERSION}.zip"
  isPCR_ZIP=ispcr.zip
  wget -O ${isPCR_ZIP} "${isPCR_DL}"
  unzip -o ${isPCR_ZIP}
  cd isPcrSrc
  export HOME=${PWD}
  sed -i 's/-Werror//g' inc/common.mk
  mkdir -p bin/${MACHTYPE}
  mkdir -p lib/${MACHTYPE}
  make
  sudo mv bin/${MACHTYPE}/*Pcr /usr/local/bin
  cd ..
  rm -r isPcrSrc ${isPCR_ZIP}
  export HOME=${OLDHOME}


  echo "Installing NGMASTER"

  NGMASTER_GT="git+https://github.com/MDU-PHL/ngmaster.git@v${NGMASTER_VERSION}"
  sudo pip3.6 install ${NGMASTER_GT}

  echo "UPDATING NGMASTER DB"
  sudo ngmaster --updatedb --assumeyes

  echo "Sorting some env variables..."
  echo "DB updated on $(date "+%Y-%m-%d")" > /etc/dbupdate
  sudo chmod 555 /etc/dbupdate
  sudo echo 'LANGUAGE="en_US:en"' >> $SINGULARITY_ENVIRONMENT
  sudo echo 'LC_ALL="en_US.UTF-8"' >> $SINGULARITY_ENVIRONMENT
  sudo echo 'LC_CTYPE="UTF-8"' >> $SINGULARITY_ENVIRONMENT
  sudo echo 'LANG="en_US.UTF-8"' >>  $SINGULARITY_ENVIRONMENT

  echo "Done"

%runscript
  echo "Welcome to NGMATER 0.5.1" >&2
  cat /etc/dbupdate >&2
  exec ngmaster "$@"

%test
  echo "Testing NGMASTER"
  ngmaster --test
```

## Collection

 - Name: [phgenomics-singularity/ngmaster](https://github.com/phgenomics-singularity/ngmaster)
 - License: None

