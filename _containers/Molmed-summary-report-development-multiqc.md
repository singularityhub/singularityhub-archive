---
id: 7262
name: "Molmed/summary-report-development"
branch: "master"
tag: "multiqc"
commit: "995199f56c07613286c11e8168d31e6572ec3fd6"
version: "5fce91cd823519ce22bec2b7ef66d9e5"
build_date: "2019-12-17T13:54:55.809Z"
size_mb: 509
size: 185589791
sif: "https://datasets.datalad.org/shub/Molmed/summary-report-development/multiqc/2019-12-17-995199f5-5fce91cd/5fce91cd823519ce22bec2b7ef66d9e5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Molmed/summary-report-development/multiqc/2019-12-17-995199f5-5fce91cd/
recipe: https://datasets.datalad.org/shub/Molmed/summary-report-development/multiqc/2019-12-17-995199f5-5fce91cd/Singularity
collection: Molmed/summary-report-development
---

# Molmed/summary-report-development:multiqc

```bash
$ singularity pull shub://Molmed/summary-report-development:multiqc
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ewels/multiqc:v1.7

%post
  pip install --upgrade --force-reinstall git+https://github.com/MultiQC/MultiQC_Clarity.git
```

## Collection

 - Name: [Molmed/summary-report-development](https://github.com/Molmed/summary-report-development)
 - License: None

