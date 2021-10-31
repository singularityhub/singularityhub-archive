---
id: 8343
name: "pndni/Charge_GM_WM_Properties_Pipeline"
branch: "1.0.0-alpha7"
tag: "1.0.0-alpha7"
commit: "2d2bfc4a6f9507ceb7c9269c3c61e06c3ea302d4"
version: "867e33508680500721322140f3034d1f"
build_date: "2019-04-10T18:24:18.776Z"
size_mb: 23303
size: 9584168991
sif: "https://datasets.datalad.org/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha7/2019-04-10-2d2bfc4a-867e3350/867e33508680500721322140f3034d1f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha7/2019-04-10-2d2bfc4a-867e3350/
recipe: https://datasets.datalad.org/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha7/2019-04-10-2d2bfc4a-867e3350/Singularity
collection: pndni/Charge_GM_WM_Properties_Pipeline
---

# pndni/Charge_GM_WM_Properties_Pipeline:1.0.0-alpha7

```bash
$ singularity pull shub://pndni/Charge_GM_WM_Properties_Pipeline:1.0.0-alpha7
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
    Version 1.0.0-alpha7
```

## Collection

 - Name: [pndni/Charge_GM_WM_Properties_Pipeline](https://github.com/pndni/Charge_GM_WM_Properties_Pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

