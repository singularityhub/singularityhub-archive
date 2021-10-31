---
id: 11614
name: "FCP-INDI/C-PAC"
branch: "master"
tag: "latest"
commit: "0926b451dd8622b25eb68c7bcc770f0156238b23"
version: "8c3a2d47d79caadf889756e05179f9a0"
build_date: "2021-04-19T00:45:41.899Z"
size_mb: 9738.0
size: 4519936031
sif: "https://datasets.datalad.org/shub/FCP-INDI/C-PAC/latest/2021-04-19-0926b451-8c3a2d47/8c3a2d47d79caadf889756e05179f9a0.sif"
url: https://datasets.datalad.org/shub/FCP-INDI/C-PAC/latest/2021-04-19-0926b451-8c3a2d47/
recipe: https://datasets.datalad.org/shub/FCP-INDI/C-PAC/latest/2021-04-19-0926b451-8c3a2d47/Singularity
collection: FCP-INDI/C-PAC
---

# FCP-INDI/C-PAC:latest

```bash
$ singularity pull shub://FCP-INDI/C-PAC:latest
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

 - Name: [FCP-INDI/C-PAC](https://github.com/FCP-INDI/C-PAC)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

