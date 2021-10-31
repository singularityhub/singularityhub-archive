---
id: 11931
name: "AdrienLeGuillou/singularity-r"
branch: "master"
tag: "latest"
commit: "af252faebb27a231e71cb3f0d9d2100e60d5b32f"
version: "51426386ee5fbcb389187da2b7528df2669489e5a1fd73419b84af2163a4beff"
build_date: "2020-01-03T14:25:38.343Z"
size_mb: 221.46875
size: 232226816
sif: "https://datasets.datalad.org/shub/AdrienLeGuillou/singularity-r/latest/2020-01-03-af252fae-51426386/51426386ee5fbcb389187da2b7528df2669489e5a1fd73419b84af2163a4beff.sif"
url: https://datasets.datalad.org/shub/AdrienLeGuillou/singularity-r/latest/2020-01-03-af252fae-51426386/
recipe: https://datasets.datalad.org/shub/AdrienLeGuillou/singularity-r/latest/2020-01-03-af252fae-51426386/Singularity
collection: AdrienLeGuillou/singularity-r
---

# AdrienLeGuillou/singularity-r:latest

```bash
$ singularity pull shub://AdrienLeGuillou/singularity-r:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post
  # Software versions
  export R_VERSION=3.6.2
  export DEBIAN_FRONTEND=noninteractive
  export DEBCONF_NONINTERACTIVE_SEEN=true

  # Get dependencies
  echo 'tzdata tzdata/Areas select Etc' | debconf-set-selections
  echo 'tzdata tzdata/Zones/Etc select UTC' | debconf-set-selections
  apt-get update -qqy
  apt-get install -qqy --no-install-recommends \
    tzdata \
    locales \
    gnupg \
    ca-certificates

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8

  # Install R
  echo "deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/" > /etc/apt/sources.list.d/r.list
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9

  apt-get update
  apt-get install -y --no-install-recommends \
    r-base=${R_VERSION}* \
    r-base-core=${R_VERSION}* \
    r-base-dev=${R_VERSION}* \
    r-recommended=${R_VERSION}* \
    r-base-html=${R_VERSION}* \
    r-doc-html=${R_VERSION}* \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libcairo2-dev \
    libxt-dev \
    less

  # Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cloud.r-project.org/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site

  # Add a directory for host R libraries
  mkdir -p /library
  echo "R_LIBS_SITE=/library:\${R_LIBS_SITE}" >> /usr/lib/R/etc/Renviron.site

  # Clean up
  apt-get clean
  rm -rf /var/lib/apt/lists/*

%labels
  Maintaner Adrien Le Guillou
  R_Version 3.6.2

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"
```

## Collection

 - Name: [AdrienLeGuillou/singularity-r](https://github.com/AdrienLeGuillou/singularity-r)
 - License: [MIT License](https://api.github.com/licenses/mit)

