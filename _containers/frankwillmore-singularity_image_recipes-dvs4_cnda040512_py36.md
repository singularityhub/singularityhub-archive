---
id: 9635
name: "frankwillmore/singularity_image_recipes"
branch: "master"
tag: "dvs4_cnda040512_py36"
commit: "3140226d48fed38e679fd1d68206e291203dffda"
version: "e9e4fc710c6ae25993c7bf7c99735850"
build_date: "2019-06-07T11:19:42.511Z"
size_mb: 5658
size: 2624716831
sif: "https://datasets.datalad.org/shub/frankwillmore/singularity_image_recipes/dvs4_cnda040512_py36/2019-06-07-3140226d-e9e4fc71/e9e4fc710c6ae25993c7bf7c99735850.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/frankwillmore/singularity_image_recipes/dvs4_cnda040512_py36/2019-06-07-3140226d-e9e4fc71/
recipe: https://datasets.datalad.org/shub/frankwillmore/singularity_image_recipes/dvs4_cnda040512_py36/2019-06-07-3140226d-e9e4fc71/Singularity
collection: frankwillmore/singularity_image_recipes
---

# frankwillmore/singularity_image_recipes:dvs4_cnda040512_py36

```bash
$ singularity pull shub://frankwillmore/singularity_image_recipes:dvs4_cnda040512_py36
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos

%post
   echo install development tools
   yum update -y
   yum install -y centos-release-scl
   yum install -y devtoolset-4 wget bzip2
   yum install -y java-1.8.0-openjdk-devel.x86_64


   echo setting up devtoolset-4
   scl enable devtoolset-4 bash
   echo gcc version
   gcc --version
   
   MPICH_VERSION=3.3
   echo installing mpich $MPICH_VERSION
   mkdir /mpich
   cd /mpich
   wget http://www.mpich.org/static/downloads/$MPICH_VERSION/mpich-$MPICH_VERSION.tar.gz
   tar xf mpich-$MPICH_VERSION.tar.gz --strip-components=1
   ./configure --prefix=/mpich/install --disable-wrapper-rpath
   make -j 4 install
   
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

   echo Downloading miniconda installer
   wget https://repo.continuum.io/miniconda/$MINICONDA_INSTALL_FILE -P $DOWNLOAD_PATH
      
   chmod +x $DOWNLOAD_PATH/Miniconda$CONDAVER-$VERSION-Linux-x86_64.sh

   echo Installing Miniconda
   $DOWNLOAD_PATH/Miniconda$CONDAVER-$VERSION-Linux-x86_64.sh -b -p $PREFIX_PATH -u

   # add conda to environment
   export PATH=$PATH:$PREFIX_PATH/bin

   echo moving into $PREFIX_PATH
   cd $PREFIX_PATH

   conda  config --add channels intel

   echo CONDA BINARY: $(which conda)
   echo CONDA VERSION: $(conda --version)
   
   echo install tensorflow dependencies and other things
   conda install -y tensorflow -c intel

   echo install keras
   conda install -y keras
   
   echo install pytorch
   conda install -y pytorch-cpu torchvision-cpu -c pytorch

   echo install other data science modules
   conda install -y pandas matplotlib scikit-learn scikit-image h5py

   echo install horovod
   pip install horovod

%environment
   export PATH=/miniconda3/4.5.12/bin:$PATH
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/mpich/install/lib
```

## Collection

 - Name: [frankwillmore/singularity_image_recipes](https://github.com/frankwillmore/singularity_image_recipes)
 - License: None

