---
id: 6769
name: "powerPlant/nextgenmap-srf"
branch: "master"
tag: "latest"
commit: "73178f30fbe0f83e7240846b58ec0bb0b439cae3"
version: "160a1c0dcc2648327059c7f1562decee"
build_date: "2019-01-31T22:31:30.607Z"
size_mb: 545
size: 207396895
sif: "https://datasets.datalad.org/shub/powerPlant/nextgenmap-srf/latest/2019-01-31-73178f30-160a1c0d/160a1c0dcc2648327059c7f1562decee.simg"
url: https://datasets.datalad.org/shub/powerPlant/nextgenmap-srf/latest/2019-01-31-73178f30-160a1c0d/
recipe: https://datasets.datalad.org/shub/powerPlant/nextgenmap-srf/latest/2019-01-31-73178f30-160a1c0d/Singularity
collection: powerPlant/nextgenmap-srf
---

# powerPlant/nextgenmap-srf:latest

```bash
$ singularity pull shub://powerPlant/nextgenmap-srf:latest
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
  ngm "$@"
```

## Collection

 - Name: [powerPlant/nextgenmap-srf](https://github.com/powerPlant/nextgenmap-srf)
 - License: None

