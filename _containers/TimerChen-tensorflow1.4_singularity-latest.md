---
id: 10780
name: "TimerChen/tensorflow1.4_singularity"
branch: "master"
tag: "latest"
commit: "5200bfc1f28dad74df147a4290a4757a5306456b"
version: "1fc0acce7407349b2d6c2b736bbef98b"
build_date: "2020-05-14T20:58:09.402Z"
size_mb: 3125.0
size: 1581420575
sif: "https://datasets.datalad.org/shub/TimerChen/tensorflow1.4_singularity/latest/2020-05-14-5200bfc1-1fc0acce/1fc0acce7407349b2d6c2b736bbef98b.sif"
url: https://datasets.datalad.org/shub/TimerChen/tensorflow1.4_singularity/latest/2020-05-14-5200bfc1-1fc0acce/
recipe: https://datasets.datalad.org/shub/TimerChen/tensorflow1.4_singularity/latest/2020-05-14-5200bfc1-1fc0acce/Singularity
collection: TimerChen/tensorflow1.4_singularity
---

# TimerChen/tensorflow1.4_singularity:latest

```bash
$ singularity pull shub://TimerChen/tensorflow1.4_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.4.1-gpu-py3

%post
    apt-get update && apt-get -y install locales
    locale-gen en_US.UTF-8
    apt-get install -y git wget python3-dev python3-pip python3-tk
    apt-get clean

    apt-get install -y libcupti-dev
```

## Collection

 - Name: [TimerChen/tensorflow1.4_singularity](https://github.com/TimerChen/tensorflow1.4_singularity)
 - License: None

