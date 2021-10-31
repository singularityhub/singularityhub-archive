---
id: 9578
name: "bcaffo/kerasSingularity"
branch: "master"
tag: "addrstudio"
commit: "4ee176c03eb94719cc45e97fe2a2b3ce87555fa4"
version: "c91bbaed216465245072c8093f17e7ab"
build_date: "2019-06-05T15:20:41.291Z"
size_mb: 2661
size: 921628703
sif: "https://datasets.datalad.org/shub/bcaffo/kerasSingularity/addrstudio/2019-06-05-4ee176c0-c91bbaed/c91bbaed216465245072c8093f17e7ab.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bcaffo/kerasSingularity/addrstudio/2019-06-05-4ee176c0-c91bbaed/
recipe: https://datasets.datalad.org/shub/bcaffo/kerasSingularity/addrstudio/2019-06-05-4ee176c0-c91bbaed/Singularity
collection: bcaffo/kerasSingularity
---

# bcaffo/kerasSingularity:addrstudio

```bash
$ singularity pull shub://bcaffo/kerasSingularity:addrstudio
```

## Singularity Recipe

```singularity
bootstrap: shub
from: bcaffo/kerasSingularity:ubuntu16

%post 

    ## From the rocker/rstudio file
    apt-get install -y --no-install-recommends \
      file \
      git \
      libapparmor1 \
      libcurl4-openssl-dev \
      libedit2 \
      libssl-dev \
      lsb-release \
      psmisc \
      procps \
      python-setuptools \
      sudo \
      wget \
      libclang-dev \
      libclang-3.8-dev \
      libobjc-5-dev \
      libclang1-3.8 \
      libclang-common-3.8-dev \
      libllvm3.8 \
      libobjc4 \
      libgc1c2 \

    RSTUDIO_URL="https://www.rstudio.org/download/latest/stable/server/debian9_64/rstudio-server-latest-amd64.deb"
    wget -q $RSTUDIO_URL
    dpkg -i rstudio-server-*-amd64.deb
    rm rstudio-server-*-amd64.deb
    
    ## Add a user
    useradd rstudio
```

## Collection

 - Name: [bcaffo/kerasSingularity](https://github.com/bcaffo/kerasSingularity)
 - License: None

