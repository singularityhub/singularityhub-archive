---
id: 757
name: "patrickvdb/drop-seq_singularity"
branch: "master"
tag: "latest"
commit: "78530032c9438931e34a045bd83cab9a6f84b874"
version: "d8e45b9bd955e38bf138bc025ea8db15"
build_date: "2017-11-09T14:26:04.449Z"
size_mb: 1055
size: 509796383
sif: "https://datasets.datalad.org/shub/patrickvdb/drop-seq_singularity/latest/2017-11-09-78530032-d8e45b9b/d8e45b9bd955e38bf138bc025ea8db15.simg"
url: https://datasets.datalad.org/shub/patrickvdb/drop-seq_singularity/latest/2017-11-09-78530032-d8e45b9b/
recipe: https://datasets.datalad.org/shub/patrickvdb/drop-seq_singularity/latest/2017-11-09-78530032-d8e45b9b/Singularity
collection: patrickvdb/drop-seq_singularity
---

# patrickvdb/drop-seq_singularity:latest

```bash
$ singularity pull shub://patrickvdb/drop-seq_singularity:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:pvdb90/drop-seq-tools


%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/drop-seq_singularity](https://github.com/patrickvdb/drop-seq_singularity)
 - License: None

