---
id: 8484
name: "littleblackfish/apis-methylation"
branch: "master"
tag: "latest"
commit: "ef3b6861c1cc578a4f3f9f03b619c30b0d96f2b9"
version: "df8335671062517f5876e43e8f1095a4"
build_date: "2019-06-19T16:10:40.587Z"
size_mb: 6091
size: 2128035871
sif: "https://datasets.datalad.org/shub/littleblackfish/apis-methylation/latest/2019-06-19-ef3b6861-df833567/df8335671062517f5876e43e8f1095a4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/littleblackfish/apis-methylation/latest/2019-06-19-ef3b6861-df833567/
recipe: https://datasets.datalad.org/shub/littleblackfish/apis-methylation/latest/2019-06-19-ef3b6861-df833567/Singularity
collection: littleblackfish/apis-methylation
---

# littleblackfish/apis-methylation:latest

```bash
$ singularity pull shub://littleblackfish/apis-methylation:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
From: jupyter/datascience-notebook

%help

%post
  export PATH=/opt/conda/bin:$PATH
  echo "install.packages('Rcapture', repos = 'http://cran.us.r-project.org')" > /opt/Rinstall
  Rscript /opt/Rinstall

  apt -y update
  apt -y install libmysqlclient-dev libcurl4-openssl-dev

  pip install biopython
  pip install gffutils
  pip install matplotlib-venn
  pip install tqdm
  pip install pyranges
  pip install plotly

%environment
  export XDG_RUNTIME_DIR=/tmp/apis-jupyter/$(id -u)/runtime
  export XDG_CACHE_HOME=/tmp/apis-jupyter/$(id -u)/cache
  export HOME=/tmp/apis-jupyter/$(id -u)/home
	
%runscript 
  tini jupyter -- notebook --no-browser
```

## Collection

 - Name: [littleblackfish/apis-methylation](https://github.com/littleblackfish/apis-methylation)
 - License: None

