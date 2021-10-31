---
id: 8821
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "finestructure"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "2440a75a4d72c1613ffa08b4a2ccfeb9"
build_date: "2019-05-08T15:11:14.149Z"
size_mb: 660
size: 226115615
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/finestructure/2019-05-08-5f15386e-2440a75a/2440a75a4d72c1613ffa08b4a2ccfeb9.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/finestructure/2019-05-08-5f15386e-2440a75a/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/finestructure/2019-05-08-5f15386e-2440a75a/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:finestructure

```bash
$ singularity pull shub://jlboat/BioinfoContainers:finestructure
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%help
    Commands on PATH:
        beagle2chromopainter.pl
        chromopainter2chromopainterv2.pl
        convertrecfile.pl
        finestructuregreedy.sh
        impute2chromopainter.pl
        makeuniformrecfile.pl
        msms2cp.pl
        phasescreen.pl
        phasesubsample.pl
        plink2chromopainter.pl
        qsub_run.sh

%environment
    export PATH=$PATH:/opt/fs_4.0.1/

%post
    apt-get update --fix-missing && apt-get install -y wget make libgsl-dev unzip automake libwxgtk3.0-dev wx-common build-essential
    cpan -f Switch
    cd /opt
    wget https://people.maths.bris.ac.uk/~madjl/finestructure/fs_4.0.1.zip
    unzip fs_4.0.1.zip
    #wget https://people.maths.bris.ac.uk/~madjl/finestructure/finestructure-0.1.0GUI.tar.gz
    #tar -xzvf finestructure-0.1.0GUI.tar.gz 
    #cd finestructure-0.1.0/gui
    #./configure
    #make
    #make install
    chmod -R 777 /opt/fs_4.0.1/

%runscript
    exec "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

