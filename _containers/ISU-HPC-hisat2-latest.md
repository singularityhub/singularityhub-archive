---
id: 7988
name: "ISU-HPC/hisat2"
branch: "master"
tag: "latest"
commit: "1361322e9aa8ad1f66a53917501780cef15391f5"
version: "04a209f5dcff1d6f9fb140629e2f69f3"
build_date: "2021-02-25T16:21:50.811Z"
size_mb: 867
size: 334467103
sif: "https://datasets.datalad.org/shub/ISU-HPC/hisat2/latest/2021-02-25-1361322e-04a209f5/04a209f5dcff1d6f9fb140629e2f69f3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/hisat2/latest/2021-02-25-1361322e-04a209f5/
recipe: https://datasets.datalad.org/shub/ISU-HPC/hisat2/latest/2021-02-25-1361322e-04a209f5/Singularity
collection: ISU-HPC/hisat2
---

# ISU-HPC/hisat2:latest

```bash
$ singularity pull shub://ISU-HPC/hisat2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: makaho/hisat2-zstd

%labels
MAINTAINER rgrandin@iastate.edu
APPLICATION hisat2

%help
This container provides hisat2

%runscript
exec hisat2 "$@"
```

## Collection

 - Name: [ISU-HPC/hisat2](https://github.com/ISU-HPC/hisat2)
 - License: None

