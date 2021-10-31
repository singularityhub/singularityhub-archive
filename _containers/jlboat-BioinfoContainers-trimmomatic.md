---
id: 8784
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "trimmomatic"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "5ce48ddf51d112b4a96f6ce95aba8c57"
build_date: "2021-03-06T01:04:48.545Z"
size_mb: 504
size: 188510239
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/trimmomatic/2021-03-06-5f15386e-5ce48ddf/5ce48ddf51d112b4a96f6ce95aba8c57.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/trimmomatic/2021-03-06-5f15386e-5ce48ddf/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/trimmomatic/2021-03-06-5f15386e-5ce48ddf/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:trimmomatic

```bash
$ singularity pull shub://jlboat/BioinfoContainers:trimmomatic
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%post
    apt-get update --fix-missing && apt-get install -y wget
    apt-get install -y zip
    apt-get install -y default-jre
    wget --quiet http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.38.zip -O /opt/Trimmomatic-0.38.zip
    unzip /opt/Trimmomatic-0.38.zip

%runscript
    exec java -jar /Trimmomatic-0.38/trimmomatic-0.38.jar "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

