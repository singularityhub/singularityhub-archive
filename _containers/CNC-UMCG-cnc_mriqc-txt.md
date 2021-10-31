---
id: 7361
name: "CNC-UMCG/cnc_mriqc"
branch: "master"
tag: "txt"
commit: "0a6d8a7918a1d215a665c51e771f7e924b9cdf93"
version: "57ab0781429927267e128cd5c8e491e8"
build_date: "2019-02-21T12:58:53.369Z"
size_mb: 7317
size: 2814734367
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_mriqc/txt/2019-02-21-0a6d8a79-57ab0781/57ab0781429927267e128cd5c8e491e8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CNC-UMCG/cnc_mriqc/txt/2019-02-21-0a6d8a79-57ab0781/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_mriqc/txt/2019-02-21-0a6d8a79-57ab0781/Singularity
collection: CNC-UMCG/cnc_mriqc
---

# CNC-UMCG/cnc_mriqc:txt

```bash
$ singularity pull shub://CNC-UMCG/cnc_mriqc:txt
```

## Singularity Recipe

```singularity
Bootstrap: docker

FROM: poldracklab/mriqc:0.14.2

%post
        apt-get update && apt-get -y purge libgsl2 && apt-get -y install libgsl2
```

## Collection

 - Name: [CNC-UMCG/cnc_mriqc](https://github.com/CNC-UMCG/cnc_mriqc)
 - License: None

