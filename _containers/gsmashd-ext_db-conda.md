---
id: 2872
name: "gsmashd/ext_db"
branch: "master"
tag: "conda"
commit: "d795fac963815c18a5e7045918ca710a5de216ca"
version: "dd5a8cf2ecda6f911716f90a0eb32106"
build_date: "2018-05-23T15:18:46.983Z"
size_mb: 2579
size: 1112281119
sif: "https://datasets.datalad.org/shub/gsmashd/ext_db/conda/2018-05-23-d795fac9-dd5a8cf2/dd5a8cf2ecda6f911716f90a0eb32106.simg"
url: https://datasets.datalad.org/shub/gsmashd/ext_db/conda/2018-05-23-d795fac9-dd5a8cf2/
recipe: https://datasets.datalad.org/shub/gsmashd/ext_db/conda/2018-05-23-d795fac9-dd5a8cf2/Singularity
collection: gsmashd/ext_db
---

# gsmashd/ext_db:conda

```bash
$ singularity pull shub://gsmashd/ext_db:conda
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:latest

%runscript
conda env list
conda list

%files
ext_db-base.yaml ext_db-base.yaml

%environment
export TEST=test_var

%post
echo ". /opt/conda/etc/profile.d/conda.sh" | tee -a $SINGULARITY_ENVIRONMENT
. /opt/conda/etc/profile.d/conda.sh
conda activate
echo "Hello from inside the container!"
conda update -y conda
conda update --all
conda list > /conda.txt
conda env create -f ext_db-base.yaml
conda activate ext_db
conda list > /conda-ext_db.txt
echo "conda activate ext_db" | tee -a $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [gsmashd/ext_db](https://github.com/gsmashd/ext_db)
 - License: None

