---
id: 3002
name: "ISU-HPC/jupyter"
branch: "master"
tag: "latest"
commit: "66c46f7ba3bbf6dfc0e9dc241a24a4c96a2c0a0f"
version: "9d9baba9342c37793a4da740680cfe2d"
build_date: "2021-04-16T19:08:59.652Z"
size_mb: 1058
size: 343916575
sif: "https://datasets.datalad.org/shub/ISU-HPC/jupyter/latest/2021-04-16-66c46f7b-9d9baba9/9d9baba9342c37793a4da740680cfe2d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/jupyter/latest/2021-04-16-66c46f7b-9d9baba9/
recipe: https://datasets.datalad.org/shub/ISU-HPC/jupyter/latest/2021-04-16-66c46f7b-9d9baba9/Singularity
collection: ISU-HPC/jupyter
---

# ISU-HPC/jupyter:latest

```bash
$ singularity pull shub://ISU-HPC/jupyter:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
FROM: python:3.6.5

%labels
AUTHOR Yasasvy Nanyam ynanyam@iastate.edu

%post
pip3 install --no-cache-dir jupyterlab
```

## Collection

 - Name: [ISU-HPC/jupyter](https://github.com/ISU-HPC/jupyter)
 - License: None

