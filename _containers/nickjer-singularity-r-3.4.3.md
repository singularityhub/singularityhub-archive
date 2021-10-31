---
id: 1361
name: "nickjer/singularity-r"
branch: "master"
tag: "3.4.3"
commit: "50646b33041b1e84c34e76af7666faeaef4c1f4f"
version: "a1ac594aa54d4f5c3cf8a16fe263b8fa"
build_date: "2021-01-20T13:27:03.581Z"
size_mb: 591
size: 230768671
sif: "https://datasets.datalad.org/shub/nickjer/singularity-r/3.4.3/2021-01-20-50646b33-a1ac594a/a1ac594aa54d4f5c3cf8a16fe263b8fa.simg"
url: https://datasets.datalad.org/shub/nickjer/singularity-r/3.4.3/2021-01-20-50646b33-a1ac594a/
recipe: https://datasets.datalad.org/shub/nickjer/singularity-r/3.4.3/2021-01-20-50646b33-a1ac594a/Singularity
collection: nickjer/singularity-r
---

# nickjer/singularity-r:3.4.3

```bash
$ singularity pull shub://nickjer/singularity-r:3.4.3
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer Jeremy Nicklas
  R_Version 3.4.3

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%runscript
  exec R "${@}"

%post
  # Software versions
  export R_VERSION=3.4.3

  # Get dependencies
  apt-get update
  apt-get install -y --no-install-recommends \
    locales

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8

  # Install R
  echo "deb http://cran.r-project.org/bin/linux/ubuntu xenial/" > /etc/apt/sources.list.d/r.list
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
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

  # Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site

  # Add a directory for host R libraries
  mkdir -p /library
  echo "R_LIBS_SITE=/library:\${R_LIBS_SITE}" >> /usr/lib/R/etc/Renviron.site

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [nickjer/singularity-r](https://github.com/nickjer/singularity-r)
 - License: [MIT License](https://api.github.com/licenses/mit)

