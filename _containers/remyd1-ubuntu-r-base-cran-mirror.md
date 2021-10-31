---
id: 1374
name: "remyd1/ubuntu-r-base"
branch: "master"
tag: "cran-mirror"
commit: "b79ba285ae5b1616e41635003edc2b067711c072"
version: "728aab06b5becdf25a59b9e171e3e50e"
build_date: "2018-01-19T22:16:27.738Z"
size_mb: 795
size: 320557087
sif: "https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/cran-mirror/2018-01-19-b79ba285-728aab06/728aab06b5becdf25a59b9e171e3e50e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/remyd1/ubuntu-r-base/cran-mirror/2018-01-19-b79ba285-728aab06/
recipe: https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/cran-mirror/2018-01-19-b79ba285-728aab06/Singularity
collection: remyd1/ubuntu-r-base
---

# remyd1/ubuntu-r-base:cran-mirror

```bash
$ singularity pull shub://remyd1/ubuntu-r-base:cran-mirror
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04
IncludeCmd: yes


%environment
  R_VERSION=3.4.3
  export R_VERSION
  R_CONFIG_DIR=/etc/R/
  export R_CONFIG_DIR

%labels
  Author Remy Dernat
  Version v0.0.1
  R_Version 3.4.3
  build_date 2018 Jan 19

%apprun R
  exec R "$@"

%apprun Rscript
  exec Rscript "$@"

%runscript
  exec R "$@"

%post
  apt-get update
  apt-get install -y software-properties-common
  add-apt-repository "deb http://cloud.r-project.org/bin/linux/ubuntu xenial/"
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
  apt-get update
  apt-get install -y r-base r-base-dev libblas3 libblas-dev liblapack-dev liblapack3

  # installing some packages
  echo install.packages\(\"ade4\"\, repos\=\'https://cloud.r-project.org\'\) | R --slave
  echo install.packages\(\"ape\"\, repos\=\'https://cloud.r-project.org/\'\) | R --slave
  echo install.packages\(\"FD\"\, repos\=\'https://cloud.r-project.org/\'\) | R --slave
```

## Collection

 - Name: [remyd1/ubuntu-r-base](https://github.com/remyd1/ubuntu-r-base)
 - License: None

