---
id: 9943
name: "brucemoran/Singularity"
branch: "master"
tag: "centos7-r_3.5.1"
commit: "a7ad83c3f6a18536b898ef1921de3250d29756f5"
version: "43ce56b61f35fa345aa74793f093c889"
build_date: "2019-06-21T06:30:06.084Z"
size_mb: 2108
size: 729972767
sif: "https://datasets.datalad.org/shub/brucemoran/Singularity/centos7-r_3.5.1/2019-06-21-a7ad83c3-43ce56b6/43ce56b61f35fa345aa74793f093c889.simg"
url: https://datasets.datalad.org/shub/brucemoran/Singularity/centos7-r_3.5.1/2019-06-21-a7ad83c3-43ce56b6/
recipe: https://datasets.datalad.org/shub/brucemoran/Singularity/centos7-r_3.5.1/2019-06-21-a7ad83c3-43ce56b6/Singularity
collection: brucemoran/Singularity
---

# brucemoran/Singularity:centos7-r_3.5.1

```bash
$ singularity pull shub://brucemoran/Singularity:centos7-r_3.5.1
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:brucemoran/Singularity:centos7

%post

    yum install -y libcurl-devel \
                   cairo-devel \
                   mysql-devel \
                   libxml2-devel \
                   netcdf-devel \
                   udunits2-devel \
                   openssl-devel \
                   libssh2-devel \
                   libgit2-devel

    yum -y install R.x86_64
    mkdir -p /usr/local/lib64/R/bin
    ln -s /usr/bin/R /usr/local/lib64/R/bin/R

    ##locales
    echo 'export LANG=en_US.UTF-8 LANGUAGE=C LC_ALL=C LC_CTYPE=C LC_COLLATE=C  LC_TIME=C LC_MONETARY=C LC_PAPER=C LC_MEASUREMENT=C' >> $SINGULARITY_ENVIRONMENT

    ##set R environmental variables
    echo 'export R_LIBS=/usr/lib64/R/library' >> $SINGULARITY_ENVIRONMENT
    export R_LIBS=/usr/lib64/R/library

    #BiocManager to allow further install of packages
    R_DOCS=$(readlink -e /usr/share/doc/R-*)
    mkdir -p $R_DOCS/html/
    R --slave -e 'install.packages("BiocManager", repos="https://cloud.r-project.org/", quiet=T); library("BiocManager"); BiocManager::install(c("tidyverse", "ggplot2", "devtools", "plyr", "dplyr"), dependencies=c("Depends", "Imports", "LinkingTo"), update=TRUE, ask=FALSE, build_vignettes = FALSE, clean=TRUE)'
```

## Collection

 - Name: [brucemoran/Singularity](https://github.com/brucemoran/Singularity)
 - License: None

