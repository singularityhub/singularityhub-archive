---
id: 6736
name: "GregoryAshton/containers"
branch: "master"
tag: "bilby0.3.5"
commit: "1ef300092417868bb9f077723a63bc2008e4caa9"
version: "93da2a3621dc8808deece9539ff89d33"
build_date: "2019-01-31T07:08:05.105Z"
size_mb: 4088
size: 1844600863
sif: "https://datasets.datalad.org/shub/GregoryAshton/containers/bilby0.3.5/2019-01-31-1ef30009-93da2a36/93da2a3621dc8808deece9539ff89d33.simg"
url: https://datasets.datalad.org/shub/GregoryAshton/containers/bilby0.3.5/2019-01-31-1ef30009-93da2a36/
recipe: https://datasets.datalad.org/shub/GregoryAshton/containers/bilby0.3.5/2019-01-31-1ef30009-93da2a36/Singularity
collection: GregoryAshton/TestBilbySingularity
---

# GregoryAshton/containers:bilby0.3.5

```bash
$ singularity pull shub://GregoryAshton/containers:bilby0.3.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bilbydev/bilby-test-suite-python37

%help
A singularity container for running bilby scripts. To use, simply execute the
container, providing the bilby_script and any additional arguments. E.g.,

./name_of_this_container.simg run_script.py

%post
export PATH="/opt/conda/bin:$PATH"
pip install bilby==0.3.5

%runscript
exec /opt/conda/bin/python "$@"
```

## Collection

 - Name: [GregoryAshton/containers](https://github.com/GregoryAshton/containers)
 - License: None

