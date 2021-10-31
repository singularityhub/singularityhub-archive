---
id: 12922
name: "fpinter/work-environment"
branch: "master"
tag: "latest"
commit: "26ef4c47379f1ad6ab7b4e4ce287818b9cea3253"
version: "280125e2ddd15b7e22c1fcb86b66b696dada3b0f11442bcfc0ac02dfceb38301"
build_date: "2021-02-26T02:32:40.031Z"
size_mb: 1043.2890625
size: 1093967872
sif: "https://datasets.datalad.org/shub/fpinter/work-environment/latest/2021-02-26-26ef4c47-280125e2/280125e2ddd15b7e22c1fcb86b66b696dada3b0f11442bcfc0ac02dfceb38301.sif"
url: https://datasets.datalad.org/shub/fpinter/work-environment/latest/2021-02-26-26ef4c47-280125e2/
recipe: https://datasets.datalad.org/shub/fpinter/work-environment/latest/2021-02-26-26ef4c47-280125e2/Singularity
collection: fpinter/work-environment
---

# fpinter/work-environment:latest

```bash
$ singularity pull shub://fpinter/work-environment:latest
```

## Singularity Recipe

```singularity
BootStrap: library
From: ubuntu:20.04

%files
  renv.lock

%post
  # Install R
  sed -i 's/main/main restricted universe/g' /etc/apt/sources.list
  echo 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/' >> /etc/apt/sources.list
  apt-get -y install gnupg ca-certificates
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
  apt update

  apt-get -y install locales r-base r-base-dev
  apt-get clean
  locale-gen en_US.UTF-8

  # R packages
  apt-get -y install wget
  wget https://github.com/jgm/pandoc/releases/download/2.11.2/pandoc-2.11.2-1-amd64.deb
  dpkg -i pandoc-2.11.2-1-amd64.deb

  apt-get -y install libxml2-dev libcurl4-openssl-dev libssl-dev libgdal-dev libudunits2-dev
  Rscript -e 'install.packages("renv", repos="https://cloud.r-project.org/")'
  mkdir /opt/renv
  echo "RENV_PATHS_CACHE = /opt/renv" >> $(R RHOME)/etc/Renviron.site
  Rscript -e "options(renv.consent = TRUE); renv::restore()"

  # Install Anaconda (but not packages)
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  bash Miniconda3-latest-Linux-x86_64.sh -bfp /usr/local

%test
  #!/bin/sh
  exec Rscript -e "library(dplyr)"
  exec pandoc --version
```

## Collection

 - Name: [fpinter/work-environment](https://github.com/fpinter/work-environment)
 - License: None

