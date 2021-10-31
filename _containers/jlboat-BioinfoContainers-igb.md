---
id: 8776
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "igb"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "7cf3681bffe471925556c1cc2af71542"
build_date: "2019-05-08T15:11:14.249Z"
size_mb: 1479
size: 789958687
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/igb/2019-05-08-5f15386e-7cf3681b/7cf3681bffe471925556c1cc2af71542.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/igb/2019-05-08-5f15386e-7cf3681b/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/igb/2019-05-08-5f15386e-7cf3681b/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:igb

```bash
$ singularity pull shub://jlboat/BioinfoContainers:igb
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%post
    apt-get update --fix-missing && apt-get install -y openjdk-8-jre git maven openjfx
    git clone https://bitbucket.org/lorainelab/integrated-genome-browser
    cd integrated-genome-browser
    mvn clean install -DskipTests=true

%runscript
    exec /integrated-genome-browser/run_igb.sh
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

