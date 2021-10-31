---
id: 2250
name: "TheEtkinLab/CPAC"
branch: "master"
tag: "v1.0.3"
commit: "871f75dcf72392547e74c39dfb16a87961f43760"
version: "6662e1b39cf703840031202981aa2507"
build_date: "2018-03-25T21:23:38.193Z"
size_mb: 3616
size: 1499508767
sif: "https://datasets.datalad.org/shub/TheEtkinLab/CPAC/v1.0.3/2018-03-25-871f75dc-6662e1b3/6662e1b39cf703840031202981aa2507.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TheEtkinLab/CPAC/v1.0.3/2018-03-25-871f75dc-6662e1b3/
recipe: https://datasets.datalad.org/shub/TheEtkinLab/CPAC/v1.0.3/2018-03-25-871f75dc-6662e1b3/Singularity
collection: TheEtkinLab/CPAC
---

# TheEtkinLab/CPAC:v1.0.3

```bash
$ singularity pull shub://TheEtkinLab/CPAC:v1.0.3
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
Version 1.0.3

%post
    echo "Hello from inside the C-PAC container"
    echo "Install additional software here"
```

## Collection

 - Name: [TheEtkinLab/CPAC](https://github.com/TheEtkinLab/CPAC)
 - License: None

