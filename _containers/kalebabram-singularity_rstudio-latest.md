---
id: 1557
name: "kalebabram/singularity_rstudio"
branch: "master"
tag: "latest"
commit: "8bc789756666cd8285c057b143259e81c9cc682d"
version: "b0afed0ab0372de9a6027550941c0051"
build_date: "2020-03-05T10:53:07.387Z"
size_mb: 1422
size: 472473631
sif: "https://datasets.datalad.org/shub/kalebabram/singularity_rstudio/latest/2020-03-05-8bc78975-b0afed0a/b0afed0ab0372de9a6027550941c0051.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kalebabram/singularity_rstudio/latest/2020-03-05-8bc78975-b0afed0a/
recipe: https://datasets.datalad.org/shub/kalebabram/singularity_rstudio/latest/2020-03-05-8bc78975-b0afed0a/Singularity
collection: kalebabram/singularity_rstudio
---

# kalebabram/singularity_rstudio:latest

```bash
$ singularity pull shub://kalebabram/singularity_rstudio:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: kalebabram/singularity_r
 
%help
  This will run RStudio server

%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}

%post
  # Software versions
  export RSTUDIO_LATEST=$(wget --no-check-certificate -qO- https://s3.amazonaws.com/rstudio-server/current.ver)

  # Install RStudio Server
  apt-get update
  apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gdebi-core
  wget \
    --no-verbose \
    -O rstudio-server.deb \
    "https://download2.rstudio.org/rstudio-server-${RSTUDIO_LATEST}-amd64.deb"
  gdebi -n rstudio-server.deb
  rm -f rstudio-server.deb

  # run install scripts
  wget https://raw.githubusercontent.com/kalebabram/singularity_rstudio/master/RNAmmer_1.0.tar.gz 
  wget https://raw.githubusercontent.com/kalebabram/singularity_rstudio/master/Prodigal_2.0.tar.gz 
  wget https://raw.githubusercontent.com/kalebabram/singularity_rstudio/master/build.R 
  chmod 777 /build.R
  Rscript /build.R
  # Clean up
  rm -rf /var/lib/apt/lists/*

%labels
  RStudio_version 1.1.419

%apprun rserver
  exec rserver "${@}"

%runscript
  exec rserver "${@}"
```

## Collection

 - Name: [kalebabram/singularity_rstudio](https://github.com/kalebabram/singularity_rstudio)
 - License: None

