---
id: 2259
name: "mjstealey/rstudio"
branch: "master"
tag: "latest"
commit: "c555474972b27810d05b4b3df11100d6671ab018"
version: "7d0a26115a0e6bf426d615a5f89b9a8c"
build_date: "2021-04-14T08:36:32.105Z"
size_mb: 1539
size: 497098783
sif: "https://datasets.datalad.org/shub/mjstealey/rstudio/latest/2021-04-14-c5554749-7d0a2611/7d0a26115a0e6bf426d615a5f89b9a8c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mjstealey/rstudio/latest/2021-04-14-c5554749-7d0a2611/
recipe: https://datasets.datalad.org/shub/mjstealey/rstudio/latest/2021-04-14-c5554749-7d0a2611/Singularity
collection: mjstealey/rstudio
---

# mjstealey/rstudio:latest

```bash
$ singularity pull shub://mjstealey/rstudio:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: r-base:3.4.4

%help
  RStudio Desktop version 1.1.442
  R version 3.4.4 (2018-03-15) -- "Someone to Lean On"

  Usage:
  $ singularity run rstudio.3.4.4.simg [args]
  $ singularity run --app R rstudio.3.4.4.simg [args]
  $ singularity run --app Rscript rstudio.3.4.4.simg [args]
  $ singularity run --app rstudio rstudio.3.4.4.simg

%setup

%files

%labels
  Maintainer Michael J. Stealey
  Maintainer_Email stealey@renci.org
  RStudio_Version 1.1.442
  R_Version 3.4.4

%environment
  RSTUDIO_VERSION=1.1.442
  R_BASE_VERSION=3.4.4
  LC_ALL=en_US.UTF-8
  LANG=en_US.UTF-8

%post
  export RSTUDIO_VERSION=1.1.442
  apt-get update
  apt-get install -y \
    wget \
    gdebi-core \
    libxslt1-dev \
    qt5-default \
    mesa-utils \
    libgl1-mesa-glx \
    libgl1-mesa-dev
  wget \
    --no-verbose \
    "https://download1.rstudio.org/rstudio-xenial-${RSTUDIO_VERSION}-amd64.deb"
  gdebi -n rstudio-xenial-${RSTUDIO_VERSION}-amd64.deb
  rm -f rstudio-xenial-${RSTUDIO_VERSION}-amd64.deb
  rm -rf /var/lib/apt/lists/*

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%apprun rstudio
  exec rstudio "${@}"

%runscript
  exec "${@}"

%test
  exec R --version
```

## Collection

 - Name: [mjstealey/rstudio](https://github.com/mjstealey/rstudio)
 - License: [MIT License](https://api.github.com/licenses/mit)

