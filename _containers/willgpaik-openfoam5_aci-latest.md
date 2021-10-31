---
id: 7734
name: "willgpaik/openfoam5_aci"
branch: "master"
tag: "latest"
commit: "8966d9d5d87fe6cd24921de1562fc2e68b4bf826"
version: "73141a429a5b6c88629fc8c0b0a26815"
build_date: "2020-05-18T19:08:14.981Z"
size_mb: 3389
size: 1048838175
sif: "https://datasets.datalad.org/shub/willgpaik/openfoam5_aci/latest/2020-05-18-8966d9d5-73141a42/73141a429a5b6c88629fc8c0b0a26815.simg"
url: https://datasets.datalad.org/shub/willgpaik/openfoam5_aci/latest/2020-05-18-8966d9d5-73141a42/
recipe: https://datasets.datalad.org/shub/willgpaik/openfoam5_aci/latest/2020-05-18-8966d9d5-73141a42/Singularity
collection: willgpaik/openfoam5_aci
---

# willgpaik/openfoam5_aci:latest

```bash
$ singularity pull shub://willgpaik/openfoam5_aci:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From:openfoam/openfoam5-paraview54

%environment
    export HOME=/storage/work/cxl1166/sw
    export PATH=/storage/work/cxl1166/sw/LIGGGHTS/LIGGGHTS-PUBLIC/src:$PATH
    export PATH=/storage/work/cxl1166/sw/LIGGGHTS/mylpp/src:$PATH
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
    
    /opt/openfoam5/etc/bashrc

%labels
Author jpj5196
Modified by Will

%post
    apt-get update -y
    apt-get install -y git-core
    apt-get install -y build-essential flex bison cmake zlib1g-dev libboost-system-dev libboost-thread-dev libopenmpi-dev openmpi-bin gnuplot libreadline-dev libncurses-dev libxt-dev libscotch-dev libptscotch-dev
    apt-get install -y libvtk6-dev
    apt-get install -y python-numpy
    apt-get install -y octave eog
   
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/comm.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pcomm.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/datatype_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pdatatype_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/file.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pfile.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/group.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pgroup.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/intercomm.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pintercomm.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/mpicxx.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pmpicxx.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/request_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/prequest_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/topology_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/ptopology_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/comm_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pcomm_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/errhandler.h /usr/lib/openmpi/include/openmpi/ompi/mpi/perrhandler.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/file_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pfile_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/group_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pgroup_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/intercomm_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pintercomm_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/op.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pop.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/status.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pstatus.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/win.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pwin.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/constants.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pconstants.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/errhandler_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/perrhandler_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/functions.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pfunctions.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/info.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pinfo.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/intracomm.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pintracomm.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/op_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pop_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/status_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pstatus_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/win_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pwin_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/datatype.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pdatatype.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/exception.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pexception.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/functions_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pfunctions_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/info_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pinfo_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/intracomm_inln.h /usr/lib/openmpi/include/openmpi/ompi/mpi/pintracomm_inln.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/request.h /usr/lib/openmpi/include/openmpi/ompi/mpi/prequest.h
    ln -s /usr/lib/openmpi/include/openmpi/ompi/mpi/topology.h /usr/lib/openmpi/include/openmpi/ompi/mpi/ptopology.h

    #------------------------------------------------------------------------------
    # Create local binding point for our HPC
    #------------------------------------------------------------------------------
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
    
#    cp /opt/openfoam5/etc/bashrc /.singularity.d/env/openfoam.sh
    chmod +x /opt/openfoam5/etc/bashrc
```

## Collection

 - Name: [willgpaik/openfoam5_aci](https://github.com/willgpaik/openfoam5_aci)
 - License: None

