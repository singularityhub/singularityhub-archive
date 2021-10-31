---
id: 1655
name: "keceli/mopac_container"
branch: "master"
tag: "old"
commit: "ba7c80aa057ad046e5a3ebda561e4963e9040ed6"
version: "6f0025fe3c13fadb48b48020f893047b"
build_date: "2018-02-07T19:54:06.587Z"
size_mb: 151
size: 57491487
sif: "https://datasets.datalad.org/shub/keceli/mopac_container/old/2018-02-07-ba7c80aa-6f0025fe/6f0025fe3c13fadb48b48020f893047b.simg"
url: https://datasets.datalad.org/shub/keceli/mopac_container/old/2018-02-07-ba7c80aa-6f0025fe/
recipe: https://datasets.datalad.org/shub/keceli/mopac_container/old/2018-02-07-ba7c80aa-6f0025fe/Singularity
collection: keceli/mopac_container
---

# keceli/mopac_container:old

```bash
$ singularity pull shub://keceli/mopac_container:old
```

## Singularity Recipe

```singularity
From: ubuntu:latest
Bootstrap: docker
%help
A container for MOPAC quantum chemistry package.
More info on MOPAC: http://openmopac.net/
You need a license to run MOPAC. See http://openmopac.net/download-c.html (Free for academic)
For this recipe you need to have a mopac_license.txt file, which only contains
the license key string that you have.
This file should be in your home directory or in the directory, where you build the image from recipe.
Licensing does not work for the images build on singularity hub. You need an overlay where you add your license
through the shell. See latest recipe help.
%labels
AUTHOR Murat Keceli
REPO https://github.com/keceli/mopac_container
%setup
echo "Home directory during setup" $HOME
echo "Creating directory:"  ${SINGULARITY_ROOTFS}/opt/mopac
mkdir -p ${SINGULARITY_ROOTFS}/opt/mopac
if [ -f  $HOME/mopac_license.txt ] ; then
  echo "Copying license file at" $HOME
  cp -p $HOME/mopac_license.txt ${SINGULARITY_ROOTFS}/opt/mopac
fi
if [ -f  mopac_license.txt ] ; then
  echo "Copying license file at" $PWD "to" ${SINGULARITY_ROOTFS}/opt/mopac
  cp -p $HOME/mopac_license.txt ${SINGULARITY_ROOTFS}/opt/mopac
fi
%post
echo "************************************************************"
echo "Installling required components"
echo "************************************************************" 
  apt-get -y install wget unzip
echo "************************************************************"
echo "Installling MOPAC"
echo "************************************************************"    
  echo "Home directory during post" $HOME
  mkdir -p /opt/mopac
  chmod 777 /opt/mopac
  cd /opt/mopac
  wget http://openmopac.net/MOPAC2016_for_Linux_64_bit.zip
  unzip MOPAC2016_for_Linux_64_bit.zip
  export LD_LIBRARY_PATH=/opt/mopac
  chmod +x /opt/mopac/MOPAC2016.exe
  # Type your MOPAC license key, and uncomment the following line
  #./MOPAC2016.exe $MOPAC_LICENSE_KEY
  if [ -f  ./mopac_license.txt ] ; then
    echo -ne '\n' "Yes"  | ./MOPAC2016.exe $(cat mopac_license.txt)
  fi
%environment
  LD_LIBRARY_PATH=/opt/mopac
  export LD_LIBRARY_PATH
%runscript
  echo "Running mopac with input file $1"
  exec /opt/mopac/MOPAC2016.exe "$1"
```

## Collection

 - Name: [keceli/mopac_container](https://github.com/keceli/mopac_container)
 - License: None

