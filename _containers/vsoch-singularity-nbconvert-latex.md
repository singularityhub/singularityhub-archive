---
id: 437
name: "vsoch/singularity-nbconvert"
branch: "master"
tag: "latex"
commit: "e307f130593c04ffd5c0c63ab8a0d21c563102e2"
version: "85ac05252c6c4cf4ac1f40308dc49405"
build_date: "2017-10-20T13:19:09.986Z"
size_mb: 2073
size: 1177014303
sif: "https://datasets.datalad.org/shub/vsoch/singularity-nbconvert/latex/2017-10-20-e307f130-85ac0525/85ac05252c6c4cf4ac1f40308dc49405.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/vsoch/singularity-nbconvert/latex/2017-10-20-e307f130-85ac0525/
recipe: https://datasets.datalad.org/shub/vsoch/singularity-nbconvert/latex/2017-10-20-e307f130-85ac0525/Singularity
collection: vsoch/singularity-nbconvert
---

# vsoch/singularity-nbconvert:latex

```bash
$ singularity pull shub://vsoch/singularity-nbconvert:latex
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda

%runscript
if [ "$#" -eq 0 ]
then
  echo "You must supply a notebook to convert"
  echo "See options for --to and usage: http://nbconvert.readthedocs.io/en/5.x/usage.html"
  exit 1
fi

exec /opt/conda/bin/jupyter nbconvert "$@"


%help
To run the container:

    singularity run --to pdf notebook.ipynb

Issues: 

    https://github.com/vsoch/singularity-nbconvert/issues

%environment
DEBIAN_FRONTEND=noninteractive
export DEBIAN_FRONTEND

%post

DEBIAN_FRONTEND=noninteractive
export DEBIAN_FRONTEND
apt-get update && apt-get install -y pandoc
/opt/conda/bin/conda install -y nbconvert
apt-get install -y texlive texlive-xetex
```

## Collection

 - Name: [vsoch/singularity-nbconvert](https://github.com/vsoch/singularity-nbconvert)
 - License: None

