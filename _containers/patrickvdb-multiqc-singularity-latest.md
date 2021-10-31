---
id: 4704
name: "patrickvdb/multiqc-singularity"
branch: "master"
tag: "latest"
commit: "c1f01c03a52bffd279a10d1d1e8927ddf0f51b16"
version: "84ecb9cd74fcca0dbbaf4f4131d01dc1"
build_date: "2018-09-07T21:20:10.515Z"
size_mb: 2102
size: 916516895
sif: "https://datasets.datalad.org/shub/patrickvdb/multiqc-singularity/latest/2018-09-07-c1f01c03-84ecb9cd/84ecb9cd74fcca0dbbaf4f4131d01dc1.simg"
url: https://datasets.datalad.org/shub/patrickvdb/multiqc-singularity/latest/2018-09-07-c1f01c03-84ecb9cd/
recipe: https://datasets.datalad.org/shub/patrickvdb/multiqc-singularity/latest/2018-09-07-c1f01c03-84ecb9cd/Singularity
collection: patrickvdb/multiqc-singularity
---

# patrickvdb/multiqc-singularity:latest

```bash
$ singularity pull shub://patrickvdb/multiqc-singularity:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:pvdb90/multiqc:v1.3

%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/multiqc-singularity](https://github.com/patrickvdb/multiqc-singularity)
 - License: None

