---
id: 15669
name: "Larssvaenjensen/qtlua_qttorch_singularity"
branch: "main"
tag: "latest"
commit: "fb5ddcb680d89d392507e1c10463d88c7aa2b079"
version: "1267a7f9f1948b2de1ab7c5f241c9e07"
build_date: "2021-03-18T12:07:18.581Z"
size_mb: 3291.0
size: 1411362847
sif: "https://datasets.datalad.org/shub/Larssvaenjensen/qtlua_qttorch_singularity/latest/2021-03-18-fb5ddcb6-1267a7f9/1267a7f9f1948b2de1ab7c5f241c9e07.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Larssvaenjensen/qtlua_qttorch_singularity/latest/2021-03-18-fb5ddcb6-1267a7f9/
recipe: https://datasets.datalad.org/shub/Larssvaenjensen/qtlua_qttorch_singularity/latest/2021-03-18-fb5ddcb6-1267a7f9/Singularity
collection: Larssvaenjensen/qtlua_qttorch_singularity
---

# Larssvaenjensen/qtlua_qttorch_singularity:latest

```bash
$ singularity pull shub://Larssvaenjensen/qtlua_qttorch_singularity:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
from: nvcr.io/nvidia/torch:18.08-py2

%post
    echo "start" 
    apt-get -y update
    echo "1" 
    git clone https://bitbucket.org/mchldann/aaai2019.git
    cd aaai2019/
    echo "2" 
    apt-get install -y libsdl1.2-dev libsdl-gfx1.2-dev libsdl-image1.2-dev cmake
    mkdir build && cd build
    cmake -DUSE_SDL=ON -DUSE_RLGLUE=OFF -DBUILD_EXAMPLES=ON ..
    make -j 4
    echo "3" 
    cd ..
    pip install .
    echo "4" 
    cd src/agent
    chmod +x run_gpu_pellet
    echo "5" 
    apt install -y qt4-default
    luarocks install qtlua
    luarocks install qttorch
    luarocks install lanes
    echo "slut"
```

## Collection

 - Name: [Larssvaenjensen/qtlua_qttorch_singularity](https://github.com/Larssvaenjensen/qtlua_qttorch_singularity)
 - License: None

