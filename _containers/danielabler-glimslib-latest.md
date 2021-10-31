---
id: 9016
name: "danielabler/glimslib"
branch: "master"
tag: "latest"
commit: "7667df99f882e1303646de30d5a7b70ca203027e"
version: "3d50f5014a91323059f41b9201d92580"
build_date: "2019-05-11T17:20:54.315Z"
size_mb: 7637
size: 2193965087
sif: "https://datasets.datalad.org/shub/danielabler/glimslib/latest/2019-05-11-7667df99-3d50f501/3d50f5014a91323059f41b9201d92580.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/danielabler/glimslib/latest/2019-05-11-7667df99-3d50f501/
recipe: https://datasets.datalad.org/shub/danielabler/glimslib/latest/2019-05-11-7667df99-3d50f501/Singularity
collection: danielabler/glimslib
---

# danielabler/glimslib:latest

```bash
$ singularity pull shub://danielabler/glimslib:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: danabl/glimslib_ants:2018-1

%post
    ldconfig

%files
    WELCOME.Singularity /usr/local/share/WELCOME

%runscript
    cat /usr/local/share/WELCOME
    exec /bin/bash -i
```

## Collection

 - Name: [danielabler/glimslib](https://github.com/danielabler/glimslib)
 - License: [MIT License](https://api.github.com/licenses/mit)

