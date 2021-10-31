---
id: 14918
name: "afonsoguerra/SnpEffWrapper"
branch: "master"
tag: "latest"
commit: "ca963d6d971b898d884634e531360e23295aced3"
version: "d1dd8a6fe47194a7e8629374974eba2b829e1c965b1c7df2b422a6b09287d46e"
build_date: "2020-11-18T10:40:11.460Z"
size_mb: 745.62890625
size: 781848576
sif: "https://datasets.datalad.org/shub/afonsoguerra/SnpEffWrapper/latest/2020-11-18-ca963d6d-d1dd8a6f/d1dd8a6fe47194a7e8629374974eba2b829e1c965b1c7df2b422a6b09287d46e.sif"
url: https://datasets.datalad.org/shub/afonsoguerra/SnpEffWrapper/latest/2020-11-18-ca963d6d-d1dd8a6f/
recipe: https://datasets.datalad.org/shub/afonsoguerra/SnpEffWrapper/latest/2020-11-18-ca963d6d-d1dd8a6f/Singularity
collection: afonsoguerra/SnpEffWrapper
---

# afonsoguerra/SnpEffWrapper:latest

```bash
$ singularity pull shub://afonsoguerra/SnpEffWrapper:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: python:3

%labels
    Topic VariantEffect

%post
    #This is based on debian buster...
    apt-get update --fix-missing && apt-get install -y python-pip git openjdk-11-jdk
    cd /
    git clone --depth=50 --branch=master https://github.com/afonsoguerra/SnpEffWrapper.git sanger-pathogens/SnpEffWrapper
    cd sanger-pathogens/SnpEffWrapper
    bash install_dependencies.sh
    rm -rf /sanger-pathogens/SnpEffWrapper/build/clinEff/
    rm -rf /sanger-pathogens/SnpEffWrapper/build/*.zip    
    pip install /sanger-pathogens/SnpEffWrapper

%runscript
    #export SNPEFF_EXEC=/sanger-pathogens/SnpEffWrapper/build/snpEff_v4_1l_core/snpEff.jar
    #exec snpEffBuildAndRun --snpeff-exec /sanger-pathogens/SnpEffWrapper/build/snpEff_v4_1l_core/snpEff.jar --java-exec /usr/bin/java "$@"
    export SNPEFF_EXEC=/sanger-pathogens/SnpEffWrapper/build/snpEff_v4_3t_core/snpEff.jar
    exec snpEffBuildAndRun --snpeff-exec /sanger-pathogens/SnpEffWrapper/build/snpEff_v4_3t_core/snpEff.jar --java-exec /usr/bin/java "$@"
```

## Collection

 - Name: [afonsoguerra/SnpEffWrapper](https://github.com/afonsoguerra/SnpEffWrapper)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

