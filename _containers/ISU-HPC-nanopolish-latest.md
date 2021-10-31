---
id: 10068
name: "ISU-HPC/nanopolish"
branch: "master"
tag: "latest"
commit: "fe47e0a3f0e9e7e70003f1041719db91a33fc125"
version: "094762bcee768a6f87597ebc84a5ed3b"
build_date: "2019-06-28T22:40:05.595Z"
size_mb: 969
size: 310448159
sif: "https://datasets.datalad.org/shub/ISU-HPC/nanopolish/latest/2019-06-28-fe47e0a3-094762bc/094762bcee768a6f87597ebc84a5ed3b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/nanopolish/latest/2019-06-28-fe47e0a3-094762bc/
recipe: https://datasets.datalad.org/shub/ISU-HPC/nanopolish/latest/2019-06-28-fe47e0a3-094762bc/Singularity
collection: ISU-HPC/nanopolish
---

# ISU-HPC/nanopolish:latest

```bash
$ singularity pull shub://ISU-HPC/nanopolish:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ttubb/nanopolish:latest

%labels
Maintainer ynanyam@iastate.edu

%post

# The original maintainer overlooked the permissions on some scripts

#chmod a+x /software/nanopolish/scripts/*
#sed -i '1i#!/usr/bin/env python3' /software/nanopolish/scripts/nanopolish_merge.py
```

## Collection

 - Name: [ISU-HPC/nanopolish](https://github.com/ISU-HPC/nanopolish)
 - License: None

