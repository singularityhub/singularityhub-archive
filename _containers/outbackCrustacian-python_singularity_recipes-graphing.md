---
id: 3961
name: "outbackCrustacian/python_singularity_recipes"
branch: "master"
tag: "graphing"
commit: "bc5645a2d7d53053d192266666e7101e48b9c00e"
version: "fc3f12be984d1b87ae19bea6828572a2"
build_date: "2018-08-13T19:33:55.556Z"
size_mb: 1396
size: 401960991
sif: "https://datasets.datalad.org/shub/outbackCrustacian/python_singularity_recipes/graphing/2018-08-13-bc5645a2-fc3f12be/fc3f12be984d1b87ae19bea6828572a2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/outbackCrustacian/python_singularity_recipes/graphing/2018-08-13-bc5645a2-fc3f12be/
recipe: https://datasets.datalad.org/shub/outbackCrustacian/python_singularity_recipes/graphing/2018-08-13-bc5645a2-fc3f12be/Singularity
collection: outbackCrustacian/python_singularity_recipes
---

# outbackCrustacian/python_singularity_recipes:graphing

```bash
$ singularity pull shub://outbackCrustacian/python_singularity_recipes:graphing
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: outbackCrustacian/python_singularity_recipes:python

%setup
   cp graphtest.py ${SINGULARITY_ROOTFS}/

%post
   yes | yum install vim-X11 vim-common vim-enhanced vim-minimal
   cd /usr/bin/
   pip3 install matplotlib
   pip3 install numpy
   cd ..
   cd ..
```

## Collection

 - Name: [outbackCrustacian/python_singularity_recipes](https://github.com/outbackCrustacian/python_singularity_recipes)
 - License: None

