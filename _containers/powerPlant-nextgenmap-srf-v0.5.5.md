---
id: 6770
name: "powerPlant/nextgenmap-srf"
branch: "master"
tag: "v0.5.5"
commit: "3df23a87eaa5b6840431fd498aa7c472c90a5c89"
version: "7ec2d4b9c30a90606941c4c0a777bf33"
build_date: "2019-02-05T05:54:32.383Z"
size_mb: 545
size: 207396895
sif: "https://datasets.datalad.org/shub/powerPlant/nextgenmap-srf/v0.5.5/2019-02-05-3df23a87-7ec2d4b9/7ec2d4b9c30a90606941c4c0a777bf33.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/nextgenmap-srf/v0.5.5/2019-02-05-3df23a87-7ec2d4b9/
recipe: https://datasets.datalad.org/shub/powerPlant/nextgenmap-srf/v0.5.5/2019-02-05-3df23a87-7ec2d4b9/Singularity
collection: powerPlant/nextgenmap-srf
---

# powerPlant/nextgenmap-srf:v0.5.5

```bash
$ singularity pull shub://powerPlant/nextgenmap-srf:v0.5.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version v0.5.5

%post
  ## Download build prerequisites
  buildDeps='git wget gcc g++ libc6-dev make cmake zlib1g-dev ca-certificates' && \
  apt-get update && apt-get install -y $buildDeps --no-install-recommends
  update-ca-certificates
  git clone https://github.com/Cibiv/NextGenMap.git && cd NextGenMap && git checkout v0.5.5 && mkdir -p build && cd build && cmake .. && make && cp -r ../bin/ngm-*/* /usr/bin/ && cd .. && rm -rf NextGenMap
  chmod 755 /usr/bin/ngm*

  ## Cleanup
  rm -rf /var/lib/apt/lists/* && \
  apt-get purge -y --auto-remove $buildDeps 
  apt-get -y clean all

%runscript
  exec ngm "$@"
```

## Collection

 - Name: [powerPlant/nextgenmap-srf](https://github.com/powerPlant/nextgenmap-srf)
 - License: None

