---
id: 12413
name: "guy1ziv2/GEDI_to_GEE"
branch: "master"
tag: "latest"
commit: "83c014dc301a5326314ee5bbea698d9414b386dd"
version: "01960c396c9b19f9a9d3023d6acb514c"
build_date: "2020-04-05T12:01:06.977Z"
size_mb: 8334.0
size: 2609201183
sif: "https://datasets.datalad.org/shub/guy1ziv2/GEDI_to_GEE/latest/2020-04-05-83c014dc-01960c39/01960c396c9b19f9a9d3023d6acb514c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/guy1ziv2/GEDI_to_GEE/latest/2020-04-05-83c014dc-01960c39/
recipe: https://datasets.datalad.org/shub/guy1ziv2/GEDI_to_GEE/latest/2020-04-05-83c014dc-01960c39/Singularity
collection: guy1ziv2/GEDI_to_GEE
---

# guy1ziv2/GEDI_to_GEE:latest

```bash
$ singularity pull shub://guy1ziv2/GEDI_to_GEE:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From: tylere/docker-ee-datascience-notebook

%files
gedi_to_gee.py
manifest.template

%runscript
exec python3 gedi_to_gee.py

%environment
HOME=/home/home02/geogz

%post
HOME=/home/home02/geogz
CLOUD_SDK_VERSION=232.0.0
apt-get -qqy update && apt-get install -qqy \
      curl \
      gcc \
      python-dev \
      python-setuptools \
      apt-transport-https \
      lsb-release \
      openssh-client \
      git \
      gnupg && \
  easy_install -U pip && \
  pip install -U crcmod   && \
  export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
  echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" > /etc/apt/sources.list.d/google-cloud-sdk.list && \
  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
  apt-get update && \
  apt-get install -y google-cloud-sdk=${CLOUD_SDK_VERSION}-0 && \
  gcloud --version && \
  pip install fiona pyproj shapely h5py bs4
```

## Collection

 - Name: [guy1ziv2/GEDI_to_GEE](https://github.com/guy1ziv2/GEDI_to_GEE)
 - License: None

