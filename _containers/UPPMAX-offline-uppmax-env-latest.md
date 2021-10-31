---
id: 14618
name: "UPPMAX/offline-uppmax-env"
branch: "master"
tag: "latest"
commit: "392557c169a61cb00e71db11cc09f349d9e2f436"
version: "4a9c12d89e80a14b2c49021e0a200a4a"
build_date: "2020-10-15T10:16:16.439Z"
size_mb: 4964.0
size: 1778905119
sif: "https://datasets.datalad.org/shub/UPPMAX/offline-uppmax-env/latest/2020-10-15-392557c1-4a9c12d8/4a9c12d89e80a14b2c49021e0a200a4a.sif"
url: https://datasets.datalad.org/shub/UPPMAX/offline-uppmax-env/latest/2020-10-15-392557c1-4a9c12d8/
recipe: https://datasets.datalad.org/shub/UPPMAX/offline-uppmax-env/latest/2020-10-15-392557c1-4a9c12d8/Singularity
collection: UPPMAX/offline-uppmax-env
---

# UPPMAX/offline-uppmax-env:latest

```bash
$ singularity pull shub://UPPMAX/offline-uppmax-env:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: uppmax/offline-uppmax-env:latest

%files
    # copy the software package files into the container
    packages/*.package.tar.gz /
    

%post
    cat /etc/bashrc.module_env >> /.singularity.d/env/99-module_env.sh
    for f in *.package.tar.gz; do tar xzvf "$f" || echo "No packages to unpack, continuing." ; rm -f "$f"; done
```

## Collection

 - Name: [UPPMAX/offline-uppmax-env](https://github.com/UPPMAX/offline-uppmax-env)
 - License: None

