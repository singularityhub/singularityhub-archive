---
id: 2312
name: "pegasus-isi/darpa_population_modeling"
branch: "master"
tag: "latest"
commit: "9a69e6468dffd83167c91340be9f4a98374ee15f"
version: "b8561a18783f28d188f9bf4849237766"
build_date: "2019-09-26T20:51:25.288Z"
size_mb: 1360
size: 507453471
sif: "https://datasets.datalad.org/shub/pegasus-isi/darpa_population_modeling/latest/2019-09-26-9a69e646-b8561a18/b8561a18783f28d188f9bf4849237766.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pegasus-isi/darpa_population_modeling/latest/2019-09-26-9a69e646-b8561a18/
recipe: https://datasets.datalad.org/shub/pegasus-isi/darpa_population_modeling/latest/2019-09-26-9a69e646-b8561a18/Singularity
collection: pegasus-isi/darpa_population_modeling
---

# pegasus-isi/darpa_population_modeling:latest

```bash
$ singularity pull shub://pegasus-isi/darpa_population_modeling:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:ubuntu:xenial

# Note: python3 is used for this project

%post

apt-get update && apt-get upgrade -y

apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        gdal-bin \
        gsfonts \
        imagemagick \
        libfreetype6-dev \
        libgdal-dev \
        libpng12-dev \
        libzmq3-dev \
        lsb-release \
        module-init-tools \
        openjdk-8-jdk \
        pkg-config \
        python \
        python3 \
        python3-dev \
        python3-pip \
        rsync \
        unzip \
        vim \
        wget

apt-get clean 
rm -rf /var/lib/apt/lists/*

pip3 install --upgrade pip==9.0.3
pip3 install --upgrade setuptools

pip3 install typing
pip3 install numpy
export CFLAGS=$(gdal-config --cflags) && pip3 install GDAL==$(gdal-config --version | awk -F'[.]' '{print $1"."$2}')
pip3 install pandas
pip3 install geopandas
pip3 install rasterio==0.36.0
```

## Collection

 - Name: [pegasus-isi/darpa_population_modeling](https://github.com/pegasus-isi/darpa_population_modeling)
 - License: None

