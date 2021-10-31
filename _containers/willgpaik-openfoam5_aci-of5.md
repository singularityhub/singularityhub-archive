---
id: 9445
name: "willgpaik/openfoam5_aci"
branch: "master"
tag: "of5"
commit: "c4f9695d2b6eeedcf2815daed0daa528b83972b0"
version: "0e641744fbf0f53514c7f1c27fef3da9"
build_date: "2019-06-21T06:30:07.679Z"
size_mb: 3389
size: 1048961055
sif: "https://datasets.datalad.org/shub/willgpaik/openfoam5_aci/of5/2019-06-21-c4f9695d-0e641744/0e641744fbf0f53514c7f1c27fef3da9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/willgpaik/openfoam5_aci/of5/2019-06-21-c4f9695d-0e641744/
recipe: https://datasets.datalad.org/shub/willgpaik/openfoam5_aci/of5/2019-06-21-c4f9695d-0e641744/Singularity
collection: willgpaik/openfoam5_aci
---

# willgpaik/openfoam5_aci:of5

```bash
$ singularity pull shub://willgpaik/openfoam5_aci:of5
```

## Singularity Recipe

```singularity
BootStrap: docker
From:openfoam/openfoam5-paraview54
    
%labels


%environment
    bash
    export LD_LIBRARY_PATH=/opt/openfoam5/platforms/linux64GccDPInt32Opt/lib:$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH=/lib64:$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH=/lib:$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH=/usr/lib:$LD_LIBRARY_PATH
    export CPATH=/usr/include:$CPATH
    export CPATH=/usr/lib/openmpi/include:$CPATH
    export MPI_ROOT=/usr/lib/openmpi
    export MPI_ARCH_FLAGS="-DMPICH_SKIP_MPICXX"
    export MPI_ARCH_INC="-I$MPI_ARCH_PATH/include"
    export MPI_ARCH_LIBS='-L$(MPI_ARCH_PATH)/lib -lmpich -lmpichcxx -lmpl -lopa -lrt'
    source /opt/openfoam5/etc/bashrc


%post
    apt-get update -y
    apt-get install -y git-core
    apt-get install -y build-essential
    apt-get -y install flex \
          bison \
          cmake \
          zlib1g-dev \
          libboost-system-dev \
          libboost-thread-dev \
          libopenmpi-dev \
          openmpi-bin \
          gnuplot \
          libreadline-dev \
          libncurses-dev \
          libxt-dev \
          libscotch-dev \
          libptscotch-dev \
          libvtk6-dev \
          python-numpy \
          octave \
          eog
      
    #echo ". /opt/openfoam5/etc/bashrc" >> /.singularity.d/env/01-base.sh
      
    # Link directories
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
```

## Collection

 - Name: [willgpaik/openfoam5_aci](https://github.com/willgpaik/openfoam5_aci)
 - License: None

