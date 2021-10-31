---
id: 987
name: "patrickvdb/kallisto-singularity"
branch: "v0.43.1"
tag: "latest"
commit: "0e4516987895ae0da1521bfe7f6411eb58b6fe44"
version: "0753e13e6d7e24e4c012bc187cdcbd7c"
build_date: "2017-11-28T19:11:34.824Z"
size_mb: 782
size: 330559519
sif: "https://datasets.datalad.org/shub/patrickvdb/kallisto-singularity/latest/2017-11-28-0e451698-0753e13e/0753e13e6d7e24e4c012bc187cdcbd7c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/patrickvdb/kallisto-singularity/latest/2017-11-28-0e451698-0753e13e/
recipe: https://datasets.datalad.org/shub/patrickvdb/kallisto-singularity/latest/2017-11-28-0e451698-0753e13e/Singularity
collection: patrickvdb/kallisto-singularity
---

# patrickvdb/kallisto-singularity:latest

```bash
$ singularity pull shub://patrickvdb/kallisto-singularity:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:pvdb90/kallisto:v0.43.1


%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/kallisto-singularity](https://github.com/patrickvdb/kallisto-singularity)
 - License: None

