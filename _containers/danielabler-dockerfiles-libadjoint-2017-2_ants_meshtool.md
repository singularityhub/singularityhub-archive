---
id: 9053
name: "danielabler/dockerfiles"
branch: "master"
tag: "libadjoint-2017-2_ants_meshtool"
commit: "ed4fed3da3f6f0558eb30874137962866eb57337"
version: "02c5e33e59ac50c26225cf98308bd792"
build_date: "2020-06-11T13:58:13.844Z"
size_mb: 8467
size: 2321580063
sif: "https://datasets.datalad.org/shub/danielabler/dockerfiles/libadjoint-2017-2_ants_meshtool/2020-06-11-ed4fed3d-02c5e33e/02c5e33e59ac50c26225cf98308bd792.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/danielabler/dockerfiles/libadjoint-2017-2_ants_meshtool/2020-06-11-ed4fed3d-02c5e33e/
recipe: https://datasets.datalad.org/shub/danielabler/dockerfiles/libadjoint-2017-2_ants_meshtool/2020-06-11-ed4fed3d-02c5e33e/Singularity
collection: danielabler/dockerfiles
---

# danielabler/dockerfiles:libadjoint-2017-2_ants_meshtool

```bash
$ singularity pull shub://danielabler/dockerfiles:libadjoint-2017-2_ants_meshtool
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: danabl/glimslib:libadjoint-2017-2_ants_meshtool

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

