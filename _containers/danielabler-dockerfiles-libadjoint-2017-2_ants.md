---
id: 9048
name: "danielabler/dockerfiles"
branch: "master"
tag: "libadjoint-2017-2_ants"
commit: "114fe822392eb582d05403049e97f6ad2b8a8d5b"
version: "691b1c726b8ae41aa551980e6b6d8a8b"
build_date: "2021-03-02T14:21:36.610Z"
size_mb: 7857
size: 2193772575
sif: "https://datasets.datalad.org/shub/danielabler/dockerfiles/libadjoint-2017-2_ants/2021-03-02-114fe822-691b1c72/691b1c726b8ae41aa551980e6b6d8a8b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/danielabler/dockerfiles/libadjoint-2017-2_ants/2021-03-02-114fe822-691b1c72/
recipe: https://datasets.datalad.org/shub/danielabler/dockerfiles/libadjoint-2017-2_ants/2021-03-02-114fe822-691b1c72/Singularity
collection: danielabler/dockerfiles
---

# danielabler/dockerfiles:libadjoint-2017-2_ants

```bash
$ singularity pull shub://danielabler/dockerfiles:libadjoint-2017-2_ants
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: danabl/glimslib:libadjoint-2017-2_ants

%post
    ldconfig

%files
    WELCOME.Singularity /usr/local/share/WELCOME

%runscript
    cat /usr/local/share/WELCOME
    exec /bin/bash -i
```

## Collection

 - Name: [danielabler/dockerfiles](https://github.com/danielabler/dockerfiles)
 - License: None

