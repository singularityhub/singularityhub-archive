---
id: 13991
name: "powerPlant/qiime2-srf"
branch: "master"
tag: "2020.2"
commit: "196642e99dd2e07c6acb139043bc3e8ea7c7c526"
version: "74faafbfe03bfae26a9b625f8745b603c9b1a40e4f1343472cdb0e8e7b643004"
build_date: "2021-04-09T05:55:42.835Z"
size_mb: 2223.828125
size: 2331852800
sif: "https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2020.2/2021-04-09-196642e9-74faafbf/74faafbfe03bfae26a9b625f8745b603c9b1a40e4f1343472cdb0e8e7b643004.sif"
url: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2020.2/2021-04-09-196642e9-74faafbf/
recipe: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2020.2/2021-04-09-196642e9-74faafbf/Singularity
collection: powerPlant/qiime2-srf
---

# powerPlant/qiime2-srf:2020.2

```bash
$ singularity pull shub://powerPlant/qiime2-srf:2020.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: qiime2/core:2020.2

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 2020.2

%post
  chmod 775 /home/qiime2/q2cli/cache/completion.sh

%runscript
if [ -x /opt/conda/envs/qiime2-2020.2/bin/$SINGULARITY_NAME ]; then
    exec $SINGULARITY_NAME "$@"
else
  /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"singularity exec $SINGULARITY_NAME <cmd>\", where <cmd> is one of the following:\n"
  exec echo biom qiime
fi
```

## Collection

 - Name: [powerPlant/qiime2-srf](https://github.com/powerPlant/qiime2-srf)
 - License: None

