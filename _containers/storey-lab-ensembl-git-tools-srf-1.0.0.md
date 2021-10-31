---
id: 14164
name: "storey-lab/ensembl-git-tools-srf"
branch: "master"
tag: "1.0.0"
commit: "8199aa32ebc5c8deb3f7efe8ee1ea5bec91613de"
version: "63746745d4fc780577af47be34af2db5c0660b794f4e612b3749b3c92c947a5c"
build_date: "2020-09-03T04:00:38.703Z"
size_mb: 307.9765625
size: 322936832
sif: "https://datasets.datalad.org/shub/storey-lab/ensembl-git-tools-srf/1.0.0/2020-09-03-8199aa32-63746745/63746745d4fc780577af47be34af2db5c0660b794f4e612b3749b3c92c947a5c.sif"
url: https://datasets.datalad.org/shub/storey-lab/ensembl-git-tools-srf/1.0.0/2020-09-03-8199aa32-63746745/
recipe: https://datasets.datalad.org/shub/storey-lab/ensembl-git-tools-srf/1.0.0/2020-09-03-8199aa32-63746745/Singularity
collection: storey-lab/ensembl-git-tools-srf
---

# storey-lab/ensembl-git-tools-srf:1.0.0

```bash
$ singularity pull shub://storey-lab/ensembl-git-tools-srf:1.0.0
```

## Singularity Recipe

```singularity
BootStrap: docker
From: perl:5.30

%labels
  Author kiwiroy@users-noreply.github.com
  Maintainer roy.storey@plantandfood.co.nz
  Version 0.1.0

%environment
  export LC_ALL=C
  export PERL5OPT=-I/opt/local/lib/perl5

%setup
  echo export BUILDER_REPOSITORY_VERSION="$(git rev-parse --verify --short HEAD)"       > .builderinfo
  echo export BUILDER_REPOSITORY_NAME="$(basename "$(git rev-parse --show-toplevel)")" >> .builderinfo
  echo export BUILDER_REPOSITORY_URL="$(git remote get-url origin)"                    >> .builderinfo

%files
  .builderinfo .builderinfo
  git-ensembl-commands /opt/singularity-commands

%post
  cd /opt
  ## record builder details
  cat .builderinfo >> $SINGULARITY_ENVIRONMENT && rm .builderinfo
  
  ### install / update system dependencies
  apt-get -y update && apt-get -y install git locales
  
  ### clone application and save details
  git clone https://github.com/Ensembl/ensembl-git-tools.git ensembl-git-tools && cd ensembl-git-tools
  APP_REPOSITORY_VERSION=$(git rev-parse --verify --short HEAD)
  APP_REPOSITORY_NAME=$(basename "$(git rev-parse --show-toplevel)")
  APP_REPOSITORY_URL=$(git remote get-url origin)
  
  ### install dependencies and application
  cpanm -L/opt/local --installdeps -n -q .
  cpanm -L/opt/local .
  
  ### cleanup and store environment
  cd .. && rm -rf ensembl-git-tools ~/.cpanm
  echo "export APP_REPOSITORY_VERSION=\"${APP_REPOSITORY_VERSION}\"" >> $SINGULARITY_ENVIRONMENT
  echo "export APP_REPOSITORY_NAME=\"${APP_REPOSITORY_NAME}\""       >> $SINGULARITY_ENVIRONMENT
  echo "export APP_REPOSITORY_URL=\"${APP_REPOSITORY_URL}\""         >> $SINGULARITY_ENVIRONMENT
  echo 'PATH=$PATH:/opt/local/bin'                                   >> $SINGULARITY_ENVIRONMENT

%runscript
  SINGULARITY_BASENAME=$(basename $SINGULARITY_NAME .sif)
  if echo $SINGULARITY_BASENAME | grep -qxf /opt/singularity-commands; then
    exec /opt/local/bin/$SINGULARITY_NAME "$@"
  else
    /bin/echo "This is a Singularity image with the following commands:"
    /bin/echo ""
    exec cat /opt/singularity-commands
  fi
```

## Collection

 - Name: [storey-lab/ensembl-git-tools-srf](https://github.com/storey-lab/ensembl-git-tools-srf)
 - License: None

