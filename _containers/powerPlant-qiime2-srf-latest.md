---
id: 6778
name: "powerPlant/qiime2-srf"
branch: "master"
tag: "latest"
commit: "e83edfe10b7b92e99f2264987e9d4fb2ab2b9963"
version: "00c20af6ede04409eea0942fd16145294a90a6e2cc1d5bfcfba086f421a4f292"
build_date: "2020-10-22T03:16:00.775Z"
size_mb: 1989.55078125
size: 2086195200
sif: "https://datasets.datalad.org/shub/powerPlant/qiime2-srf/latest/2020-10-22-e83edfe1-00c20af6/00c20af6ede04409eea0942fd16145294a90a6e2cc1d5bfcfba086f421a4f292.sif"
url: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/latest/2020-10-22-e83edfe1-00c20af6/
recipe: https://datasets.datalad.org/shub/powerPlant/qiime2-srf/latest/2020-10-22-e83edfe1-00c20af6/Singularity
collection: powerPlant/qiime2-srf
---

# powerPlant/qiime2-srf:latest

```bash
$ singularity pull shub://powerPlant/qiime2-srf:latest
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

