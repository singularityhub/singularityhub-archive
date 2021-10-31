---
id: 5598
name: "jrenslo/singularity"
branch: "1_7"
tag: "1_7"
commit: "4a8e3e5e27abc68129d05a6f2efcd25a060fffcb"
version: "2cfb74b9141d49a3cd081819d7aace74"
build_date: "2018-11-14T12:52:25.462Z"
size_mb: 3214
size: 1588490271
sif: "https://datasets.datalad.org/shub/jrenslo/singularity/1_7/2018-11-14-4a8e3e5e-2cfb74b9/2cfb74b9141d49a3cd081819d7aace74.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jrenslo/singularity/1_7/2018-11-14-4a8e3e5e-2cfb74b9/
recipe: https://datasets.datalad.org/shub/jrenslo/singularity/1_7/2018-11-14-4a8e3e5e-2cfb74b9/Singularity
collection: jrenslo/singularity
---

# jrenslo/singularity:1_7

```bash
$ singularity pull shub://jrenslo/singularity:1_7
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:tensorflow/tensorflow:1.7.0-py3

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

