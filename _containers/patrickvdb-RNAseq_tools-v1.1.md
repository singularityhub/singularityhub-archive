---
id: 5179
name: "patrickvdb/RNAseq_tools"
branch: "master"
tag: "v1.1"
commit: "d74ee17f6e8f45faea0d31caa95520f8d5c37cef"
version: "7c6517f415c9953f4078ab50b8ac5687"
build_date: "2018-10-09T10:11:50.120Z"
size_mb: 3566
size: 1524387871
sif: "https://datasets.datalad.org/shub/patrickvdb/RNAseq_tools/v1.1/2018-10-09-d74ee17f-7c6517f4/7c6517f415c9953f4078ab50b8ac5687.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/patrickvdb/RNAseq_tools/v1.1/2018-10-09-d74ee17f-7c6517f4/
recipe: https://datasets.datalad.org/shub/patrickvdb/RNAseq_tools/v1.1/2018-10-09-d74ee17f-7c6517f4/Singularity
collection: patrickvdb/RNAseq_tools
---

# patrickvdb/RNAseq_tools:v1.1

```bash
$ singularity pull shub://patrickvdb/RNAseq_tools:v1.1
```

## Singularity Recipe

```singularity
bootstrap:docker
From:pvdb90/rnaseq_tools:v1.1


%post
  mkdir -p /cvmfs /scratch /tmpdir /scratch-shared /scratch-local /hpc /projects /lustre1 /lustre2 /lustre4
```

## Collection

 - Name: [patrickvdb/RNAseq_tools](https://github.com/patrickvdb/RNAseq_tools)
 - License: None

