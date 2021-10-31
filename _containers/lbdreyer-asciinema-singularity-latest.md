---
id: 1051
name: "lbdreyer/asciinema-singularity"
branch: "master"
tag: "latest"
commit: "ea887e3f973cd076d89236fce09e2fb24648b2a0"
version: "ca167e42526992bf6dc4c6b88702710f"
build_date: "2017-12-06T16:44:56.152Z"
size_mb: 444
size: 192753695
sif: "https://datasets.datalad.org/shub/lbdreyer/asciinema-singularity/latest/2017-12-06-ea887e3f-ca167e42/ca167e42526992bf6dc4c6b88702710f.simg"
url: https://datasets.datalad.org/shub/lbdreyer/asciinema-singularity/latest/2017-12-06-ea887e3f-ca167e42/
recipe: https://datasets.datalad.org/shub/lbdreyer/asciinema-singularity/latest/2017-12-06-ea887e3f-ca167e42/Singularity
collection: lbdreyer/asciinema-singularity
---

# lbdreyer/asciinema-singularity:latest

```bash
$ singularity pull shub://lbdreyer/asciinema-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:latest

%post
    apt-get update
    apt-get -y install python3-pip locales
    pip3 install asciinema
    locale-gen en_GB.UTF-8


%environment
    LANG=en_GB.UTF-8
    LANGUAGE=en_GB:en
    LC_ALL=en_GB.UTF-8
    export LANG LANGUAGE LC_ALL

%runscript
exec asciinema "$@"
```

## Collection

 - Name: [lbdreyer/asciinema-singularity](https://github.com/lbdreyer/asciinema-singularity)
 - License: None

