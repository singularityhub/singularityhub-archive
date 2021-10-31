---
id: 4706
name: "patrickvdb/multiqc-singularity"
branch: "v1.3"
tag: "v1.3"
commit: "2dba807095967ae68faa23195ca67b87a96640bd"
version: "78231609b779f57e7613426dbbfc647c"
build_date: "2018-09-07T21:20:10.501Z"
size_mb: 2102
size: 916516895
sif: "https://datasets.datalad.org/shub/patrickvdb/multiqc-singularity/v1.3/2018-09-07-2dba8070-78231609/78231609b779f57e7613426dbbfc647c.simg"
url: https://datasets.datalad.org/shub/patrickvdb/multiqc-singularity/v1.3/2018-09-07-2dba8070-78231609/
recipe: https://datasets.datalad.org/shub/patrickvdb/multiqc-singularity/v1.3/2018-09-07-2dba8070-78231609/Singularity
collection: patrickvdb/multiqc-singularity
---

# patrickvdb/multiqc-singularity:v1.3

```bash
$ singularity pull shub://patrickvdb/multiqc-singularity:v1.3
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

