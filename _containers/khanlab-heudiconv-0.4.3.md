---
id: 1433
name: "khanlab/heudiconv"
branch: "master"
tag: "0.4.3"
commit: "a8bffcc96f515c2550e7e439304eccb603860048"
version: "7919132eefbabd572641a616621e8086"
build_date: "2019-08-22T12:47:36.453Z"
size_mb: 2512
size: 803635231
sif: "https://datasets.datalad.org/shub/khanlab/heudiconv/0.4.3/2019-08-22-a8bffcc9-7919132e/7919132eefbabd572641a616621e8086.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/heudiconv/0.4.3/2019-08-22-a8bffcc9-7919132e/
recipe: https://datasets.datalad.org/shub/khanlab/heudiconv/0.4.3/2019-08-22-a8bffcc9-7919132e/Singularity
collection: khanlab/heudiconv
---

# khanlab/heudiconv:0.4.3

```bash
$ singularity pull shub://khanlab/heudiconv:0.4.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:xenial

#########
%setup
#########
mkdir -p $SINGULARITY_ROOTFS/opt/heudiconv
cp -Rv . $SINGULARITY_ROOTFS/opt/heudiconv


#########
%post
#########


# basics:
export DEBIAN_FRONTEND=noninteractive
export DEST=/opt

apt-get update
apt-get install -y --no-install-recommends apt-utils
apt-get install -y sudo wget curl git dos2unix tree zip unzip
#avoid interactive configureing tdata when installing afni when running 10.install_afni_fsl_sudo.sh
apt-get install -y tzdata
echo "America/New_York" | sudo tee /etc/timezone && sudo dpkg-reconfigure --frontend noninteractive tzdata
#needed when install Anaconda2
apt-get install -y bzip2
#needed when install nipype
apt-get install -y build-essential libtool autotools-dev automake autoconf


# anaconda:
ANACONDA2_DIR=$DEST/anaconda2
INST_FILE=Anaconda2-4.2.0-Linux-x86_64.sh
#-P: prefix, where there file will be save to
wget -P $ANACONDA2_DIR --tries=10 https://repo.continuum.io/archive/$INST_FILE 
#-b:bacth mode, -f: no error if install prefix already exists
PATH=$ANACONDA2_DIR/bin:$PATH
bash $ANACONDA2_DIR/$INST_FILE -b -f -p $ANACONDA2_DIR
rm $ANACONDA2_DIR/$INST_FILE



# heudiconv depends
conda install -y -c conda-forge nipype 
pip install --upgrade pip
pip install https://github.com/moloney/dcmstack/archive/c12d27d2c802d75a33ad70110124500a83e851ee.zip

#dcm2niix
RANDOM_TEMP=${RANDOM}
wget https://www.dropbox.com/s/elg1t4fm3zp4qxg/mricrogl_linux.zip?dl=0 -O ${RANDOM_TEMP}.zip;unzip -o ${RANDOM_TEMP}.zip -d ${DEST}; rm ${RANDOM_TEMP}.zip




# heudiconv
cd /opt/heudiconv
python setup.py install
cd


#########
%environment

#anaconda2
export PATH=/opt/anaconda2/bin/:$PATH
#heudiconv
export PYTHONPATH=/opt/heudiconv:$PYTHONPATH
#dcm2niix
export PATH=/opt/mricrogl_lx:$PATH

%runscript
exec heudiconv $@
```

## Collection

 - Name: [khanlab/heudiconv](https://github.com/khanlab/heudiconv)
 - License: None

