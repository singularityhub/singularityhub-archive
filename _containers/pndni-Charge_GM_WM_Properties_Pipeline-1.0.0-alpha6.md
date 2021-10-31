---
id: 8327
name: "pndni/Charge_GM_WM_Properties_Pipeline"
branch: "1.0.0-alpha6"
tag: "1.0.0-alpha6"
commit: "24718d34dc0dcc648ea6589ba36480c7c3c7f0b2"
version: "8e3cbe8fce2b1b33dd4fd11b3967c55c"
build_date: "2019-04-10T18:24:18.782Z"
size_mb: 23303
size: 9584168991
sif: "https://datasets.datalad.org/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha6/2019-04-10-24718d34-8e3cbe8f/8e3cbe8fce2b1b33dd4fd11b3967c55c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha6/2019-04-10-24718d34-8e3cbe8f/
recipe: https://datasets.datalad.org/shub/pndni/Charge_GM_WM_Properties_Pipeline/1.0.0-alpha6/2019-04-10-24718d34-8e3cbe8f/Singularity
collection: pndni/Charge_GM_WM_Properties_Pipeline
---

# pndni/Charge_GM_WM_Properties_Pipeline:1.0.0-alpha6

```bash
$ singularity pull shub://pndni/Charge_GM_WM_Properties_Pipeline:1.0.0-alpha6
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
    Version 1.0.0-alpha6
```

## Collection

 - Name: [pndni/Charge_GM_WM_Properties_Pipeline](https://github.com/pndni/Charge_GM_WM_Properties_Pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

