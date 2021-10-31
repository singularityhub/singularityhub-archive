---
id: 759
name: "patrickvdb/sequtils-singularity"
branch: "master"
tag: "latest"
commit: "84ebc8d7567a627432165bb21f5c9bfedef247ad"
version: "e535386d2a4dd408d3e2ed93237541ac"
build_date: "2017-11-09T14:26:04.477Z"
size_mb: 1862
size: 771948575
sif: "https://datasets.datalad.org/shub/patrickvdb/sequtils-singularity/latest/2017-11-09-84ebc8d7-e535386d/e535386d2a4dd408d3e2ed93237541ac.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/patrickvdb/sequtils-singularity/latest/2017-11-09-84ebc8d7-e535386d/
recipe: https://datasets.datalad.org/shub/patrickvdb/sequtils-singularity/latest/2017-11-09-84ebc8d7-e535386d/Singularity
collection: patrickvdb/sequtils-singularity
---

# patrickvdb/sequtils-singularity:latest

```bash
$ singularity pull shub://patrickvdb/sequtils-singularity:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:pvdb90/sequtils


%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/sequtils-singularity](https://github.com/patrickvdb/sequtils-singularity)
 - License: None

