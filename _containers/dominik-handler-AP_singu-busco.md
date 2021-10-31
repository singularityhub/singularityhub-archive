---
id: 14601
name: "dominik-handler/AP_singu"
branch: "master"
tag: "busco"
commit: "873d90250820721b2c22000d4249ecd4d264ec70"
version: "adbc561a63a2ab034d5fb1391e48e3da69f519010843bdc029d7f1dedf2989f0"
build_date: "2020-10-13T14:51:01.995Z"
size_mb: 1532.9765625
size: 1607442432
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/busco/2020-10-13-873d9025-adbc561a/adbc561a63a2ab034d5fb1391e48e3da69f519010843bdc029d7f1dedf2989f0.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/busco/2020-10-13-873d9025-adbc561a/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/busco/2020-10-13-873d9025-adbc561a/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:busco

```bash
$ singularity pull shub://dominik-handler/AP_singu:busco
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ezlabgva/busco:v4.1.4_cv1

#@ Bootstrap: docker
#@ From: pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-runtime

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  busco 

%post

%environment

%runscript
    $@
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

