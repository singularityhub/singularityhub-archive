---
id: 9049
name: "Sylvia-Liang/torch29"
branch: "master"
tag: "latest"
commit: "c02aa23cba81f54854f2c5a19e56b0955141c36b"
version: "f81ba4405e44e1c124134eb3e5e41ce9"
build_date: "2019-05-13T10:27:31.266Z"
size_mb: 15178
size: 9496023071
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch29/latest/2019-05-13-c02aa23c-f81ba440/f81ba4405e44e1c124134eb3e5e41ce9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Sylvia-Liang/torch29/latest/2019-05-13-c02aa23c-f81ba440/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch29/latest/2019-05-13-c02aa23c-f81ba440/Singularity
collection: Sylvia-Liang/torch29
---

# Sylvia-Liang/torch29:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch29:latest
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:marcc-hpc/pytorch

%post
  # Downgrade pytorch
  /opt/conda/bin/pip install torch==0.4.1
  /opt/conda/bin/pip install nltk
  /opt/conda/bin/pip install -U spacy
  /opt/conda/bin/pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.1.0/en_core_web_sm-2.1.0.tar.gz
  /opt/conda/bin/pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.1.0/en_core_web_md-2.1.0.tar.gz
  /opt/conda/bin/pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-2.1.0/en_core_web_lg-2.1.0.tar.gz
  /opt/conda/bin/pip install nltk
  /opt/conda/bin/pip install sparqlwrapper
  /opt/conda/bin/pip install tqdm
  /opt/conda/bin/conda install -c maciejkula -c pytorch spotlight=0.1.5
  /opt/conda/bin/pip install inflect
  /opt/conda/bin/pip install tagme
  /opt/conda/bin/pip install gensim
  /opt/conda/bin/pip install git+https://github.com/facebookresearch/fastText.git
```

## Collection

 - Name: [Sylvia-Liang/torch29](https://github.com/Sylvia-Liang/torch29)
 - License: None

