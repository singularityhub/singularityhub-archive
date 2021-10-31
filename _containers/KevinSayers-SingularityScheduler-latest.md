---
id: 2571
name: "KevinSayers/SingularityScheduler"
branch: "master"
tag: "latest"
commit: "5125f630afc1559cdb5759f711d34fae6b768cc9"
version: "11ffe79f7f2d61513a803b7fa47ba271"
build_date: "2018-04-18T11:46:24.924Z"
size_mb: 698
size: 269279263
sif: "https://datasets.datalad.org/shub/KevinSayers/SingularityScheduler/latest/2018-04-18-5125f630-11ffe79f/11ffe79f7f2d61513a803b7fa47ba271.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/KevinSayers/SingularityScheduler/latest/2018-04-18-5125f630-11ffe79f/
recipe: https://datasets.datalad.org/shub/KevinSayers/SingularityScheduler/latest/2018-04-18-5125f630-11ffe79f/Singularity
collection: KevinSayers/SingularityScheduler
---

# KevinSayers/SingularityScheduler:latest

```bash
$ singularity pull shub://KevinSayers/SingularityScheduler:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
FROM: java

%post
    apt-get update
    cd /usr/local/bin
    curl -s https://get.nextflow.io | bash
    chmod -R 777 /usr/local/bin/nextflow
```

## Collection

 - Name: [KevinSayers/SingularityScheduler](https://github.com/KevinSayers/SingularityScheduler)
 - License: None

