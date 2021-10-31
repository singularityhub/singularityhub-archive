---
id: 6152
name: "GregoryAshton/TestBilbySingularity"
branch: "master"
tag: "psrchive"
commit: "cd2c372e9538779ad58aaad9eb89915aa0dfc105"
version: "1917ae0a8f51c3fb6f1bfa4cec52476f"
build_date: "2019-01-08T15:14:13.355Z"
size_mb: 3596
size: 1576149023
sif: "https://datasets.datalad.org/shub/GregoryAshton/TestBilbySingularity/psrchive/2019-01-08-cd2c372e-1917ae0a/1917ae0a8f51c3fb6f1bfa4cec52476f.simg"
url: https://datasets.datalad.org/shub/GregoryAshton/TestBilbySingularity/psrchive/2019-01-08-cd2c372e-1917ae0a/
recipe: https://datasets.datalad.org/shub/GregoryAshton/TestBilbySingularity/psrchive/2019-01-08-cd2c372e-1917ae0a/Singularity
collection: GregoryAshton/TestBilbySingularity
---

# GregoryAshton/TestBilbySingularity:psrchive

```bash
$ singularity pull shub://GregoryAshton/TestBilbySingularity:psrchive
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: mpifrpsr/dspsr

%post
    pip install pandas
    pip install gwpy
    pip install tables
```

## Collection

 - Name: [GregoryAshton/TestBilbySingularity](https://github.com/GregoryAshton/TestBilbySingularity)
 - License: None

