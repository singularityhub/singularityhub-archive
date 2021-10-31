---
id: 762
name: "patrickvdb/fastqc-singularity"
branch: "master"
tag: "latest"
commit: "f25a39057044509408cb4fde59d633f6c4c34bc3"
version: "f5277d7bfdf865c5a120e91a7ee68d6f"
build_date: "2019-07-26T16:12:19.066Z"
size_mb: 640
size: 242245663
sif: "https://datasets.datalad.org/shub/patrickvdb/fastqc-singularity/latest/2019-07-26-f25a3905-f5277d7b/f5277d7bfdf865c5a120e91a7ee68d6f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/patrickvdb/fastqc-singularity/latest/2019-07-26-f25a3905-f5277d7b/
recipe: https://datasets.datalad.org/shub/patrickvdb/fastqc-singularity/latest/2019-07-26-f25a3905-f5277d7b/Singularity
collection: patrickvdb/fastqc-singularity
---

# patrickvdb/fastqc-singularity:latest

```bash
$ singularity pull shub://patrickvdb/fastqc-singularity:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:genomicpariscentre/fastqc

%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/fastqc-singularity](https://github.com/patrickvdb/fastqc-singularity)
 - License: None

