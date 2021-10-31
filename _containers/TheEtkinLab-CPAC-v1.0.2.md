---
id: 855
name: "TheEtkinLab/CPAC"
branch: "master"
tag: "v1.0.2"
commit: "c7aed96fd401aca7e464cf0ae52aef9f1819477a"
version: "c430a990c6d9e7be4b734ad178f9c7b7"
build_date: "2017-11-20T13:56:11.799Z"
size_mb: 3499
size: 1499508767
sif: "https://datasets.datalad.org/shub/TheEtkinLab/CPAC/v1.0.2/2017-11-20-c7aed96f-c430a990/c430a990c6d9e7be4b734ad178f9c7b7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TheEtkinLab/CPAC/v1.0.2/2017-11-20-c7aed96f-c430a990/
recipe: https://datasets.datalad.org/shub/TheEtkinLab/CPAC/v1.0.2/2017-11-20-c7aed96f-c430a990/Singularity
collection: TheEtkinLab/CPAC
---

# TheEtkinLab/CPAC:v1.0.2

```bash
$ singularity pull shub://TheEtkinLab/CPAC:v1.0.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: mnarayan/cpac

%help
You are in the C-PAC container. To see help run
singularity run TheEtkinLab-CPAC.simg -h

%runscript
    echo "Running C-PAC!"
    echo "Arguments received: $*"
    exec /code/run.py "$@"

%labels
Author mnarayan@users.noreply.github.com
Build-date 19/11/2017
Vendor Ubuntu
Version 1.0.2

%post
    echo "Hello from inside the C-PAC container"
    echo "Install additional software here"
```

## Collection

 - Name: [TheEtkinLab/CPAC](https://github.com/TheEtkinLab/CPAC)
 - License: None

