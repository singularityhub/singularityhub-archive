---
id: 1373
name: "remyd1/ubuntu-r-base"
branch: "master"
tag: "latest"
commit: "b79ba285ae5b1616e41635003edc2b067711c072"
version: "d399f46997b8714520456c8bb782974e"
build_date: "2020-06-05T12:15:17.727Z"
size_mb: 697
size: 285986847
sif: "https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/latest/2020-06-05-b79ba285-d399f469/d399f46997b8714520456c8bb782974e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/remyd1/ubuntu-r-base/latest/2020-06-05-b79ba285-d399f469/
recipe: https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/latest/2020-06-05-b79ba285-d399f469/Singularity
collection: remyd1/ubuntu-r-base
---

# remyd1/ubuntu-r-base:latest

```bash
$ singularity pull shub://remyd1/ubuntu-r-base:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04
IncludeCmd: yes


%environment
  R_VERSION=3.2.5
  export R_VERSION
  R_CONFIG_DIR=/etc/R/
  export R_CONFIG_DIR

%labels
  Author Remy Dernat
  Version v0.0.1
  R_Version 3.2.5
  build_date 2018 Jan 19

%apprun R
  exec R "$@"

%apprun Rscript
  exec Rscript "$@"

%runscript
  exec R "$@"

%post
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

