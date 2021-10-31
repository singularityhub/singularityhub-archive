---
id: 14567
name: "powerPlant/repet-srf"
branch: "master"
tag: "3.0"
commit: "6fcb1db854576968344cd6edd8abdfb3489ae8d4"
version: "6d59740d98ce4a15d90fa85741ee0881421682c98c3052f955e58cc6ca2f6c32"
build_date: "2020-10-07T23:02:06.099Z"
size_mb: 4963.2890625
size: 5204385792
sif: "https://datasets.datalad.org/shub/powerPlant/repet-srf/3.0/2020-10-07-6fcb1db8-6d59740d/6d59740d98ce4a15d90fa85741ee0881421682c98c3052f955e58cc6ca2f6c32.sif"
url: https://datasets.datalad.org/shub/powerPlant/repet-srf/3.0/2020-10-07-6fcb1db8-6d59740d/
recipe: https://datasets.datalad.org/shub/powerPlant/repet-srf/3.0/2020-10-07-6fcb1db8-6d59740d/Singularity
collection: powerPlant/repet-srf
---

# powerPlant/repet-srf:3.0

```bash
$ singularity pull shub://powerPlant/repet-srf:3.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: urgi/docker_vre_aio:v3.0

%environment
    export REPET_PATH="/usr/local/REPET_linux-x64-3.0"
    export PATH="/usr/local/REPET_linux-x64-3.0/bin:${PATH}"

%runscript
if [ -x $REPET_PATH/bin/$SINGULARITY_NAME ]; then
    exec $SINGULARITY_NAME "$@"
else
  /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"singularity exec $SINGULARITY_NAME <cmd>\", where <cmd> is one of the following:\n"
  exec ls $REPET_PATH/bin
fi

%help
    This assumes that $PATH below contains symlinks to the container image
    See https://github.com/powerPlant/README#dealing-with-multiple-entrypoints
%labels
    Author	Ben Warren <ben.warren@plantandfood.co.nz>
    Name	REPET
    Version	3.0
```

## Collection

 - Name: [powerPlant/repet-srf](https://github.com/powerPlant/repet-srf)
 - License: None

