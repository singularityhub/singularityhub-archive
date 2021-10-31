---
id: 2264
name: "phgenomics-singularity/pagit"
branch: "master"
tag: "latest"
commit: "f48649a9fbdd40573a831c2aa7e0c397d55ca0d1"
version: "4790a71ed55debcea4c9060d609e7e27"
build_date: "2019-09-04T19:18:43.746Z"
size_mb: 473
size: 196059167
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/pagit/latest/2019-09-04-f48649a9-4790a71e/4790a71ed55debcea4c9060d609e7e27.simg"
url: https://datasets.datalad.org/shub/phgenomics-singularity/pagit/latest/2019-09-04-f48649a9-4790a71e/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/pagit/latest/2019-09-04-f48649a9-4790a71e/Singularity
collection: phgenomics-singularity/pagit
---

# phgenomics-singularity/pagit:latest

```bash
$ singularity pull shub://phgenomics-singularity/pagit:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:trusty-20170817

%help
A Singulairty image for PAGIT

%labels
Maintainer Anders Goncalves da Silva
Build 1.0

%environment
PAGIT_VERSION=1.64bit
export PAGIT_VERSION

%post
    PAGIT_VERSION=1.64bit

    sudo locale-gen en_US.UTF-8
    sudo update-locale

    sudo apt-get --yes update
    sudo apt-get --yes install make wget tar tcsh openjdk-7-jre

    echo "INSTALLING PAGIT"
    INSTALLER=PAGIT.V${PAGIT_VERSION}.tgz
    wget ftp://ftp.sanger.ac.uk/pub/resources/software/pagit/${INSTALLER}
    mv ${INSTALLER} /opt && cd /opt
    tar zxf ${INSTALLER}
    sudo bash ./installme.sh
    rm -f ${INSTALLER}
    # comment out part of the test run that we don't want to run
    sudo sed -r -i 's/(^act.*)/#\1/g' PAGIT/exampleTestset/dotestrun.sh

    echo "Sorting some env variables..."
    sudo echo 'LANGUAGE="en_US:en"' >> $SINGULARITY_ENVIRONMENT
    sudo echo 'LC_ALL="en_US.UTF-8"' >> $SINGULARITY_ENVIRONMENT
    sudo echo 'LC_CTYPE="UTF-8"' >> $SINGULARITY_ENVIRONMENT
    sudo echo 'LANG="en_US.UTF-8"' >> $SINGULARITY_ENVIRONMENT

    # FIXING THE PATH
    sudo echo 'PAGIT_HOME=/opt/PAGIT' >> $SINGULARITY_ENVIRONMENT
    sudo echo 'PATH=$PAGIT_HOME/bin/:$PAGIT_HOME/bin/pileup_v0.5/:$PAGIT_HOME/bin/pileup_v0.5/ssaha2:$PAGIT_HOME/bin/pileup_v0.5/:$PAGIT_HOME/IMAGE/:$PAGIT_HOME/ABACAS:$PAGIT_HOME/ICORN/:$PAGIT_HOME/RATT/:$PATH' >> $SINGULARITY_ENVIRONMENT
    # ABACAS and IMAGE just need a path to there position
    # icorn setup
    sudo echo 'PILEUP_HOME=$PAGIT_HOME/bin/pileup_v0.5/'>> $SINGULARITY_ENVIRONMENT
    sudo echo 'ICORN_HOME=$PAGIT_HOME/ICORN/' >> $SINGULARITY_ENVIRONMENT
    sudo echo 'SNPOMATIC_HOME=$PAGIT_HOME/bin/' >> $SINGULARITY_ENVIRONMENT

    # RATT setup
    sudo echo 'RATT_HOME=$PAGIT_HOME/RATT' >> $SINGULARITY_ENVIRONMENT
    sudo echo 'RATT_CONFIG=$RATT_HOME/RATT.config' >> $SINGULARITY_ENVIRONMENT

    # PERL SETUP
    sudo echo 'PERL5LIB=$PERL5LIB:$PAGIT_HOME/lib' >> $SINGULARITY_ENVIRONMENT

    sudo echo 'export PATH PILEUP_HOME ICORN_HOME PILEUP_HOME SNPOMATIC_HOME RATT_HOME RATT_CONFIG PERL5LIB PAGIT_HOME' >> $SINGULARITY_ENVIRONMENT

%runscript
  echo "Welcome to PAGIT ${PAGIT_VERSION}" >&2
  exec "$@"

%test
  echo "Loading the environment"
  for script in /.singularity.d/env/*.sh; do
      if [ -f "$script" ]; then
          . "$script"
      fi
  done
  echo "Testing PAGIT"
  mkdir /tmp/test && cp /opt/PAGIT/exampleTestset/* /tmp/test
  cd /tmp/test
  ./dotestrun.sh
  cd .. && rm -rf test
```

## Collection

 - Name: [phgenomics-singularity/pagit](https://github.com/phgenomics-singularity/pagit)
 - License: None

