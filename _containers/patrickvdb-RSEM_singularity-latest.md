---
id: 756
name: "patrickvdb/RSEM_singularity"
branch: "master"
tag: "latest"
commit: "a4f2d94e3589403f4b173c170bde34298c33f4b8"
version: "069f7336214fca6e477c4f275fa9d0d5"
build_date: "2018-09-07T16:02:59.934Z"
size_mb: 1000
size: 395223071
sif: "https://datasets.datalad.org/shub/patrickvdb/RSEM_singularity/latest/2018-09-07-a4f2d94e-069f7336/069f7336214fca6e477c4f275fa9d0d5.simg"
url: https://datasets.datalad.org/shub/patrickvdb/RSEM_singularity/latest/2018-09-07-a4f2d94e-069f7336/
recipe: https://datasets.datalad.org/shub/patrickvdb/RSEM_singularity/latest/2018-09-07-a4f2d94e-069f7336/Singularity
collection: patrickvdb/RSEM_singularity
---

# patrickvdb/RSEM_singularity:latest

```bash
$ singularity pull shub://patrickvdb/RSEM_singularity:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:biowardrobe2/rsem:v1.3.0


%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/RSEM_singularity](https://github.com/patrickvdb/RSEM_singularity)
 - License: None

