---
id: 2786
name: "khanlab/heudiconv"
branch: "master"
tag: "0.4.3a"
commit: "6c6c9490bf16fddcb95b2f35dbe11e9de085926f"
version: "7268a215848d5532cea8b3d083cc1f67"
build_date: "2019-08-22T12:52:36.115Z"
size_mb: 2566
size: 833093663
sif: "https://datasets.datalad.org/shub/khanlab/heudiconv/0.4.3a/2019-08-22-6c6c9490-7268a215/7268a215848d5532cea8b3d083cc1f67.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khanlab/heudiconv/0.4.3a/2019-08-22-6c6c9490-7268a215/
recipe: https://datasets.datalad.org/shub/khanlab/heudiconv/0.4.3a/2019-08-22-6c6c9490-7268a215/Singularity
collection: khanlab/heudiconv
---

# khanlab/heudiconv:0.4.3a

```bash
$ singularity pull shub://khanlab/heudiconv:0.4.3a
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
#updated dropbox link to 2017_07_14 MRIcroGL version (broken link before)
wget https://www.dropbox.com/s/7fcmhwf9p87sn29/mricrogl_linux.zip?dl=0  -O ${RANDOM_TEMP}.zip;unzip -o ${RANDOM_TEMP}.zip -d ${DEST}; rm ${RANDOM_TEMP}.zip
#added below since seeing errors ..
pip install dicom



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

