---
id: 788
name: "patrickvdb/SNPsplit-singularity"
branch: "master"
tag: "latest"
commit: "b10baa8d1576c04dca93c85e114e9f22dbf1361f"
version: "5c86e327fcd2ed28add8a3329ff790c8"
build_date: "2017-11-13T21:32:38.522Z"
size_mb: 1153
size: 397996063
sif: "https://datasets.datalad.org/shub/patrickvdb/SNPsplit-singularity/latest/2017-11-13-b10baa8d-5c86e327/5c86e327fcd2ed28add8a3329ff790c8.simg"
url: https://datasets.datalad.org/shub/patrickvdb/SNPsplit-singularity/latest/2017-11-13-b10baa8d-5c86e327/
recipe: https://datasets.datalad.org/shub/patrickvdb/SNPsplit-singularity/latest/2017-11-13-b10baa8d-5c86e327/Singularity
collection: patrickvdb/SNPsplit-singularity
---

# patrickvdb/SNPsplit-singularity:latest

```bash
$ singularity pull shub://patrickvdb/SNPsplit-singularity:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:pvdb90/snpsplit-docker:0.3.2


%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/SNPsplit-singularity](https://github.com/patrickvdb/SNPsplit-singularity)
 - License: None

