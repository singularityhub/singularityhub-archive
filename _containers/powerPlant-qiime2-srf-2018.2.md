---
id: 8005
name: "powerPlant/qiime2-srf"
branch: "master"
tag: "2018.2"
commit: "196642e99dd2e07c6acb139043bc3e8ea7c7c526"
version: "2dd11248a5903cb040f228474cd4c6cb0711bdd80f04124684ac0e63b5c7de5d"
build_date: "2020-08-19T06:54:54.102Z"
size_mb: 2714.33984375
size: 2846191616
sif: "https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2018.2/2020-08-19-196642e9-2dd11248/2dd11248a5903cb040f228474cd4c6cb0711bdd80f04124684ac0e63b5c7de5d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/qiime2-srf/2018.2/2020-08-19-196642e9-2dd11248/
recipe: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2018.2/2020-08-19-196642e9-2dd11248/Singularity
collection: powerPlant/qiime2-srf
---

# powerPlant/qiime2-srf:2018.2

```bash
$ singularity pull shub://powerPlant/qiime2-srf:2018.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: qiime2/core:2018.2

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 2018.2

%runscript
if [ -x /opt/conda/envs/qiime2-2018.2/bin/$SINGULARITY_NAME ]; then
    exec $SINGULARITY_NAME "$@"
else
  /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"singularity exec $SINGULARITY_NAME <cmd>\", where <cmd> is one of the following:\n"
  exec echo biom qiime
fi
```

## Collection

 - Name: [powerPlant/qiime2-srf](https://github.com/powerPlant/qiime2-srf)
 - License: None

