---
id: 818
name: "patrickvdb/trimmomatic_singularity"
branch: "master"
tag: "latest"
commit: "c956ddf1d860d9ac4a7ca8fc78ab23b164487b49"
version: "c078a74435f0d8abf9f3c7e1abb8ffc8"
build_date: "2021-03-16T12:15:13.653Z"
size_mb: 432
size: 121258015
sif: "https://datasets.datalad.org/shub/patrickvdb/trimmomatic_singularity/latest/2021-03-16-c956ddf1-c078a744/c078a74435f0d8abf9f3c7e1abb8ffc8.simg"
url: https://datasets.datalad.org/shub/patrickvdb/trimmomatic_singularity/latest/2021-03-16-c956ddf1-c078a744/
recipe: https://datasets.datalad.org/shub/patrickvdb/trimmomatic_singularity/latest/2021-03-16-c956ddf1-c078a744/Singularity
collection: patrickvdb/trimmomatic_singularity
---

# patrickvdb/trimmomatic_singularity:latest

```bash
$ singularity pull shub://patrickvdb/trimmomatic_singularity:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:pvdb90/trimmomatic



%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/trimmomatic_singularity](https://github.com/patrickvdb/trimmomatic_singularity)
 - License: None

