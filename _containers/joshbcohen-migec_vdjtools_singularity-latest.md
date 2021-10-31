---
id: 1088
name: "joshbcohen/migec_vdjtools_singularity"
branch: "master"
tag: "latest"
commit: "0872a9810d361b6ea05df2f4b235faea8d4e44d3"
version: "d42ab6371fd8eb0a02a912b0336c1587"
build_date: "2017-12-08T23:25:34.509Z"
size_mb: 2939
size: 1066979359
sif: "https://datasets.datalad.org/shub/joshbcohen/migec_vdjtools_singularity/latest/2017-12-08-0872a981-d42ab637/d42ab6371fd8eb0a02a912b0336c1587.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/joshbcohen/migec_vdjtools_singularity/latest/2017-12-08-0872a981-d42ab637/
recipe: https://datasets.datalad.org/shub/joshbcohen/migec_vdjtools_singularity/latest/2017-12-08-0872a981-d42ab637/Singularity
collection: joshbcohen/migec_vdjtools_singularity
---

# joshbcohen/migec_vdjtools_singularity:latest

```bash
$ singularity pull shub://joshbcohen/migec_vdjtools_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: joshbcohen/migec_vdjtools:latest
%post
   mkdir /vdj_pipeline
   cp ${HOME}/.bashrc /vdj_pipeline
   mkdir /scratchLocal
   mkdir /cluster001
   mkdir /athena
   mkdir /boot
   mkdir /pbtech_mounts
   mkdir /pbtech_mounts/homes022
   mkdir /pbtech_mounts/homes031
   mkdir /pbtech_mounts/softlib001
```

## Collection

 - Name: [joshbcohen/migec_vdjtools_singularity](https://github.com/joshbcohen/migec_vdjtools_singularity)
 - License: None

