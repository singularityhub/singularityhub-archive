---
id: 10605
name: "rkalyanapurdue/geoedf-cont"
branch: "master"
tag: "latest"
commit: "6d135fdf19d5e9be5766edbcdced2e14a081a602"
version: "65a87667c23aedeba1473df5246bbc43"
build_date: "2019-08-20T20:19:37.343Z"
size_mb: 141.0
size: 60264479
sif: "https://datasets.datalad.org/shub/rkalyanapurdue/geoedf-cont/latest/2019-08-20-6d135fdf-65a87667/65a87667c23aedeba1473df5246bbc43.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/rkalyanapurdue/geoedf-cont/latest/2019-08-20-6d135fdf-65a87667/
recipe: https://datasets.datalad.org/shub/rkalyanapurdue/geoedf-cont/latest/2019-08-20-6d135fdf-65a87667/Singularity
collection: rkalyanapurdue/geoedf-cont
---

# rkalyanapurdue/geoedf-cont:latest

```bash
$ singularity pull shub://rkalyanapurdue/geoedf-cont:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

%post
    apt-get update
    apt-get -y install python3 curl wget
    mkdir /app
    mkdir /data
    mv /tmp/*.py /app
    chmod +x /app/*.py

%environment
    export PATH=/app:$PATH

%files
    ./tools/run_connector.py /tmp
    ./tools/run_processor.py /tmp

%runscript
    exec "$@"

%labels
    Author Rajesh Kalyanam
```

## Collection

 - Name: [rkalyanapurdue/geoedf-cont](https://github.com/rkalyanapurdue/geoedf-cont)
 - License: None

