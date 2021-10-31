---
id: 10948
name: "Museau/CMC_Medical_Imaging"
branch: "master"
tag: "latest"
commit: "5d8d1cadf2cf0395bfef1c0b04d86e6e32075c19"
version: "af41eafedd475a6848b6b24a9b972f22cfb6365dea633762f83bfd902118cf8a"
build_date: "2019-09-18T23:26:07.550Z"
size_mb: 1491.40234375
size: 1563848704
sif: "https://datasets.datalad.org/shub/Museau/CMC_Medical_Imaging/latest/2019-09-18-5d8d1cad-af41eafe/af41eafedd475a6848b6b24a9b972f22cfb6365dea633762f83bfd902118cf8a.sif"
url: https://datasets.datalad.org/shub/Museau/CMC_Medical_Imaging/latest/2019-09-18-5d8d1cad-af41eafe/
recipe: https://datasets.datalad.org/shub/Museau/CMC_Medical_Imaging/latest/2019-09-18-5d8d1cad-af41eafe/Singularity
collection: Museau/CMC_Medical_Imaging
---

# Museau/CMC_Medical_Imaging:latest

```bash
$ singularity pull shub://Museau/CMC_Medical_Imaging:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: pytorch/pytorch:0.4.1-cuda9-cudnn7-runtime

%environment
    export SHELL=/bin/bash
    export LC_ALL=C

%post
    apt-get update && apt-get -y dist-upgrade
    DEBIAN_FRONTEND=noninteractive apt-get install -y xorg
    apt-get clean && rm -rf /var/lib/apt/lists/*

    /opt/conda/bin/pip install scikit-image tensorboard_logger spawn

    mkdir /dataset
    mkdir /tmp_log
    mkdir /final_log

%runscript
    exec /bin/bash "$@"
```

## Collection

 - Name: [Museau/CMC_Medical_Imaging](https://github.com/Museau/CMC_Medical_Imaging)
 - License: None

