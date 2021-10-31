---
id: 7423
name: "Molmed/summary-report-development"
branch: "master"
tag: "checkqc"
commit: "f7ad01b52d5db0d87e8e3fad811ef92926111d9b"
version: "339dc97e032e199ff39761961097da3e"
build_date: "2019-12-17T13:54:29.516Z"
size_mb: 1137
size: 390021151
sif: "https://datasets.datalad.org/shub/Molmed/summary-report-development/checkqc/2019-12-17-f7ad01b5-339dc97e/339dc97e032e199ff39761961097da3e.simg"
url: https://datasets.datalad.org/shub/Molmed/summary-report-development/checkqc/2019-12-17-f7ad01b5-339dc97e/
recipe: https://datasets.datalad.org/shub/Molmed/summary-report-development/checkqc/2019-12-17-f7ad01b5-339dc97e/Singularity
collection: Molmed/summary-report-development
---

# Molmed/summary-report-development:checkqc

```bash
$ singularity pull shub://Molmed/summary-report-development:checkqc
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.6-stretch

%post
  pip install checkqc==3.3.1
```

## Collection

 - Name: [Molmed/summary-report-development](https://github.com/Molmed/summary-report-development)
 - License: None

