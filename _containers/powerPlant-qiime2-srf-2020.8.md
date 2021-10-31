---
id: 14691
name: "powerPlant/qiime2-srf"
branch: "master"
tag: "2020.8"
commit: "e83edfe10b7b92e99f2264987e9d4fb2ab2b9963"
version: "9f1cbb8a05d3122e0a3ca8146d53d284d02d52848da2875b94f8201fd9dcb5c8"
build_date: "2020-10-22T02:58:45.393Z"
size_mb: 1989.55078125
size: 2086195200
sif: "https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2020.8/2020-10-22-e83edfe1-9f1cbb8a/9f1cbb8a05d3122e0a3ca8146d53d284d02d52848da2875b94f8201fd9dcb5c8.sif"
url: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2020.8/2020-10-22-e83edfe1-9f1cbb8a/
recipe: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/2020.8/2020-10-22-e83edfe1-9f1cbb8a/Singularity
collection: powerPlant/qiime2-srf
---

# powerPlant/qiime2-srf:2020.8

```bash
$ singularity pull shub://powerPlant/qiime2-srf:2020.8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: qiime2/core:2020.8

%labels
Maintainer tejas.sevak@plantandfood.co.nz
Version 2020.8

%post
  chmod 775 /home/qiime2/q2cli/cache/completion.sh

%runscript
if [ -x /opt/conda/envs/qiime2-2020.8/bin/$SINGULARITY_NAME ]; then
    exec $SINGULARITY_NAME "$@"
else
  /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"singularity exec $SINGULARITY_NAME <cmd>\", where <cmd> is one of the following:\n"
  exec echo biom qiime
fi
```

## Collection

 - Name: [powerPlant/qiime2-srf](https://github.com/powerPlant/qiime2-srf)
 - License: None

