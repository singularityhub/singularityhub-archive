---
id: 13992
name: "powerPlant/qiime2-srf"
branch: "master"
tag: "2020.6"
commit: "196642e99dd2e07c6acb139043bc3e8ea7c7c526"
version: "d1be7050a06770fedd37899512a704548f736e15cc54372df1de6ae65e666153"
build_date: "2020-08-19T05:43:01.357Z"
size_mb: 2352.69140625
size: 2466975744
sif: "https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2020.6/2020-08-19-196642e9-d1be7050/d1be7050a06770fedd37899512a704548f736e15cc54372df1de6ae65e666153.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/qiime2-srf/2020.6/2020-08-19-196642e9-d1be7050/
recipe: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2020.6/2020-08-19-196642e9-d1be7050/Singularity
collection: powerPlant/qiime2-srf
---

# powerPlant/qiime2-srf:2020.6

```bash
$ singularity pull shub://powerPlant/qiime2-srf:2020.6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: qiime2/core:2020.6

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 2020.6

%post
  chmod 775 /home/qiime2/q2cli/cache/completion.sh

%runscript
if [ -x /opt/conda/envs/qiime2-2020.6/bin/$SINGULARITY_NAME ]; then
    exec $SINGULARITY_NAME "$@"
else
  /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"singularity exec $SINGULARITY_NAME <cmd>\", where <cmd> is one of the following:\n"
  exec echo biom qiime
fi
```

## Collection

 - Name: [powerPlant/qiime2-srf](https://github.com/powerPlant/qiime2-srf)
 - License: None

