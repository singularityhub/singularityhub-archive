---
id: 7465
name: "ZhifangYe/valhalla"
branch: "rstudio"
tag: "latest"
commit: "a59063b4e1a1c59c0be959d2b01bff95af3df2f6"
version: "978994d3bdc25bd892ef949da6feb884"
build_date: "2021-02-17T03:23:05.540Z"
size_mb: 10256
size: 4151627807
sif: "https://datasets.datalad.org/shub/ZhifangYe/valhalla/latest/2021-02-17-a59063b4-978994d3/978994d3bdc25bd892ef949da6feb884.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ZhifangYe/valhalla/latest/2021-02-17-a59063b4-978994d3/
recipe: https://datasets.datalad.org/shub/ZhifangYe/valhalla/latest/2021-02-17-a59063b4-978994d3/Singularity
collection: ZhifangYe/valhalla
---

# ZhifangYe/valhalla:latest

```bash
$ singularity pull shub://ZhifangYe/valhalla:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: zhifang/rstudio-server-test

%runscript
  exec "$@"

%apprun jupyter-notebook
  exec jupyter-notebook --no-browser "$@"

%apprun jupyter-lab
  exec jupyter-lab --no-browser "$@"

%apprun rstudio
  exec rserver "$@"

%startscript
    # RStudio Server
    rserver &
    # Jupyter Notebook
    exec jupyter-lab --no-browser --port=8386

%environment

    # MISC
    export XDG_RUNTIME_DIR=/tmp
    export QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb
    export PATH=/usr/lib/rstudio-server/bin:${PATH}
```

## Collection

 - Name: [ZhifangYe/valhalla](https://github.com/ZhifangYe/valhalla)
 - License: [MIT License](https://api.github.com/licenses/mit)

