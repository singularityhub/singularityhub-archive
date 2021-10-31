---
id: 11108
name: "OSC/sa_singularity_iqmol"
branch: "master"
tag: "latest"
commit: "e594f7356925617a72e0e4e828ee603e61e397f6"
version: "bd827017d46fec3ad2d9bc1735ebec3f"
build_date: "2020-09-02T03:57:55.145Z"
size_mb: 462.0
size: 142839839
sif: "https://datasets.datalad.org/shub/OSC/sa_singularity_iqmol/latest/2020-09-02-e594f735-bd827017/bd827017d46fec3ad2d9bc1735ebec3f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/OSC/sa_singularity_iqmol/latest/2020-09-02-e594f735-bd827017/
recipe: https://datasets.datalad.org/shub/OSC/sa_singularity_iqmol/latest/2020-09-02-e594f735-bd827017/Singularity
collection: OSC/sa_singularity_iqmol
---

# OSC/sa_singularity_iqmol:latest

```bash
$ singularity pull shub://OSC/sa_singularity_iqmol:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%labels
    Maintainer zyou@osc.edu
    Recipe https://github.com/OSC/sa_singularity_iqmol

%environment
    export QC=/opt/qchem
    export QCAUX=$QC/qcaux
    export QCPROG_S=$QC/exe/qcprog.exe_s
    export QCMPI=mpich3
    export QCRSH=ssh
    export PATH=$PATH:$QC/exe:$QC/bin
    export QCSCRATCH=$TMPDIR

%post
    apt update
    apt upgrade -y
    apt install -y wget
    wget -nc http://iqmol.org/download.php?get=iqmol_2.14.deb -O iqmol.deb
    DEBIAN_FRONTEND=noninteractive dpkg -i iqmol.deb || true
    DEBIAN_FRONTEND=noninteractive apt install -f -y
    DEBIAN_FRONTEND=noninteractive dpkg -i iqmol.deb
    rm -f iqmol.deb
    apt autoclean
    apt autoremove --purge -y
    rm -rf /var/lib/apt/lists/*

%runscript
    exec iqmol "$@"
```

## Collection

 - Name: [OSC/sa_singularity_iqmol](https://github.com/OSC/sa_singularity_iqmol)
 - License: [MIT License](https://api.github.com/licenses/mit)

