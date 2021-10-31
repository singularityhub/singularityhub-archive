---
id: 8596
name: "pndni/Charge_GM_WM_Properties_Pipeline"
branch: "master"
tag: "dev"
commit: "bcdc3533cc8b5ce7d5402a71edc5001774876f0f"
version: "926f7556f9916b4ca7c421047be6dcf8"
build_date: "2019-04-23T20:55:38.184Z"
size_mb: 23303
size: 9584168991
sif: "https://datasets.datalad.org/shub/pndni/Charge_GM_WM_Properties_Pipeline/dev/2019-04-23-bcdc3533-926f7556/926f7556f9916b4ca7c421047be6dcf8.simg"
url: https://datasets.datalad.org/shub/pndni/Charge_GM_WM_Properties_Pipeline/dev/2019-04-23-bcdc3533-926f7556/
recipe: https://datasets.datalad.org/shub/pndni/Charge_GM_WM_Properties_Pipeline/dev/2019-04-23-bcdc3533-926f7556/Singularity
collection: pndni/Charge_GM_WM_Properties_Pipeline
---

# pndni/Charge_GM_WM_Properties_Pipeline:dev

```bash
$ singularity pull shub://pndni/Charge_GM_WM_Properties_Pipeline:dev
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/FSL-and-freesurfer:fsl-6.0.1_freesurfer-6.0.1_1.0.1


%appinstall
    mkdir -p /mnt
    mkdir -p /mnt/outdir
    mkdir -p /mnt/indir
    
%appfiles charge
    scripts
    utils
    models
    QC

%appenv charge
    source $SCIF_APPENV_all
    CHARGEDIR=$SCIF_APPROOT_charge
    export CHARGEDIR

%apprun charge
    /bin/bash $CHARGEDIR/scripts/pipeline.sh "$@"

%labels
    Maintainer Steven Tilley
    Version dev
```

## Collection

 - Name: [pndni/Charge_GM_WM_Properties_Pipeline](https://github.com/pndni/Charge_GM_WM_Properties_Pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

