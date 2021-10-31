---
id: 4195
name: "MPIB/singularity-mriqc"
branch: "master"
tag: "0.14.2"
commit: "57eeaa9d732b8b71dc1104fc20141f368ed9bfd6"
version: "0238f7b8623a91a27bc5989ce3007639"
build_date: "2019-12-18T19:14:37.635Z"
size_mb: 7316
size: 2814226463
sif: "https://datasets.datalad.org/shub/MPIB/singularity-mriqc/0.14.2/2019-12-18-57eeaa9d-0238f7b8/0238f7b8623a91a27bc5989ce3007639.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MPIB/singularity-mriqc/0.14.2/2019-12-18-57eeaa9d-0238f7b8/
recipe: https://datasets.datalad.org/shub/MPIB/singularity-mriqc/0.14.2/2019-12-18-57eeaa9d-0238f7b8/Singularity
collection: MPIB/singularity-mriqc
---

# MPIB/singularity-mriqc:0.14.2

```bash
$ singularity pull shub://MPIB/singularity-mriqc:0.14.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: poldracklab/mriqc:0.14.2




%post
    apt-get update && apt-get -y purge libgsl2 && apt-get -y  install libgsl2
```

## Collection

 - Name: [MPIB/singularity-mriqc](https://github.com/MPIB/singularity-mriqc)
 - License: None

