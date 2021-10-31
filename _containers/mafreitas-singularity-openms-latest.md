---
id: 1756
name: "mafreitas/singularity-openms"
branch: "master"
tag: "latest"
commit: "0b7a38d1ade9d7df20170778987f9f75ed21764c"
version: "82a5fb1630e2bc3e0d22b294c0ba9ecb"
build_date: "2020-07-11T09:15:36.194Z"
size_mb: 2049
size: 862617631
sif: "https://datasets.datalad.org/shub/mafreitas/singularity-openms/latest/2020-07-11-0b7a38d1-82a5fb16/82a5fb1630e2bc3e0d22b294c0ba9ecb.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mafreitas/singularity-openms/latest/2020-07-11-0b7a38d1-82a5fb16/
recipe: https://datasets.datalad.org/shub/mafreitas/singularity-openms/latest/2020-07-11-0b7a38d1-82a5fb16/Singularity
collection: mafreitas/singularity-openms
---

# mafreitas/singularity-openms:latest

```bash
$ singularity pull shub://mafreitas/singularity-openms:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: mafreitas/singularity-openms:contrib

%environment
export PATH=/usr/local/openms_thirdparty/All/:$PATH
export PATH=/usr/local/openms_thirdparty/All/LuciPHOr2:$PATH
export PATH=/usr/local/openms_thirdparty/All/MSGFPlus:$PATH
export PATH=/usr/local/openms_thirdparty/All/Sirius:$PATH
export PATH=/usr/local/openms_thirdparty/Linux/64bit/:$PATH
export PATH=/usr/local/openms_thirdparty/Linux/64bit/Comet:$PATH
export PATH=/usr/local/openms_thirdparty/Linux/64bit/Fido:$PATH
export PATH=/usr/local/openms_thirdparty/Linux/64bit/MyriMatch:$PATH
export PATH=/usr/local/openms_thirdparty/Linux/64bit/OMSSA:$PATH
export PATH=/usr/local/openms_thirdparty/Linux/64bit/Percolator:$PATH
export PATH=/usr/local/openms_thirdparty/Linux/64bit/Sirius:$PATH
export PATH=/usr/local/openms_thirdparty/Linux/64bit/SpectraST:$PATH
export PATH=/usr/local/openms_thirdparty/Linux/64bit/XTandem:$PATH
export PATH=/usr/local/bin/:$PATH
export OPENMS_DATA_PATH=/usr/local/share/OpenMS
export JAVA_HOME=/usr/lib/jvm/java-8-oracle

%post
cd $HOME
git clone https://github.com/OpenMS/OpenMS.git
cd OpenMS
git checkout tags/Release2.3.0
hash=`git log | head -n 1 | cut -f 2 -d ' '`
sed -i "s/OPENMS_GIT_SHA1/\"$hash\"/" src/openms/source/CONCEPT/VersionInfo.cpp
rm -rf .git/ share/OpenMS/examples/

cd /usr/local/

git clone https://github.com/OpenMS/THIRDPARTY.git openms_thirdparty
cd openms_thirdparty
rm -rf .git Windows MacOS Linux/32bit

cd $HOME
mkdir openms-build
cd openms-build

cmake -DCMAKE_PREFIX_PATH="$HOME/contrib-build/;/usr/;/usr/local" \
        -DCMAKE_INSTALL_PREFIX=/usr/local/ \
        -DBOOST_USE_STATIC=OFF \
        -DHAS_XSERVER=Off ../OpenMS
make TOPP -j6
make UTILS -j6
make install -j6
rm -rf src doc CMakeFiles

cd $HOME
rm -rf contrib contrib-build openms-build
```

## Collection

 - Name: [mafreitas/singularity-openms](https://github.com/mafreitas/singularity-openms)
 - License: None

