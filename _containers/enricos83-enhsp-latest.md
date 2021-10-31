---
id: 14932
name: "enricos83/enhsp"
branch: "master"
tag: "latest"
commit: "4243ba1888eb91338ec37d5d84186076776e8744"
version: "39c1e42240c8e60984e8097f2e1c1c51"
build_date: "2020-11-22T11:33:03.169Z"
size_mb: 201.0
size: 99455007
sif: "https://datasets.datalad.org/shub/enricos83/enhsp/latest/2020-11-22-4243ba18-39c1e422/39c1e42240c8e60984e8097f2e1c1c51.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/enricos83/enhsp/latest/2020-11-22-4243ba18-39c1e422/
recipe: https://datasets.datalad.org/shub/enricos83/enhsp/latest/2020-11-22-4243ba18-39c1e422/Singularity
collection: enricos83/enhsp
---

# enricos83/enhsp:latest

```bash
$ singularity pull shub://enricos83/enhsp:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%post
apt update
apt install -y wget
wget https://download.java.net/java/GA/jdk14.0.1/664493ef4a6946b186ff29eb326336a2/7/GPL/openjdk-14.0.1_linux-x64_bin.tar.gz
tar -xf openjdk-14.0.1_linux-x64_bin.tar.gz
PATH=$PATH:/jdk-14.0.1/bin
rm openjdk-14.0.1_linux-x64_bin.tar.gz
export PATH
apt install -y git
git clone https://gitlab.com/enricos83/ENHSP-Public.git
cd /ENHSP-Public
git checkout enhsp-20
./compile
mv enhsp-dist ../
cd ..
rm -r ENHSP-Public
jlink --no-header-files --no-man-pages --compress=2 --strip-java-debug-attributes --add-modules jdk.jsobject --output java-runtime
rm -r /jdk-14.0.1
PATH=$PATH:/java-runtime/bin

git clone https://github.com/enricos83/downward.git
cd downward 
git checkout only-grounder
cd ..
cp -r downward/translate .
rm -fr downward
mkdir downward
mv translate downward/
apt install -y python3.8-minimal
ln -s /usr/bin/python3.8 /usr/bin/python3

apt remove -y git
apt remove -y wget
apt autoremove -y --purge
export PATH

%runscript
/java-runtime/bin/java -jar /enhsp-dist/enhsp.jar "$@"

%help
This is ENHSP-20 planner container.

%labels
Author Enrico Scala enricos83@gmail.com
```

## Collection

 - Name: [enricos83/enhsp](https://github.com/enricos83/enhsp)
 - License: None

