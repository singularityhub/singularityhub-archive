---
id: 8597
name: "pndni/Charge_GM_WM_Properties_Pipeline"
branch: "1.0.0-alpha8"
tag: "1.0.0-alpha8"
commit: "e3208cd0ce28a553a564319e4ba3b03aace7638f"
version: "645f03d83b942789d97808a4cba061af"
build_date: "2019-04-23T20:55:38.177Z"
size_mb: 23303
size: 9584168991
sif: "https://datasets.datalad.org/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha8/2019-04-23-e3208cd0-645f03d8/645f03d83b942789d97808a4cba061af.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha8/2019-04-23-e3208cd0-645f03d8/
recipe: https://datasets.datalad.org/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha8/2019-04-23-e3208cd0-645f03d8/Singularity
collection: pndni/Charge_GM_WM_Properties_Pipeline
---

# pndni/Charge_GM_WM_Properties_Pipeline:1.0.0-alpha8

```bash
$ singularity pull shub://pndni/Charge_GM_WM_Properties_Pipeline:1.0.0-alpha8
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
    Version 1.0.0-alpha8
```

## Collection

 - Name: [pndni/Charge_GM_WM_Properties_Pipeline](https://github.com/pndni/Charge_GM_WM_Properties_Pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

