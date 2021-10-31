---
id: 6779
name: "powerPlant/qiime2-srf"
branch: "master"
tag: "2018.11"
commit: "196642e99dd2e07c6acb139043bc3e8ea7c7c526"
version: "97bed31c5f32660d7e1d3659b04592610bbf0ee12cd3cfd024fa13350e54f3b7"
build_date: "2020-08-19T06:27:59.907Z"
size_mb: 2714.04296875
size: 2845880320
sif: "https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2018.11/2020-08-19-196642e9-97bed31c/97bed31c5f32660d7e1d3659b04592610bbf0ee12cd3cfd024fa13350e54f3b7.sif"
url: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2018.11/2020-08-19-196642e9-97bed31c/
recipe: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2018.11/2020-08-19-196642e9-97bed31c/Singularity
collection: powerPlant/qiime2-srf
---

# powerPlant/qiime2-srf:2018.11

```bash
$ singularity pull shub://powerPlant/qiime2-srf:2018.11
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: qiime2/core:2018.11

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 2018.11

%post
  chmod 775 /home/qiime2/q2cli/cache/completion.sh

%runscript
if [ -x /opt/conda/envs/qiime2-2018.11/bin/$SINGULARITY_NAME ]; then
    exec $SINGULARITY_NAME "$@"
else
  /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"singularity exec $SINGULARITY_NAME <cmd>\", where <cmd> is one of the following:\n"
  exec echo biom qiime
fi
```

## Collection

 - Name: [powerPlant/qiime2-srf](https://github.com/powerPlant/qiime2-srf)
 - License: None

