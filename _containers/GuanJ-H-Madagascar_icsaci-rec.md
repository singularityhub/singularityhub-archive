---
id: 7560
name: "GuanJ-H/Madagascar_icsaci"
branch: "master"
tag: "rec"
commit: "9024fe95d0fbbd253bc76499af12c45706d82505"
version: "e8d4c6e196350ffc12afe7dd916e7770"
build_date: "2019-03-01T19:49:14.189Z"
size_mb: 1383
size: 545251359
sif: "https://datasets.datalad.org/shub/GuanJ-H/Madagascar_icsaci/rec/2019-03-01-9024fe95-e8d4c6e1/e8d4c6e196350ffc12afe7dd916e7770.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GuanJ-H/Madagascar_icsaci/rec/2019-03-01-9024fe95-e8d4c6e1/
recipe: https://datasets.datalad.org/shub/GuanJ-H/Madagascar_icsaci/rec/2019-03-01-9024fe95-e8d4c6e1/Singularity
collection: GuanJ-H/Madagascar_icsaci
---

# GuanJ-H/Madagascar_icsaci:rec

```bash
$ singularity pull shub://GuanJ-H/Madagascar_icsaci:rec
```

## Singularity Recipe

```singularity
# booster from madagascar

BootStrap: docker
From: jdrew/madagascar

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

 - Name: [GuanJ-H/Madagascar_icsaci](https://github.com/GuanJ-H/Madagascar_icsaci)
 - License: None

