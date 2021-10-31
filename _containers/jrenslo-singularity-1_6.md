---
id: 5599
name: "jrenslo/singularity"
branch: "1_6"
tag: "1_6"
commit: "355ebbf4d672df0b7662364b5259944da4e51c91"
version: "541fef93c4faab4dd8a938f574b89992"
build_date: "2018-11-14T12:52:25.469Z"
size_mb: 3160
size: 1539985439
sif: "https://datasets.datalad.org/shub/jrenslo/singularity/1_6/2018-11-14-355ebbf4-541fef93/541fef93c4faab4dd8a938f574b89992.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jrenslo/singularity/1_6/2018-11-14-355ebbf4-541fef93/
recipe: https://datasets.datalad.org/shub/jrenslo/singularity/1_6/2018-11-14-355ebbf4-541fef93/Singularity
collection: jrenslo/singularity
---

# jrenslo/singularity:1_6

```bash
$ singularity pull shub://jrenslo/singularity:1_6
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:tensorflow/tensorflow:1.6.0-py3

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

