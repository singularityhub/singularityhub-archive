---
id: 3788
name: "outbackCrustacian/python_singularity_recipes"
branch: "master"
tag: "python"
commit: "28d280ab81b3424c160f7288d901b893aab3bf70"
version: "ccc00996e505f2f5f66c8c93cb2b9847"
build_date: "2018-08-10T20:17:51.360Z"
size_mb: 1204
size: 321105951
sif: "https://datasets.datalad.org/shub/outbackCrustacian/python_singularity_recipes/python/2018-08-10-28d280ab-ccc00996/ccc00996e505f2f5f66c8c93cb2b9847.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/outbackCrustacian/python_singularity_recipes/python/2018-08-10-28d280ab-ccc00996/
recipe: https://datasets.datalad.org/shub/outbackCrustacian/python_singularity_recipes/python/2018-08-10-28d280ab-ccc00996/Singularity
collection: outbackCrustacian/python_singularity_recipes
---

# outbackCrustacian/python_singularity_recipes:python

```bash
$ singularity pull shub://outbackCrustacian/python_singularity_recipes:python
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:latest

%setup
   cp hello.py ${SINGULARITY_ROOTFS}/

%post
   yum install -y wget
   yum install -y zlib-devel
   yum install -y libffi-devel
   yum install -y openssl-devel

   #Set correct path for mpich
   #Stop pending
   export PATH=$PATH:/mpich/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib
   env | sort

   wget -q https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
   tar xf Python-3.7.0.tar.xz --strip-components=1

   #install python to the container
   ./configure
   make
   make install

   ls

   python3 hello.py

   #install pip
   curl https://bootstrap.pypa.io/get-pip.py | python
```

## Collection

 - Name: [outbackCrustacian/python_singularity_recipes](https://github.com/outbackCrustacian/python_singularity_recipes)
 - License: None

