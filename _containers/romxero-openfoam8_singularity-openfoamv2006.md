---
id: 15843
name: "romxero/openfoam8_singularity"
branch: "main"
tag: "openfoamv2006"
commit: "3c213f8c57755511b8c1c930111fa4b8e532ee19"
version: "cb88492b97ee4c1c83f58a44a702670d40f30aa25e117513792dccb307a74422"
build_date: "2021-04-02T07:17:00.955Z"
size_mb: 1019.79296875
size: 1069330432
sif: "https://datasets.datalad.org/shub/romxero/openfoam8_singularity/openfoamv2006/2021-04-02-3c213f8c-cb88492b/cb88492b97ee4c1c83f58a44a702670d40f30aa25e117513792dccb307a74422.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/openfoam8_singularity/openfoamv2006/2021-04-02-3c213f8c-cb88492b/
recipe: https://datasets.datalad.org/shub/romxero/openfoam8_singularity/openfoamv2006/2021-04-02-3c213f8c-cb88492b/Singularity
collection: romxero/openfoam8_singularity
---

# romxero/openfoam8_singularity:openfoamv2006

```bash
$ singularity pull shub://romxero/openfoam8_singularity:openfoamv2006
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: openfoamplus/of_v2006_centos73
%labels
Author "Randall Cab White - rcwhite@stanford.edu"
#########
#%setup
#########
#Downlaod packages
%post
%environment
export IMAGE_NAME="openfoamV2006"
#export FOAM_INST_DIR=/opt
#export WM_PROJECT_INST_DIR=$FOAM_INST_DIR
export WM_PROJECT_DIR=/opt/OpenFOAM/OpenFOAM-v2006
. /opt/OpenFOAM/setImage_v2006.sh
export PATH=/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/qt-5.9.0/bin:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/ADIOS2-2.4.0/bin:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/ParaView-5.6.3-mpi-py/bin:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/openmpi-1.10.4/bin:/root/OpenFOAM/root-v2006/platforms/linux64GccDPInt32Opt/bin:/opt/OpenFOAM/OpenFOAM-v2006/site/2006/platforms/linux64GccDPInt32Opt/bin:/opt/OpenFOAM/OpenFOAM-v2006/platforms/linux64GccDPInt32Opt/bin:/opt/OpenFOAM/OpenFOAM-v2006/bin:/opt/OpenFOAM/OpenFOAM-v2006/wmake:$PATH
export LD_LIBRARY_PATH=/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64/zlib-1.2.11/lib:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/qt-5.9.0/lib:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/ParaView-5.6.3-mpi-py/lib/paraview-5.6/plugins:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/ParaView-5.6.3-mpi-py/lib/mesa:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/fftw-3.3.7/lib64:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/CGAL-4.12.2/lib64:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/boost_1_66_0/lib64:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/ADIOS2-2.4.0/lib64:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/mesa-17.1.1/lib64:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64/llvm-4.0.0/lib64:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/ParaView-5.6.3-mesa-mpi-py/lib:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/ParaView-5.6.3-mpi-py/lib:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/qt-5.9.0/lib:/opt/OpenFOAM/OpenFOAM-v2006/platforms/linux64GccDPInt32Opt/lib/openmpi-1.10.4:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64GccDPInt32/lib/openmpi-1.10.4:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64Gcc/openmpi-1.10.4/lib64:/root/OpenFOAM/root-v2006/platforms/linux64GccDPInt32Opt/lib:/opt/OpenFOAM/OpenFOAM-v2006/site/2006/platforms/linux64GccDPInt32Opt/lib:/opt/OpenFOAM/OpenFOAM-v2006/platforms/linux64GccDPInt32Opt/lib:/opt/OpenFOAM/ThirdParty-v2006/platforms/linux64GccDPInt32/lib:/opt/OpenFOAM/OpenFOAM-v2006/platforms/linux64GccDPInt32Opt/lib/dummy:$LD_LIBRARY_PATH

%runscript
```

## Collection

 - Name: [romxero/openfoam8_singularity](https://github.com/romxero/openfoam8_singularity)
 - License: None

