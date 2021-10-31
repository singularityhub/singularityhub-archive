---
id: 2722
name: "DoaneAS/CRISPRAnalyzeR"
branch: "master"
tag: "latest"
commit: "b2b2ad4fed1798b7d80790e5142e7c4eaaeb4168"
version: "eb3048e9c271cd0f1fba09622d90d333"
build_date: "2018-05-05T03:56:29.025Z"
size_mb: 5925
size: 2487410719
sif: "https://datasets.datalad.org/shub/DoaneAS/CRISPRAnalyzeR/latest/2018-05-05-b2b2ad4f-eb3048e9/eb3048e9c271cd0f1fba09622d90d333.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DoaneAS/CRISPRAnalyzeR/latest/2018-05-05-b2b2ad4f-eb3048e9/
recipe: https://datasets.datalad.org/shub/DoaneAS/CRISPRAnalyzeR/latest/2018-05-05-b2b2ad4f-eb3048e9/Singularity
collection: DoaneAS/CRISPRAnalyzeR
---

# DoaneAS/CRISPRAnalyzeR:latest

```bash
$ singularity pull shub://DoaneAS/CRISPRAnalyzeR:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: boutroslab/crispranalyzer:latest

%post
    mkdir /athena
    mkdir /scratchLocal
```

## Collection

 - Name: [DoaneAS/CRISPRAnalyzeR](https://github.com/DoaneAS/CRISPRAnalyzeR)
 - License: [GNU General Public License v2.0](https://api.github.com/licenses/gpl-2.0)

