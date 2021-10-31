---
id: 15703
name: "shnizzedy/C-PAC"
branch: "master"
tag: "latest"
commit: "70346dccca6eaf7b3361a34e0530cc4f56e7db79"
version: "d44b0a51c5c05029701f7d2aa38ad431"
build_date: "2021-03-15T15:20:14.768Z"
size_mb: 9738.0
size: 4519936031
sif: "https://datasets.datalad.org/shub/shnizzedy/C-PAC/latest/2021-03-15-70346dcc-d44b0a51/d44b0a51c5c05029701f7d2aa38ad431.sif"
url: https://datasets.datalad.org/shub/shnizzedy/C-PAC/latest/2021-03-15-70346dcc-d44b0a51/
recipe: https://datasets.datalad.org/shub/shnizzedy/C-PAC/latest/2021-03-15-70346dcc-d44b0a51/Singularity
collection: shnizzedy/C-PAC
---

# shnizzedy/C-PAC:latest

```bash
$ singularity pull shub://shnizzedy/C-PAC:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fcpindi/c-pac
IncludeCmd: yes

%environment
FREESURFER_HOME=/usr/lib/freesurfer

%post
```

## Collection

 - Name: [shnizzedy/C-PAC](https://github.com/shnizzedy/C-PAC)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

