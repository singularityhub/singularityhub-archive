---
id: 6432
name: "rohinijoshi06/LOFARSoftware"
branch: "master"
tag: "latest"
commit: "8f92594aa9685f5858208c85d897787dc69456ea"
version: "71a8f84b3df59552b6efc832f23b8d6a"
build_date: "2019-08-01T14:42:02.383Z"
size_mb: 2043
size: 663617567
sif: "https://datasets.datalad.org/shub/rohinijoshi06/LOFARSoftware/latest/2019-08-01-8f92594a-71a8f84b/71a8f84b3df59552b6efc832f23b8d6a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rohinijoshi06/LOFARSoftware/latest/2019-08-01-8f92594a-71a8f84b/
recipe: https://datasets.datalad.org/shub/rohinijoshi06/LOFARSoftware/latest/2019-08-01-8f92594a-71a8f84b/Singularity
collection: rohinijoshi06/LOFARSoftware
---

# rohinijoshi06/LOFARSoftware:latest

```bash
$ singularity pull shub://rohinijoshi06/LOFARSoftware:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: lofaruser/imaging-pipeline:latest

%post


%runscript
  # For debugging purposes
  printenv
  # Sanity check for LOFAR s/w
  source  /lofarsoft/lofarinit.sh
  genericpipeline.py -h
```

## Collection

 - Name: [rohinijoshi06/LOFARSoftware](https://github.com/rohinijoshi06/LOFARSoftware)
 - License: None

