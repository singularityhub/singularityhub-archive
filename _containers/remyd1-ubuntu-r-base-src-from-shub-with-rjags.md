---
id: 1985
name: "remyd1/ubuntu-r-base"
branch: "master"
tag: "src-from-shub-with-rjags"
commit: "b705565187cb07168ce69dcf0ee5e774b6761952"
version: "328c70d92754dcc2bb0e0a821ba409a0"
build_date: "2018-04-11T17:52:04.816Z"
size_mb: 1320
size: 482037791
sif: "https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/src-from-shub-with-rjags/2018-04-11-b7055651-328c70d9/328c70d92754dcc2bb0e0a821ba409a0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/remyd1/ubuntu-r-base/src-from-shub-with-rjags/2018-04-11-b7055651-328c70d9/
recipe: https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/src-from-shub-with-rjags/2018-04-11-b7055651-328c70d9/Singularity
collection: remyd1/ubuntu-r-base
---

# remyd1/ubuntu-r-base:src-from-shub-with-rjags

```bash
$ singularity pull shub://remyd1/ubuntu-r-base:src-from-shub-with-rjags
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: shub://singularity-hub.org/remyd1/ubuntu-r-base:src-bioconductor


%environment
  R_VERSION=3.4.3
  export R_VERSION
  R_CONFIG_DIR=/etc/R/
  export R_CONFIG_DIR

%labels
  Author Remy Dernat
  Version v0.0.1
  R_Version 3.4.3
  build_date 2018 Feb 09
  R_bioconductor True

%apprun R
  exec R "$@"

%apprun Rscript
  exec Rscript "$@"

%runscript
  exec R "$@"

%post
  NPROCS=`awk '/^processor/ {s+=1}; END{print s}' /proc/cpuinfo`
  apt-get install -y jags
  # installing some packages
  echo install.packages\(\"rjags\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
```

## Collection

 - Name: [remyd1/ubuntu-r-base](https://github.com/remyd1/ubuntu-r-base)
 - License: None

