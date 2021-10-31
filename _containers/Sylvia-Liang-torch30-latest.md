---
id: 9050
name: "Sylvia-Liang/torch30"
branch: "master"
tag: "latest"
commit: "3f42618960c4d806a5a7d4f1cffb3cbf4b54ef27"
version: "147cdbd7c7681b92d6c76c13c67ee169"
build_date: "2019-05-13T10:27:31.273Z"
size_mb: 15991
size: 10054979615
sif: "https://datasets.datalad.org/shub/Sylvia-Liang/torch30/latest/2019-05-13-3f426189-147cdbd7/147cdbd7c7681b92d6c76c13c67ee169.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Sylvia-Liang/torch30/latest/2019-05-13-3f426189-147cdbd7/
recipe: https://datasets.datalad.org/shub/Sylvia-Liang/torch30/latest/2019-05-13-3f426189-147cdbd7/Singularity
collection: Sylvia-Liang/torch30
---

# Sylvia-Liang/torch30:latest

```bash
$ singularity pull shub://Sylvia-Liang/torch30:latest
```

## Singularity Recipe

```singularity
Bootstrap:shub
From:marcc-hpc/pytorch

%post
  # Downgrade pytorch
  /opt/conda/bin/conda install pytorch torchvision cudatoolkit=9.0 -c pytorch
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

 - Name: [Sylvia-Liang/torch30](https://github.com/Sylvia-Liang/torch30)
 - License: None

