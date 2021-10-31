---
id: 6692
name: "jtchilders/singularity_mpi_test_recipe"
branch: "master"
tag: "miniconda040512"
commit: "7b889f95bac5191123dc7b8f248818aa32077731"
version: "9f93a347f835bb0ab1f8e33370633c93"
build_date: "2019-01-30T00:38:09.074Z"
size_mb: 4231
size: 2202468383
sif: "https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/miniconda040512/2019-01-30-7b889f95-9f93a347/9f93a347f835bb0ab1f8e33370633c93.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jtchilders/singularity_mpi_test_recipe/miniconda040512/2019-01-30-7b889f95-9f93a347/
recipe: https://datasets.datalad.org/shub/jtchilders/singularity_mpi_test_recipe/miniconda040512/2019-01-30-7b889f95-9f93a347/Singularity
collection: jtchilders/singularity_mpi_test_recipe
---

# jtchilders/singularity_mpi_test_recipe:miniconda040512

```bash
$ singularity pull shub://jtchilders/singularity_mpi_test_recipe:miniconda040512
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: jtchilders/singularity_mpi_test_recipe:mpich

%setup
   mkdir ${SINGULARITY_ROOTFS}/test
   cp keras_mnist.py ${SINGULARITY_ROOTFS}/test
   cp download_mnist.sh ${SINGULARITY_ROOTFS}/test

%post
   # install development tools
   yum update -y
   yum groupinstall -y "Development Tools"
   yum install -y gcc
   yum install -y gcc-c++
   yum install -y wget

   # setup MPICH 
   export PATH=$PATH:/mpich/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib

   #####
   #  miniconda install
   ############

   
   
   # change this if you want different versions
   CONDAVER=3
   VERSION=4.5.12
   BASE_DIR=/miniconda$CONDAVER
   PREFIX_PATH=$BASE_DIR/$VERSION
   DOWNLOAD_PATH=$BASE_DIR/DOWNLOADS

   # make install area
   mkdir -p $PREFIX_PATH
   mkdir -p $DOWNLOAD_PATH

   MINICONDA_INSTALL_FILE=Miniconda$CONDAVER-$VERSION-Linux-x86_64.sh

   if [ ! -f $DOWNLOAD_PATH/$MINICONDA_INSTALL_FILE ]; then
      echo Downloading miniconda installer
      wget https://repo.continuum.io/miniconda/$MINICONDA_INSTALL_FILE -P $DOWNLOAD_PATH
      
      chmod +x $DOWNLOAD_PATH/Miniconda$CONDAVER-$VERSION-Linux-x86_64.sh
   fi

   echo Installing Miniconda
   $DOWNLOAD_PATH/Miniconda$CONDAVER-$VERSION-Linux-x86_64.sh -b -p $PREFIX_PATH -u

   # add conda to environment
   export PATH=$PATH:$PREFIX_PATH/bin


   echo moving into $PREFIX_PATH
   cd $PREFIX_PATH

   echo CONDA BINARY: $(which conda)
   echo CONDA VERSION: $(conda --version)

   echo install tensorflow dependencies and other things
   conda install -y tensorflow -c intel

   echo install keras
   conda install -y keras
   
   echo install pytorch
   conda install -y pytorch-cpu torchvision-cpu -c pytorch

   echo install mpi4py
   conda install -y mpi4py

   # install keras and horovod
   echo install horovod
   pip install horovod

%environment
   export PATH=/miniconda3/4.5.12/bin:$PATH

%runscript
   python /test/keras_mnist.py
```

## Collection

 - Name: [jtchilders/singularity_mpi_test_recipe](https://github.com/jtchilders/singularity_mpi_test_recipe)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

