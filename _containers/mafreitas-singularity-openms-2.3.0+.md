---
id: 1761
name: "mafreitas/singularity-openms"
branch: "master"
tag: "2.3.0+"
commit: "3f9b31f078f9763105ec959922999232e030546c"
version: "4485cae803abf8ab214d618d7cc93427"
build_date: "2018-02-19T23:49:16.059Z"
size_mb: 2049
size: 862617631
sif: "https://datasets.datalad.org/shub/mafreitas/singularity-openms/2.3.0+/2018-02-19-3f9b31f0-4485cae8/4485cae803abf8ab214d618d7cc93427.simg"
url: https://datasets.datalad.org/shub/mafreitas/singularity-openms/2.3.0+/2018-02-19-3f9b31f0-4485cae8/
recipe: https://datasets.datalad.org/shub/mafreitas/singularity-openms/2.3.0+/2018-02-19-3f9b31f0-4485cae8/Singularity
collection: mafreitas/singularity-openms
---

# mafreitas/singularity-openms:2.3.0+

```bash
$ singularity pull shub://mafreitas/singularity-openms:2.3.0+
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

