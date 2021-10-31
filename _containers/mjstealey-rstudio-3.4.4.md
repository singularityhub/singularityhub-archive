---
id: 3618
name: "mjstealey/rstudio"
branch: "master"
tag: "3.4.4"
commit: "50828c538c53e3d377f2638ba8e11cb48b012617"
version: "f1171514a03b200361db2c971d7fc000"
build_date: "2018-07-21T00:28:21.655Z"
size_mb: 1541
size: 498069535
sif: "https://datasets.datalad.org/shub/mjstealey/rstudio/3.4.4/2018-07-21-50828c53-f1171514/f1171514a03b200361db2c971d7fc000.simg"
url: https://datasets.datalad.org/shub/mjstealey/rstudio/3.4.4/2018-07-21-50828c53-f1171514/
recipe: https://datasets.datalad.org/shub/mjstealey/rstudio/3.4.4/2018-07-21-50828c53-f1171514/Singularity
collection: mjstealey/rstudio
---

# mjstealey/rstudio:3.4.4

```bash
$ singularity pull shub://mjstealey/rstudio:3.4.4
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

