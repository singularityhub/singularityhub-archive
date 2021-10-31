---
id: 3777
name: "outbackCrustacian/python_singularity_recipes"
branch: "master"
tag: "massfile"
commit: "da5d1bc6469c13615eb0319f9dec289a62315c7b"
version: "36080d6d1d8a8a8336f69e26f0cf7c8d"
build_date: "2018-08-02T20:49:37.968Z"
size_mb: 1286
size: 347824159
sif: "https://datasets.datalad.org/shub/outbackCrustacian/python_singularity_recipes/massfile/2018-08-02-da5d1bc6-36080d6d/36080d6d1d8a8a8336f69e26f0cf7c8d.simg"
url: https://datasets.datalad.org/shub/outbackCrustacian/python_singularity_recipes/massfile/2018-08-02-da5d1bc6-36080d6d/
recipe: https://datasets.datalad.org/shub/outbackCrustacian/python_singularity_recipes/massfile/2018-08-02-da5d1bc6-36080d6d/Singularity
collection: outbackCrustacian/python_singularity_recipes
---

# outbackCrustacian/python_singularity_recipes:massfile

```bash
$ singularity pull shub://outbackCrustacian/python_singularity_recipes:massfile
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: outbackCrustacian/python_singularity_recipes:python

%setup
   #make directory for files to be created to
   mkdir ${SINGULARITY_ROOTFS}/files
   cp create_files.py ${SINGULARITY_ROOTFS}/
   #coppy time test into the root directory for use
   #to run do aprun -n 1 -N 1 singularity run python3 /time_test.py
   cp time_test.py ${SINGULARITY_ROOTFS}/
   chmod +x time_test.py

%post
   yes | yum install vim-X11 vim-common vim-enhanced vim-minimal
   #Set correct path for mpich
   export PATH=$PATH:/mpich/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib
   env | sort

   find / -name libmpi.so.12
   python3 hello.py


   #install pip
   curl https://bootstrap.pypa.io/get-pip.py | python

   ls
   cd usr/bin/
   echo SWITCHING NOW
   ls

   #pip3 install mpi4py
   env MPICC=/mpich/install/bin/mpicc pip3 install mpi4py
   cd /

   #create 1k 1kb files
   ulimit -n 2048
   cd /files/
   ulimit -n 2048
   /mpich/install/bin/mpiexec -np 99 python3 /create_files.py
   ls
   cd ..

%runscript
   /time_test.py
```

## Collection

 - Name: [outbackCrustacian/python_singularity_recipes](https://github.com/outbackCrustacian/python_singularity_recipes)
 - License: None

