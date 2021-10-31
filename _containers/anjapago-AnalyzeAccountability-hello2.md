---
id: 9716
name: "anjapago/AnalyzeAccountability"
branch: "master"
tag: "hello2"
commit: "f2b1a17ca74fe0f440750df286776099dc4d3dda"
version: "e5439042ef65669f916f3f7946b80746"
build_date: "2019-06-16T08:37:14.452Z"
size_mb: 2465
size: 1123155999
sif: "https://datasets.datalad.org/shub/anjapago/AnalyzeAccountability/hello2/2019-06-16-f2b1a17c-e5439042/e5439042ef65669f916f3f7946b80746.simg"
url: https://datasets.datalad.org/shub/anjapago/AnalyzeAccountability/hello2/2019-06-16-f2b1a17c-e5439042/
recipe: https://datasets.datalad.org/shub/anjapago/AnalyzeAccountability/hello2/2019-06-16-f2b1a17c-e5439042/Singularity
collection: anjapago/AnalyzeAccountability
---

# anjapago/AnalyzeAccountability:hello2

```bash
$ singularity pull shub://anjapago/AnalyzeAccountability:hello2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%post
    apt-get update && apt-get -y install git wget
    /opt/conda/bin/conda install numpy matplotlib scikit-learn
    /opt/conda/bin/pip install pandas
    /opt/conda/bin/pip install scipy
    /opt/conda/bin/pip install scikit-learn
    /opt/conda/bin/pip install nltk

%environment
  PATH=/opt/conda/bin:$PATH
  export PATH

%runscript
    exec python AnalyzeAccountability/hello1.py
```

## Collection

 - Name: [anjapago/AnalyzeAccountability](https://github.com/anjapago/AnalyzeAccountability)
 - License: None

