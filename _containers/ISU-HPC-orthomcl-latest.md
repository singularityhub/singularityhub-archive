---
id: 2595
name: "ISU-HPC/orthomcl"
branch: "master"
tag: "latest"
commit: "169ff2a77d0c2291009548319c86ad3f92152f78"
version: "39caa4719a738aef71de8504b9491447"
build_date: "2021-03-17T02:34:45.265Z"
size_mb: 527
size: 202207263
sif: "https://datasets.datalad.org/shub/ISU-HPC/orthomcl/latest/2021-03-17-169ff2a7-39caa471/39caa4719a738aef71de8504b9491447.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/orthomcl/latest/2021-03-17-169ff2a7-39caa471/
recipe: https://datasets.datalad.org/shub/ISU-HPC/orthomcl/latest/2021-03-17-169ff2a7-39caa471/Singularity
collection: ISU-HPC/orthomcl
---

# ISU-HPC/orthomcl:latest

```bash
$ singularity pull shub://ISU-HPC/orthomcl:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: granek/orthomcl

%help
A containerized version of OrthoMCL.
Documentation: https://www.hpc.iastate.edu/guides/containers


%labels
    Maintainer Iowa State University High-Performance Computing Group
    Version  v1.0
```

## Collection

 - Name: [ISU-HPC/orthomcl](https://github.com/ISU-HPC/orthomcl)
 - License: None

