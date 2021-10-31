---
id: 7581
name: "jpetucci/abcd_hpc-icsaci"
branch: "master"
tag: "rec"
commit: "09fdddf8c1a2231f65b684d410348ab133647734"
version: "a38bc1532334f27d9873c5a9c186f652"
build_date: "2019-03-12T15:09:01.714Z"
size_mb: 13608
size: 5907972127
sif: "https://datasets.datalad.org/shub/jpetucci/abcd_hpc-icsaci/rec/2019-03-12-09fdddf8-a38bc153/a38bc1532334f27d9873c5a9c186f652.simg"
url: https://datasets.datalad.org/shub/jpetucci/abcd_hpc-icsaci/rec/2019-03-12-09fdddf8-a38bc153/
recipe: https://datasets.datalad.org/shub/jpetucci/abcd_hpc-icsaci/rec/2019-03-12-09fdddf8-a38bc153/Singularity
collection: jpetucci/abcd_hpc-icsaci
---

# jpetucci/abcd_hpc-icsaci:rec

```bash
$ singularity pull shub://jpetucci/abcd_hpc-icsaci:rec
```

## Singularity Recipe

```singularity
# FMRIPREP from dcanlabs

BootStrap: docker
From: dcanlabs/abcd-hcp-pipeline:latest

%runscript
    exec "/entrypoint.sh" "$@"

%environment

%post
    #------------------------------------------------------------------------------
    # Create local binding points for our ICS-ACI
    #------------------------------------------------------------------------------
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
#
```

## Collection

 - Name: [jpetucci/abcd_hpc-icsaci](https://github.com/jpetucci/abcd_hpc-icsaci)
 - License: None

