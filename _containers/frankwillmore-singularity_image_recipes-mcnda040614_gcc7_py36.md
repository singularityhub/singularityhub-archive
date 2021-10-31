---
id: 9631
name: "frankwillmore/singularity_image_recipes"
branch: "master"
tag: "mcnda040614_gcc7_py36"
commit: "70ea30c542669408bc9b14f0bb89f5d60aced2cf"
version: "f603efaae005a4bcf4f2fac2e64d66a6"
build_date: "2019-06-07T11:19:42.524Z"
size_mb: 7776
size: 3368747039
sif: "https://datasets.datalad.org/shub/frankwillmore/singularity_image_recipes/mcnda040614_gcc7_py36/2019-06-07-70ea30c5-f603efaa/f603efaae005a4bcf4f2fac2e64d66a6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/frankwillmore/singularity_image_recipes/mcnda040614_gcc7_py36/2019-06-07-70ea30c5-f603efaa/
recipe: https://datasets.datalad.org/shub/frankwillmore/singularity_image_recipes/mcnda040614_gcc7_py36/2019-06-07-70ea30c5-f603efaa/Singularity
collection: frankwillmore/singularity_image_recipes
---

# frankwillmore/singularity_image_recipes:mcnda040614_gcc7_py36

```bash
$ singularity pull shub://frankwillmore/singularity_image_recipes:mcnda040614_gcc7_py36
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos


%post
   # install development tools
   yum update -y
   yum install -y wget bzip2 which make libfabric

   #####
   #  miniconda install
   ############
   
   # change this if you want different versions
   CONDAVER=3
   VERSION=4.6.14
   BASE_DIR=/miniconda$CONDAVER
   PREFIX_PATH=$BASE_DIR/$VERSION
   DOWNLOAD_PATH=$BASE_DIR/DOWNLOADS

   # make install area
   mkdir -p $PREFIX_PATH
   mkdir -p $DOWNLOAD_PATH

   MINICONDA_INSTALL_FILE=Miniconda$CONDAVER-$VERSION-Linux-x86_64.sh

   echo Downloading miniconda installer
   wget https://repo.continuum.io/miniconda/$MINICONDA_INSTALL_FILE -P $DOWNLOAD_PATH
      
   chmod +x $DOWNLOAD_PATH/Miniconda$CONDAVER-$VERSION-Linux-x86_64.sh

   echo Installing Miniconda
   $DOWNLOAD_PATH/Miniconda$CONDAVER-$VERSION-Linux-x86_64.sh -b -p $PREFIX_PATH -u

   # add conda to environment
   export PATH=$PREFIX_PATH/bin:$PATH


   echo moving into $PREFIX_PATH
   cd $PREFIX_PATH

   echo CONDA BINARY: $(which conda)
   echo CONDA VERSION: $(conda --version)
   
   echo Setting intel channel to the primary
   conda config --add channels intel

   echo install tensorflow dependencies and other things
   conda install -y tensorflow -c intel

   echo install keras
   conda install -y keras pandas h5py matplotlib scikit-learn scikit-image
   
   echo install pytorch
   conda install -y pytorch-cpu torchvision-cpu -c pytorch

   echo install gcc
   conda install -y gcc_linux-64 gxx_linux-64
   find $PREFIX_PATH/bin -type f -name "x86_64-conda_cos6-linux-gnu-*" -exec bash -c "python -c \"print('{}'.split('linux-gnu-')[-1])\" | xargs -I file ln -s {} $PREFIX_PATH/bin/file" \;

   echo which gcc: $(/bin/which gcc)
   echo which g++: $(/bin/which g++)
   echo gcc version
   gcc --version

   MPICH_VERSION=3.3
   echo installing mpich $MPICH_VERSION
   mkdir /mpich
   cd /mpich
   wget http://www.mpich.org/static/downloads/$MPICH_VERSION/mpich-$MPICH_VERSION.tar.gz
   tar xf mpich-$MPICH_VERSION.tar.gz --strip-components=1
   ./configure --prefix=/mpich/install --disable-wrapper-rpath --disable-fortran
   make -j 4 install
   
   # setup MPICH 
   export PATH=$PATH:/mpich/install/bin
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib

   echo install mpi4py
   conda install -y mpi4py

   # install keras and horovod
   echo install horovod
   CC=/mpich/install/bin/mpicc CXX=/mpich/install/bin/mpicxx pip install --no-cache-dir horovod

%environment
   export PATH=/miniconda3/4.5.12/bin:$PATH

%runscript
   python /test/keras_mnist.py
```

## Collection

 - Name: [frankwillmore/singularity_image_recipes](https://github.com/frankwillmore/singularity_image_recipes)
 - License: None

