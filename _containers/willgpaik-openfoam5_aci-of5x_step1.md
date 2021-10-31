---
id: 9963
name: "willgpaik/openfoam5_aci"
branch: "master"
tag: "of5x_step1"
commit: "0ba9927b315e17a2efd76393702dbb80b398be4f"
version: "74539208fd822be756e81bd65c085dea34eb58481a6c46040d831e3b320d31c2"
build_date: "2019-10-02T20:55:56.955Z"
size_mb: 718.94140625
size: 753864704
sif: "https://datasets.datalad.org/shub/willgpaik/openfoam5_aci/of5x_step1/2019-10-02-0ba9927b-74539208/74539208fd822be756e81bd65c085dea34eb58481a6c46040d831e3b320d31c2.sif"
url: https://datasets.datalad.org/shub/willgpaik/openfoam5_aci/of5x_step1/2019-10-02-0ba9927b-74539208/
recipe: https://datasets.datalad.org/shub/willgpaik/openfoam5_aci/of5x_step1/2019-10-02-0ba9927b-74539208/Singularity
collection: willgpaik/openfoam5_aci
---

# willgpaik/openfoam5_aci:of5x_step1

```bash
$ singularity pull shub://willgpaik/openfoam5_aci:of5x_step1
```

## Singularity Recipe

```singularity
#BootStrap: shub
#From: willgpaik/centos7_aci:latest
BootStrap: docker
From: centos:7

%environment
  bash
  source /opt/sw/OpenFOAM/OpenFOAM-5.x/etc/bashrc WM_LABEL_SIZE=32 WM_MPLIB=OPENMPI FOAMY_HEX_MESH=yes


%post
  # https://openfoamwiki.net/index.php/Installation/Linux/OpenFOAM-5.x/CentOS_SL_RHEL
  yum -y groupinstall 'Development Tools' 
  yum -y install zlib-devel libXext-devel libGLU-devel libXt-devel libXrender-devel libXinerama-devel \
      libpng-devel libXrandr-devel libXi-devel libXft-devel libjpeg-turbo-devel libXcursor-devel \
      readline-devel ncurses-devel python python-devel cmake qt-devel qt-assistant \
      mpfr-devel gmp-devel wget git
      
  #scl enable devtoolset-8 bash
  
  #export PATH="$PATH:/usr/lib64/openmpi/bin/"
  #export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/lib64/openmpi/lib/"
  #export MPI_ROOT=/usr/lib64/openmpi/
  #export BOOST_ROOT=/usr/local/
      
  alias wmRefresh="echo blah"
  set +e
  
  mkdir -p /opt/sw/OpenFOAM
  cd /opt/sw/OpenFOAM
  git clone https://github.com/OpenFOAM/OpenFOAM-5.x.git
  git clone https://github.com/OpenFOAM/ThirdParty-5.x.git
  
  cd ThirdParty-5.x
  mkdir download
  wget -P download  https://www.cmake.org/files/v3.9/cmake-3.9.0.tar.gz
  wget -P download  https://github.com/CGAL/cgal/releases/download/releases%2FCGAL-4.10/CGAL-4.10.tar.xz
  wget -P download https://sourceforge.net/projects/boost/files/boost/1.55.0/boost_1_55_0.tar.bz2
  wget -P download https://www.open-mpi.org/software/ompi/v2.1/downloads/openmpi-2.1.1.tar.bz2
  wget -P download http://www.paraview.org/files/v5.4/ParaView-v5.4.0.tar.gz
  
  tar -xzf download/cmake-3.9.0.tar.gz
  tar -xJf download/CGAL-4.10.tar.xz
  tar -xjf download/boost_1_55_0.tar.bz2
  tar -xjf download/openmpi-2.1.1.tar.bz2
  tar -xzf download/ParaView-v5.4.0.tar.gz --transform='s/ParaView-v5.4.0/ParaView-5.4.0/'
  
  cd ..
  
  sed -i -e 's/\(boost_version=\)boost-system/\1boost_1_55_0/' OpenFOAM-5.x/etc/config.sh/CGAL
  sed -i -e 's/\(cgal_version=\)cgal-system/\1CGAL-4.10/' OpenFOAM-5.x/etc/config.sh/CGAL
    
  #ln -s /usr/lib64/openmpi/mpicc /opt/sw/OpenFOAM/OpenFOAM-5.x/bin/mpicc
  #ln -s /usr/lib64/openmpi/mpirun /opt/sw/OpenFOAM/OpenFOAM-5.x/bin/mpirun
  
  #source /opt/sw/OpenFOAM/OpenFOAM-5.x/etc/bashrc WM_LABEL_SIZE=64 WM_MPLIB=OPENMPI FOAMY_HEX_MESH=yes
  # Install with WM_LABEL_SIZE=32 -> for CFDEM
  source /opt/sw/OpenFOAM/OpenFOAM-5.x/etc/bashrc WM_MPLIB=OPENMPI FOAMY_HEX_MESH=yes
    
  # Don't need to build cmake 3.9 since source container already has cmake 3
  cd $WM_THIRD_PARTY_DIR
  ./makeCmake > log.makeCmake 2>&1
  wmRefresh
  
  cd $WM_THIRD_PARTY_DIR
  ./Allwmake -j 2 > log.make 2>&1
  wmRefresh
  
  cd $WM_THIRD_PARTY_DIR
 
  #this will take a while... somewhere between 30 minutes to 2 hours or more
  ./makeParaView -mpi -python -qmake $(which qmake-qt4) > log.makePV 2>&1
  
  wmRefresh
  
  #cd $WM_PROJECT_DIR
  #./Allwmake -j 2 > log.make 2>&1
  
  #source /opt/sw/OpenFOAM/OpenFOAM-5.x/etc/bashrc WM_MPLIB=OPENMPI FOAMY_HEX_MESH=yes
```

## Collection

 - Name: [willgpaik/openfoam5_aci](https://github.com/willgpaik/openfoam5_aci)
 - License: None

