---
id: 4740
name: "patrickvdb/RNAseq_tools"
branch: "master"
tag: "v1.0"
commit: "117b94b4fde11272381ca51a19f9f6d04c29c513"
version: "7a068c968fc47cf8263880891ec5f961"
build_date: "2018-10-09T10:11:50.126Z"
size_mb: 2317
size: 957169695
sif: "https://datasets.datalad.org/shub/patrickvdb/RNAseq_tools/v1.0/2018-10-09-117b94b4-7a068c96/7a068c968fc47cf8263880891ec5f961.simg"
url: https://datasets.datalad.org/shub/patrickvdb/RNAseq_tools/v1.0/2018-10-09-117b94b4-7a068c96/
recipe: https://datasets.datalad.org/shub/patrickvdb/RNAseq_tools/v1.0/2018-10-09-117b94b4-7a068c96/Singularity
collection: patrickvdb/RNAseq_tools
---

# patrickvdb/RNAseq_tools:v1.0

```bash
$ singularity pull shub://patrickvdb/RNAseq_tools:v1.0
```

## Singularity Recipe

```singularity
bootstrap:docker
From:pvdb90/rnaseq_tools:v1.0


%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/RNAseq_tools](https://github.com/patrickvdb/RNAseq_tools)
 - License: None

