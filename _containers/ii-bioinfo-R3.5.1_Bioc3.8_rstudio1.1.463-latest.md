---
id: 6142
name: "ii-bioinfo/R3.5.1_Bioc3.8_rstudio1.1.463"
branch: "master"
tag: "latest"
commit: "ce5378b5bdbcbbee3675a4d1cf91989f92575161"
version: "466a148297af2c7c793c0177f9a7efa6"
build_date: "2021-01-18T14:29:57.463Z"
size_mb: 2589
size: 798650399
sif: "https://datasets.datalad.org/shub/ii-bioinfo/R3.5.1_Bioc3.8_rstudio1.1.463/latest/2021-01-18-ce5378b5-466a1482/466a148297af2c7c793c0177f9a7efa6.simg"
url: https://datasets.datalad.org/shub/ii-bioinfo/R3.5.1_Bioc3.8_rstudio1.1.463/latest/2021-01-18-ce5378b5-466a1482/
recipe: https://datasets.datalad.org/shub/ii-bioinfo/R3.5.1_Bioc3.8_rstudio1.1.463/latest/2021-01-18-ce5378b5-466a1482/Singularity
collection: ii-bioinfo/R3.5.1_Bioc3.8_rstudio1.1.463
---

# ii-bioinfo/R3.5.1_Bioc3.8_rstudio1.1.463:latest

```bash
$ singularity pull shub://ii-bioinfo/R3.5.1_Bioc3.8_rstudio1.1.463:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: bioconductor/release_core2:R3.5.1_Bioc3.8

%help
  RStudio Desktop version 1.1.463
  R version 3.5.1

  Usage:
  $ singularity run rstudio.3.5.1.simg [args]
  $ singularity run --app R rstudio.3.5.1.simg [args]
  $ singularity run --app Rscript rstudio.3.5.1.simg [args]
  $ singularity run --app rstudio rstudio.3.5.1.simg

%setup

%files

%labels
  ii-bioinfo@imp.ac.at
  RStudio_Version 1.1.463
  R_Version 3.5.1
  based on "https://github.com/mjstealey/rstudio"

%environment
  RSTUDIO_VERSION=1.1.463
  R_BASE_VERSION=3.5.1
  LC_ALL=en_US.UTF-8
  LANG=en_US.UTF-8

%post
  export RSTUDIO_VERSION=1.1.463
  apt-get update
  apt-get install -y \
    wget \
    gdebi-core \
    libxslt1-dev \
    qt5-default \
    mesa-utils \
    libgl1-mesa-glx \
    libgl1-mesa-dev \
    libxt6 \
    openssh-client

  R -e "install.packages('caTools')" #needed in rstudio

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

 - Name: [ii-bioinfo/R3.5.1_Bioc3.8_rstudio1.1.463](https://github.com/ii-bioinfo/R3.5.1_Bioc3.8_rstudio1.1.463)
 - License: None

