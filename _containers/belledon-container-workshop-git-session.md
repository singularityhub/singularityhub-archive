---
id: 1464
name: "belledon/container-workshop"
branch: "master"
tag: "git-session"
commit: "3359f2b65e2ef762b1d1bf9ac56d3d7407c462eb"
version: "04b8102f0abae87f6d41fa4716eafdb7"
build_date: "2018-01-24T23:46:17.169Z"
size_mb: 813
size: 285450271
sif: "https://datasets.datalad.org/shub/belledon/container-workshop/git-session/2018-01-24-3359f2b6-04b8102f/04b8102f0abae87f6d41fa4716eafdb7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/belledon/container-workshop/git-session/2018-01-24-3359f2b6-04b8102f/
recipe: https://datasets.datalad.org/shub/belledon/container-workshop/git-session/2018-01-24-3359f2b6-04b8102f/Singularity
collection: belledon/container-workshop
---

# belledon/container-workshop:git-session

```bash
$ singularity pull shub://belledon/container-workshop:git-session
```

## Singularity Recipe

```singularity
bootstrap: docker
from: ubuntu:16.04


%post
  apt-get update
  apt-get install -y  vim \
                      nano \
                      git \
                      git-annex \
                      python3 \
                      python3-pip \
                      python3-numpy \
                      python3-setuptools \
                      python3-wheel \

  pip3 install datalad
```

## Collection

 - Name: [belledon/container-workshop](https://github.com/belledon/container-workshop)
 - License: None

