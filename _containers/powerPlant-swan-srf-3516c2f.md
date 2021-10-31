---
id: 7214
name: "powerPlant/swan-srf"
branch: "master"
tag: "3516c2f"
commit: "433697ec400f5d58d65285d3c730ff66d0798770"
version: "1de4e12584dee00ea5666428da6febb8"
build_date: "2019-02-14T08:45:05.056Z"
size_mb: 3805
size: 2260480031
sif: "https://datasets.datalad.org/shub/powerPlant/swan-srf/3516c2f/2019-02-14-433697ec-1de4e125/1de4e12584dee00ea5666428da6febb8.simg"
url: https://datasets.datalad.org/shub/powerPlant/swan-srf/3516c2f/2019-02-14-433697ec-1de4e125/
recipe: https://datasets.datalad.org/shub/powerPlant/swan-srf/3516c2f/2019-02-14-433697ec-1de4e125/Singularity
collection: powerPlant/swan-srf
---

# powerPlant/swan-srf:3516c2f

```bash
$ singularity pull shub://powerPlant/swan-srf:3516c2f
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: charade/xlibbox@sha256:04b1aca63f51cd18972b44380a7fcf2da0115c9e21e80fb9d375f39f229f686d

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 3516c2f

%environment
  SWAN_BIN=/opt/swan/bin
  PATH=$SWAN_BIN:$PATH
  export SWAN_BIN PATH

%post
  cd /tmp
  git clone https://charade@bitbucket.org/charade/swan.git
  cd swan
  git checkout 3516c2f
  
  export SWAN_BIN=/opt/swan/bin
  mkdir -p $SWAN_BIN
  cd /tmp
  R CMD INSTALL swan

%runscript
if [ $# -eq 0 ]; then
  /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"$SINGULARITY_NAME <cmd>\" or \"singularity exec $SINGULARITY_NAME <cmd>\", where <cmd> is one of the following:\n"
  exec /bin/echo "sclip_scan swan_join swan_scan swan_stat"
else
  exec "$@"
fi
```

## Collection

 - Name: [powerPlant/swan-srf](https://github.com/powerPlant/swan-srf)
 - License: None

