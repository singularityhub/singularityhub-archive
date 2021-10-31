---
id: 6582
name: "GuanJ-H/booster_icsaci"
branch: "master"
tag: "rec"
commit: "05c915a866d1d83b2a1f10b66608cdbda0a8dc0f"
version: "794bf1b436e169a048f08f449246692e"
build_date: "2019-01-26T22:48:03.214Z"
size_mb: 98
size: 37613599
sif: "https://datasets.datalad.org/shub/GuanJ-H/booster_icsaci/rec/2019-01-26-05c915a8-794bf1b4/794bf1b436e169a048f08f449246692e.simg"
url: https://datasets.datalad.org/shub/GuanJ-H/booster_icsaci/rec/2019-01-26-05c915a8-794bf1b4/
recipe: https://datasets.datalad.org/shub/GuanJ-H/booster_icsaci/rec/2019-01-26-05c915a8-794bf1b4/Singularity
collection: GuanJ-H/booster_icsaci
---

# GuanJ-H/booster_icsaci:rec

```bash
$ singularity pull shub://GuanJ-H/booster_icsaci:rec
```

## Singularity Recipe

```singularity
# booster from evolbioinfo

BootStrap: docker
From: evolbioinfo/booster

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

 - Name: [GuanJ-H/booster_icsaci](https://github.com/GuanJ-H/booster_icsaci)
 - License: None

