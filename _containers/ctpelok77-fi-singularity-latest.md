---
id: 13396
name: "ctpelok77/fi-singularity"
branch: "master"
tag: "latest"
commit: "9c70e75cc56bcac8d5aa04fa71b7d9d52589bd3b"
version: "df2ed5cd6674f934110a78a1d0b07d7a"
build_date: "2021-04-06T12:26:36.437Z"
size_mb: 117.0
size: 41930783
sif: "https://datasets.datalad.org/shub/ctpelok77/fi-singularity/latest/2021-04-06-9c70e75c-df2ed5cd/df2ed5cd6674f934110a78a1d0b07d7a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ctpelok77/fi-singularity/latest/2021-04-06-9c70e75c-df2ed5cd/
recipe: https://datasets.datalad.org/shub/ctpelok77/fi-singularity/latest/2021-04-06-9c70e75c-df2ed5cd/Singularity
collection: ctpelok77/fi-singularity
---

# ctpelok77/fi-singularity:latest

```bash
$ singularity pull shub://ctpelok77/fi-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ctpelok77/forbiditerative:latest

%setup
    # Just for diagnosis purposes
    hostname -f > $SINGULARITY_ROOTFS/etc/build_host
%runscript
    # This will be called whenever the Singularity container is invoked
    python3 /workspace/forbiditerative/run.py $@

%post

## 
%labels
Name        Forbid-Iterative
Description Forbid-Iterative (FI) Planner is an Automated PDDL based planner that includes planners for top-k, top-quality, and diverse computational tasks.
Authors     Michael Katz <michael.katz1@ibm.com>
```

## Collection

 - Name: [ctpelok77/fi-singularity](https://github.com/ctpelok77/fi-singularity)
 - License: None

