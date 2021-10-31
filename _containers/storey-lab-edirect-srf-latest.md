---
id: 14022
name: "storey-lab/edirect-srf"
branch: "master"
tag: "latest"
commit: "5321d7b401aaa9e201ba609e893ddb49ba283195"
version: "ed2decf818beb49add5fdbadcc19123732a93cc61e8b28fcecc4820cad61ac9d"
build_date: "2020-08-24T04:49:03.259Z"
size_mb: 334.46484375
size: 350711808
sif: "https://datasets.datalad.org/shub/storey-lab/edirect-srf/latest/2020-08-24-5321d7b4-ed2decf8/ed2decf818beb49add5fdbadcc19123732a93cc61e8b28fcecc4820cad61ac9d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/storey-lab/edirect-srf/latest/2020-08-24-5321d7b4-ed2decf8/
recipe: https://datasets.datalad.org/shub/storey-lab/edirect-srf/latest/2020-08-24-5321d7b4-ed2decf8/Singularity
collection: storey-lab/edirect-srf
---

# storey-lab/edirect-srf:latest

```bash
$ singularity pull shub://storey-lab/edirect-srf:latest
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

%setup
  echo export BUILDER_REPOSITORY_VERSION="$(git rev-parse --verify --short HEAD)"       > .builderinfo
  echo export BUILDER_REPOSITORY_NAME="$(basename "$(git rev-parse --show-toplevel)")" >> .builderinfo
  echo export BUILDER_REPOSITORY_URL="$(git remote get-url origin)"                    >> .builderinfo

%files
  .builderinfo .builderinfo
  cpanfile cpanfile
  edirect-commands allowed

%post
### install / update system dependencies
  apt-get -y update && apt-get -y install git locales
  APP_REPOSITORY_VERSION=13.8.20200819
  APP_REPOSITORY_NAME=edirect
  APP_REPOSITORY_URL=https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/$APP_REPOSITORY_VERSION/$APP_REPOSITORY_NAME-$APP_REPOSITORY_VERSION.tar.gz
### install dependencies and application
  cpanm --installdeps -n -q .
### install
  curl -Lo edirect.tar.gz $APP_REPOSITORY_URL
  tar -zxf edirect.tar.gz
  curl -Lo edirect/rchive.Linux.gz https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/$APP_REPOSITORY_VERSION/rchive.Linux.gz
  gunzip edirect/rchive.Linux.gz
  chmod +x edirect/rchive.Linux
  curl -Lo edirect/xtract.Linux.gz https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/$APP_REPOSITORY_VERSION/xtract.Linux.gz
  gunzip edirect/xtract.Linux.gz
  chmod +x edirect/xtract.Linux
### cleanup and store environment
  rm -rf cpanfile ~/.cpanm
  echo "export APP_REPOSITORY_VERSION=\"${APP_REPOSITORY_VERSION}\"" >> $SINGULARITY_ENVIRONMENT
  echo "export APP_REPOSITORY_NAME=\"${APP_REPOSITORY_NAME}\""       >> $SINGULARITY_ENVIRONMENT
  echo "export APP_REPOSITORY_URL=\"${APP_REPOSITORY_URL}\""         >> $SINGULARITY_ENVIRONMENT
  cat .builderinfo                                                   >> $SINGULARITY_ENVIRONMENT
  echo "PATH=\"/edirect:/usr/local/bin:$PATH\""                      >> $SINGULARITY_ENVIRONMENT

%runscript
### apprun with a dashes are not supported
### neither are symlinks to manage/change singularity name
### roll our own.
  ## echo "Container created by $BUILDER_REPOSITORY_NAME@$BUILDER_REPOSITORY_VERSION ($BUILDER_REPOSITORY_URL)" >&2
  ## echo "Application from: $APP_REPOSITORY_NAME@$APP_REPOSITORY_VERSION ($APP_REPOSITORY_URL)"                >&2
  SINGULARITY_BASENAME="$(basename "$SINGULARITY_NAME" .sif)"
  if echo "$SINGULARITY_BASENAME" | grep -qxf /allowed; then
    if which "$SINGULARITY_BASENAME" >/dev/null; then
      exec "$SINGULARITY_BASENAME" "$@"
    else
      echo "$SINGULARITY_BASENAME is not known" >&2
    fi
  else
    echo "$SINGULARITY_BASENAME is not an $APP_REPOSITORY_NAME command" >&2
  fi
```

## Collection

 - Name: [storey-lab/edirect-srf](https://github.com/storey-lab/edirect-srf)
 - License: None

