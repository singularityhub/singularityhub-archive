---
id: 5002
name: "sujoyp/simulation"
branch: "master"
tag: "latest"
commit: "61d12c1f71af4404db0f15dfb354b2a3d582bb79"
version: "87f42cb7305fb7a8ff41e730d534f02f"
build_date: "2018-09-26T21:16:14.524Z"
size_mb: 8306
size: 3899793439
sif: "https://datasets.datalad.org/shub/sujoyp/simulation/latest/2018-09-26-61d12c1f-87f42cb7/87f42cb7305fb7a8ff41e730d534f02f.simg"
url: https://datasets.datalad.org/shub/sujoyp/simulation/latest/2018-09-26-61d12c1f-87f42cb7/
recipe: https://datasets.datalad.org/shub/sujoyp/simulation/latest/2018-09-26-61d12c1f-87f42cb7/Singularity
collection: sujoyp/simulation
---

# sujoyp/simulation:latest

```bash
$ singularity pull shub://sujoyp/simulation:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: sujoyp/cuda-9.0-base-simu

%post

    # OGRE
    git clone https://github.com/sujoyp/ogre.git
    cd ogre/sinbad-ogre-4c20a40dae61/
    mkdir build
    cd build
    cmake -DFREETYPE_INCLUDE_DIR=/usr/include/freetype2 \
    -DFREETYPE_FT2BUILD_INCLUDE_DIR=/usr/include/freetype2 \
    -DOGRE_CONFIG_THREADS=0 \
    ..
    make -j8
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local/OGRE .
    make install
```

## Collection

 - Name: [sujoyp/simulation](https://github.com/sujoyp/simulation)
 - License: None

