---
id: 5349
name: "drskrs/sng-intermediates"
branch: "master"
tag: "centos7"
commit: "bd466cd73596a3ea782ce163790edf1c50a527ef"
version: "e0e2a599a3e8456e5ae7753abbe40019"
build_date: "2018-10-25T18:55:06.202Z"
size_mb: 352
size: 72949791
sif: "https://datasets.datalad.org/shub/drskrs/sng-intermediates/centos7/2018-10-25-bd466cd7-e0e2a599/e0e2a599a3e8456e5ae7753abbe40019.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/drskrs/sng-intermediates/centos7/2018-10-25-bd466cd7-e0e2a599/
recipe: https://datasets.datalad.org/shub/drskrs/sng-intermediates/centos7/2018-10-25-bd466cd7-e0e2a599/Singularity
collection: drskrs/sng-intermediates
---

# drskrs/sng-intermediates:centos7

```bash
$ singularity pull shub://drskrs/sng-intermediates:centos7
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:centos:7

%runscript
    echo "Moin."
```

## Collection

 - Name: [drskrs/sng-intermediates](https://github.com/drskrs/sng-intermediates)
 - License: None

