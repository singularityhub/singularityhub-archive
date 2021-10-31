---
id: 8317
name: "pndni/Charge_GM_WM_Properties_Pipeline"
branch: "1.0.0-alpha5"
tag: "1.0.0-alpha5"
commit: "5ffbd71b6746b0715c41acb868c726ec875264bb"
version: "ea1b18ace55edec0a4a2cd19a3068822"
build_date: "2019-04-10T11:51:50.880Z"
size_mb: 23303
size: 9584168991
sif: "https://datasets.datalad.org/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha5/2019-04-10-5ffbd71b-ea1b18ac/ea1b18ace55edec0a4a2cd19a3068822.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha5/2019-04-10-5ffbd71b-ea1b18ac/
recipe: https://datasets.datalad.org/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha5/2019-04-10-5ffbd71b-ea1b18ac/Singularity
collection: pndni/Charge_GM_WM_Properties_Pipeline
---

# pndni/Charge_GM_WM_Properties_Pipeline:1.0.0-alpha5

```bash
$ singularity pull shub://pndni/Charge_GM_WM_Properties_Pipeline:1.0.0-alpha5
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/FSL-and-freesurfer:fsl-6.0.1_freesurfer-6.0.1_1.0.1


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
    Version 1.0.0-alpha5
```

## Collection

 - Name: [pndni/Charge_GM_WM_Properties_Pipeline](https://github.com/pndni/Charge_GM_WM_Properties_Pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

