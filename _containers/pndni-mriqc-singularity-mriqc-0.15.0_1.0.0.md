---
id: 8714
name: "pndni/mriqc-singularity"
branch: "master"
tag: "mriqc-0.15.0_1.0.0"
commit: "7b7f28328d683d978524e80e277c2d9cbc97cd9c"
version: "c388dba210896700d946b290259f8bea"
build_date: "2019-04-29T20:57:19.698Z"
size_mb: 7589
size: 2928963615
sif: "https://datasets.datalad.org/shub/pndni/mriqc-singularity/mriqc-0.15.0_1.0.0/2019-04-29-7b7f2832-c388dba2/c388dba210896700d946b290259f8bea.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/mriqc-singularity/mriqc-0.15.0_1.0.0/2019-04-29-7b7f2832-c388dba2/
recipe: https://datasets.datalad.org/shub/pndni/mriqc-singularity/mriqc-0.15.0_1.0.0/2019-04-29-7b7f2832-c388dba2/Singularity
collection: pndni/mriqc-singularity
---

# pndni/mriqc-singularity:mriqc-0.15.0_1.0.0

```bash
$ singularity pull shub://pndni/mriqc-singularity:mriqc-0.15.0_1.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: poldracklab/mriqc:0.15.0

%post
    mkdir /data
    mkdir /out
```

## Collection

 - Name: [pndni/mriqc-singularity](https://github.com/pndni/mriqc-singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

