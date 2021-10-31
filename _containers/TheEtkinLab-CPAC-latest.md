---
id: 850
name: "TheEtkinLab/CPAC"
branch: "master"
tag: "latest"
commit: "ad89c1fb84da15891d9756a8034e93591136287f"
version: "5ef624efe2717537834991216e9c75c4"
build_date: "2017-11-20T13:56:11.809Z"
size_mb: 3508
size: 1499508767
sif: "https://datasets.datalad.org/shub/TheEtkinLab/CPAC/latest/2017-11-20-ad89c1fb-5ef624ef/5ef624efe2717537834991216e9c75c4.simg"
url: https://datasets.datalad.org/shub/TheEtkinLab/CPAC/latest/2017-11-20-ad89c1fb-5ef624ef/
recipe: https://datasets.datalad.org/shub/TheEtkinLab/CPAC/latest/2017-11-20-ad89c1fb-5ef624ef/Singularity
collection: TheEtkinLab/CPAC
---

# TheEtkinLab/CPAC:latest

```bash
$ singularity pull shub://TheEtkinLab/CPAC:latest
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
Build-date 03/11/2017
Vendor Ubuntu
Version 1.0.1b

%post
    echo "Hello from inside the C-PAC container"
    echo "Install additional software here"
```

## Collection

 - Name: [TheEtkinLab/CPAC](https://github.com/TheEtkinLab/CPAC)
 - License: None

