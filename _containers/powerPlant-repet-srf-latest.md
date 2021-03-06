---
id: 14566
name: "powerPlant/repet-srf"
branch: "master"
tag: "latest"
commit: "6fcb1db854576968344cd6edd8abdfb3489ae8d4"
version: "dd668bc0f7d057f42fd227389e2c7a7b9eda4c2b30c76abc1dbc14ec265359c5"
build_date: "2020-10-07T22:03:45.162Z"
size_mb: 4963.28515625
size: 5204381696
sif: "https://datasets.datalad.org/shub/powerPlant/repet-srf/latest/2020-10-07-6fcb1db8-dd668bc0/dd668bc0f7d057f42fd227389e2c7a7b9eda4c2b30c76abc1dbc14ec265359c5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/repet-srf/latest/2020-10-07-6fcb1db8-dd668bc0/
recipe: https://datasets.datalad.org/shub/powerPlant/repet-srf/latest/2020-10-07-6fcb1db8-dd668bc0/Singularity
collection: powerPlant/repet-srf
---

# powerPlant/repet-srf:latest

```bash
$ singularity pull shub://powerPlant/repet-srf:latest
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

