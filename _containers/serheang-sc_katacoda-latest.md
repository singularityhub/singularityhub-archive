---
id: 11033
name: "serheang/sc_katacoda"
branch: "master"
tag: "latest"
commit: "ffc6b1336796a8ffd63bafd3899a42f8d4dac741"
version: "e1a3b93c47f84c53cee807ac500c473d"
build_date: "2019-09-27T03:21:53.820Z"
size_mb: 179.0
size: 38809631
sif: "https://datasets.datalad.org/shub/serheang/sc_katacoda/latest/2019-09-27-ffc6b133-e1a3b93c/e1a3b93c47f84c53cee807ac500c473d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/serheang/sc_katacoda/latest/2019-09-27-ffc6b133-e1a3b93c/
recipe: https://datasets.datalad.org/shub/serheang/sc_katacoda/latest/2019-09-27-ffc6b133-e1a3b93c/Singularity
collection: serheang/sc_katacoda
---

# serheang/sc_katacoda:latest

```bash
$ singularity pull shub://serheang/sc_katacoda:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
from:alpine:latest

%labels
  MAINTAINER Ser Heang TAN <serheang+git@gmail.com>
  WHATAMI katacoda
  VERSION 1.0

%help
  This is a container to run katacoda cli.  You just need to run the sif.  
For example:
  singularity run katacoda.sif
OR
  katacoda.sif

%environment
  export OS=$(sed -n -e 's/^ID=//p' /etc/os-release)
  export VERSION=$(sed -n -e 's/^VERSION_ID=//p' /etc/os-release)
  export LC_ALL=C
  export PATH=/usr/local/bin:$PATH

%post
  apk update
  apk add npm

  ## Get katacoda-cli via npm
  npm install katacoda-cli --global

  ## CLEANUP

%runscript
  echo "Running katacoda in ${OS}-${VERSION} container"
  katacoda $@
```

## Collection

 - Name: [serheang/sc_katacoda](https://github.com/serheang/sc_katacoda)
 - License: [MIT License](https://api.github.com/licenses/mit)

