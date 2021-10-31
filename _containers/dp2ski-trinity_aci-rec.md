---
id: 6811
name: "dp2ski/trinity_aci"
branch: "master"
tag: "rec"
commit: "277caa9bcc5a4d939ca9aeced5c6a3f61505f760"
version: "678525e94d048046a40c3b0d6d81409d"
build_date: "2019-02-01T19:07:43.727Z"
size_mb: 4724
size: 1867632671
sif: "https://datasets.datalad.org/shub/dp2ski/trinity_aci/rec/2019-02-01-277caa9b-678525e9/678525e94d048046a40c3b0d6d81409d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dp2ski/trinity_aci/rec/2019-02-01-277caa9b-678525e9/
recipe: https://datasets.datalad.org/shub/dp2ski/trinity_aci/rec/2019-02-01-277caa9b-678525e9/Singularity
collection: dp2ski/trinity_aci
---

# dp2ski/trinity_aci:rec

```bash
$ singularity pull shub://dp2ski/trinity_aci:rec
```

## Singularity Recipe

```singularity
BootStrap: docker
From: trinityrnaseq/trinityrnaseq

%runscript
    exec /usr/local/bin/trinityrnaseq/Trinity "$@"

%post
    #ACI mappings
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/group
    mkdir -p /gpfs/scratch
    mkdir -p /var/spool/torque
```

## Collection

 - Name: [dp2ski/trinity_aci](https://github.com/dp2ski/trinity_aci)
 - License: None

