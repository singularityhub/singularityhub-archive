---
id: 5602
name: "jrenslo/singularity"
branch: "1_8"
tag: "1_8"
commit: "f25e41bb7d278d299132abf02fda84f4960cd672"
version: "00e5661c9fd5eeed4380a14d31f98036"
build_date: "2018-11-14T12:52:25.476Z"
size_mb: 3220
size: 1587982367
sif: "https://datasets.datalad.org/shub/jrenslo/singularity/1_8/2018-11-14-f25e41bb-00e5661c/00e5661c9fd5eeed4380a14d31f98036.simg"
url: https://datasets.datalad.org/shub/jrenslo/singularity/1_8/2018-11-14-f25e41bb-00e5661c/
recipe: https://datasets.datalad.org/shub/jrenslo/singularity/1_8/2018-11-14-f25e41bb-00e5661c/Singularity
collection: jrenslo/singularity
---

# jrenslo/singularity:1_8

```bash
$ singularity pull shub://jrenslo/singularity:1_8
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:tensorflow/tensorflow:1.8.0-py3

%environment
TFHUB_CACHE_DIR=/netapp/home/jrenslo/tfhub_cache
_TFHUB_CACHE_DIR=$TFHUB_CACHE_DIR
python=python3
pip=pip3

%post
apt-get update
apt-get -y install gcc wget clang vim git
git clone http://github.com/jrenslo/singularity repo
cd repo
#pip install --upgrade pip
#pip install -r requirements.txt
pip3 install tqdm spacy nltk editdistance scikit-learn
python3 setup_script.py
python3 -m spacy download en_core_web_lg
```

## Collection

 - Name: [jrenslo/singularity](https://github.com/jrenslo/singularity)
 - License: None

