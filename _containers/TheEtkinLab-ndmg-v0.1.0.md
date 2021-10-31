---
id: 1501
name: "TheEtkinLab/ndmg"
branch: "master"
tag: "v0.1.0"
commit: "490cea1e1a7e1a1159e265316b7154a3beb409ae"
version: "cf9b51217a5e23800548f3c22635a7ca"
build_date: "2018-05-13T10:34:42.468Z"
size_mb: 1988
size: 906280991
sif: "https://datasets.datalad.org/shub/TheEtkinLab/ndmg/v0.1.0/2018-05-13-490cea1e-cf9b5121/cf9b51217a5e23800548f3c22635a7ca.simg"
url: https://datasets.datalad.org/shub/TheEtkinLab/ndmg/v0.1.0/2018-05-13-490cea1e-cf9b5121/
recipe: https://datasets.datalad.org/shub/TheEtkinLab/ndmg/v0.1.0/2018-05-13-490cea1e-cf9b5121/Singularity
collection: TheEtkinLab/ndmg
---

# TheEtkinLab/ndmg:v0.1.0

```bash
$ singularity pull shub://TheEtkinLab/ndmg:v0.1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bids/ndmg

%help
You are in the BIDS-ndmg container. To see help run
singularity run TheEtkinLab-ndmg.simg -h

%runscript
    echo "Running ndmg!"
    echo "Arguments received: $*"
    exec ndmg_bids "$@"

%labels
Author mnarayan@users.noreply.github.com
Build-date 10/05/2018
Vendor Ubuntu
Version v0.1.0

%post
    echo "Hello from inside the ndmg container"
    echo "Install additional software here"
```

## Collection

 - Name: [TheEtkinLab/ndmg](https://github.com/TheEtkinLab/ndmg)
 - License: None

