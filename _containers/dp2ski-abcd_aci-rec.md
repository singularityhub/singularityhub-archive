---
id: 7747
name: "dp2ski/abcd_aci"
branch: "master"
tag: "rec"
commit: "c5f02b628b1c1f53c6354bbc3f5c9eca6b6729a2"
version: "7d3cd620ea4d050e56a680b124df6263"
build_date: "2019-04-13T15:19:00.787Z"
size_mb: 13634
size: 5931180063
sif: "https://datasets.datalad.org/shub/dp2ski/abcd_aci/rec/2019-04-13-c5f02b62-7d3cd620/7d3cd620ea4d050e56a680b124df6263.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dp2ski/abcd_aci/rec/2019-04-13-c5f02b62-7d3cd620/
recipe: https://datasets.datalad.org/shub/dp2ski/abcd_aci/rec/2019-04-13-c5f02b62-7d3cd620/Singularity
collection: dp2ski/abcd_aci
---

# dp2ski/abcd_aci:rec

```bash
$ singularity pull shub://dp2ski/abcd_aci:rec
```

## Singularity Recipe

```singularity
# FMRIPREP from dcanlabs
# docker image converted to ubuntu 16 to work with aci systems

BootStrap: docker
From: dp2ski/abcd_ubuntu16:0.0.1
#DCAN lab pushed a hotfix in 0.0.1 for running with singularity

%runscript
    /app/SetupEnv.sh
    cd /tmp
    exec python3 /app/run.py "$@"

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
```

## Collection

 - Name: [dp2ski/abcd_aci](https://github.com/dp2ski/abcd_aci)
 - License: None

