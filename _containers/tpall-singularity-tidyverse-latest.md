---
id: 14695
name: "tpall/singularity-tidyverse"
branch: "master"
tag: "latest"
commit: "d78777ae9505f39833485ee238fe77c7487469aa"
version: "bc534cccbc3b00e93636a992aaedfbb04df9b0e8d62986e865c62286971bfecd"
build_date: "2021-01-19T07:11:32.840Z"
size_mb: 490.41015625
size: 514232320
sif: "https://datasets.datalad.org/shub/tpall/singularity-tidyverse/latest/2021-01-19-d78777ae-bc534ccc/bc534cccbc3b00e93636a992aaedfbb04df9b0e8d62986e865c62286971bfecd.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tpall/singularity-tidyverse/latest/2021-01-19-d78777ae-bc534ccc/
recipe: https://datasets.datalad.org/shub/tpall/singularity-tidyverse/latest/2021-01-19-d78777ae-bc534ccc/Singularity
collection: tpall/singularity-tidyverse
---

# tpall/singularity-tidyverse:latest

```bash
$ singularity pull shub://tpall/singularity-tidyverse:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: tpall/singularity-r:latest

%labels
  Maintainer tpall

%help
  This will run R tidyverse + some other packages

%post
  ## Download and install tidyverse & other packages
  apt-get update -qq \
  && apt-get -y --no-install-recommends install \
    libxml2-dev \
    libcairo2-dev \
    libgit2-dev \
    default-libmysqlclient-dev \
    libpq-dev \
    libsasl2-dev \
    libsqlite3-dev \
    libssh2-1-dev \
    unixodbc-dev \
    libudunits2-dev \
    libcurl4-openssl-dev \
    libssl-dev \
    libgdal-dev \
    libgsl-dev \
    libnode-dev \
    libharfbuzz-dev \
    libfribidi-dev \
  && install2.r --error \
    --deps TRUE \
    --skipinstalled \
    tidyverse \
    lubridate \
    remotes \
    rmarkdown \
    bookdown \
    vroom \
    gert \
    readxl \
    here
```

## Collection

 - Name: [tpall/singularity-tidyverse](https://github.com/tpall/singularity-tidyverse)
 - License: None

