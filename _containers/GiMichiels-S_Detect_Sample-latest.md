---
id: 2611
name: "GiMichiels/S_Detect_Sample"
branch: "master"
tag: "latest"
commit: "3d9ad81f1ad703b4f9b3a0f9ddaebb3fbb0afd69"
version: "28cabb747a2edfa7feabd466624944e7"
build_date: "2018-04-21T17:37:03.797Z"
size_mb: 2495
size: 1197027359
sif: "https://datasets.datalad.org/shub/GiMichiels/S_Detect_Sample/latest/2018-04-21-3d9ad81f-28cabb74/28cabb747a2edfa7feabd466624944e7.simg"
url: https://datasets.datalad.org/shub/GiMichiels/S_Detect_Sample/latest/2018-04-21-3d9ad81f-28cabb74/
recipe: https://datasets.datalad.org/shub/GiMichiels/S_Detect_Sample/latest/2018-04-21-3d9ad81f-28cabb74/Singularity
collection: GiMichiels/S_Detect_Sample
---

# GiMichiels/S_Detect_Sample:latest

```bash
$ singularity pull shub://GiMichiels/S_Detect_Sample:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: gmichiels/python-client-base:latest

%files
    detect_sample.py /

%runscript
    python /detect_sample.py
```

## Collection

 - Name: [GiMichiels/S_Detect_Sample](https://github.com/GiMichiels/S_Detect_Sample)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

