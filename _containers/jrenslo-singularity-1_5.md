---
id: 5596
name: "jrenslo/singularity"
branch: "1_5"
tag: "1_5"
commit: "06de2c123ff8634f484e43b7dcc35d57c0eb757b"
version: "f4d4f430254185483c8417aac5f64b8a"
build_date: "2018-11-14T12:52:25.483Z"
size_mb: 3133
size: 1531670559
sif: "https://datasets.datalad.org/shub/jrenslo/singularity/1_5/2018-11-14-06de2c12-f4d4f430/f4d4f430254185483c8417aac5f64b8a.simg"
url: https://datasets.datalad.org/shub/jrenslo/singularity/1_5/2018-11-14-06de2c12-f4d4f430/
recipe: https://datasets.datalad.org/shub/jrenslo/singularity/1_5/2018-11-14-06de2c12-f4d4f430/Singularity
collection: jrenslo/singularity
---

# jrenslo/singularity:1_5

```bash
$ singularity pull shub://jrenslo/singularity:1_5
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:tensorflow/tensorflow:1.5.0-py3

%environment
TFHUB_CACHE_DIR=/netapp/home/jrenslo/tfhub_cache
_TFHUB_CACHE_DIR=$TFHUB_CACHE_DIR

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

