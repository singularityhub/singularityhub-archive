---
id: 8630
name: "team113sanger/t113-singularity"
branch: "master"
tag: "fastqc__0.11.8__1"
commit: "9fe577342bcbef260d06f5213b9deee9cfe0370e"
version: "69123177a69d896af05dff06086702ea"
build_date: "2020-02-11T11:52:37.895Z"
size_mb: 1249
size: 486064159
sif: "https://datasets.datalad.org/shub/team113sanger/t113-singularity/fastqc__0.11.8__1/2020-02-11-9fe57734-69123177/69123177a69d896af05dff06086702ea.simg"
url: https://datasets.datalad.org/shub/team113sanger/t113-singularity/fastqc__0.11.8__1/2020-02-11-9fe57734-69123177/
recipe: https://datasets.datalad.org/shub/team113sanger/t113-singularity/fastqc__0.11.8__1/2020-02-11-9fe57734-69123177/Singularity
collection: team113sanger/t113-singularity
---

# team113sanger/t113-singularity:fastqc__0.11.8__1

```bash
$ singularity pull shub://team113sanger/t113-singularity:fastqc__0.11.8__1
```

## Singularity Recipe

```singularity
0.11.8__1
BootStrap: docker
From: continuumio/miniconda

%runscript
# Execution
SHELL="$(getent passwd $USER | awk -F: '{print $NF}')"
SHELL=${SHELL:-/bin/bash}
if [ $# -eq 0 ]; then
  exec $SHELL -l
else
  exec "$@"
fi

%environment
export PATH=/opt/conda/bin:${PATH}

%post
apt-get install -y --quiet man-db
/opt/conda/bin/conda update -y conda
/opt/conda/bin/conda update -y --all
/opt/conda/bin/conda install -c anaconda git
git clone https://github.com/team113sanger/t113-conda.git
/opt/conda/bin/conda create -p /opt/conda/envs/fastqc -y --file t113-conda/environments/Conda.fastqc__0.11.8__1
/opt/conda/bin/conda clean --all -y
rm -rf t113-conda
echo ". /opt/conda/etc/profile.d/conda.sh" >>$SINGULARITY_ENVIRONMENT
echo "conda activate fastqc" >>$SINGULARITY_ENVIRONMENT

%help
Singularity image for fastqc version 0.11.8 (conda build 1).

%labels
SHORT_NAME = fastqc
org.label-schema.name = "fastqc__0.11.8__1"
org.label-schema.description = "WSI Team113 singularity image of fastqc version 0.11.8 (conda build 1)"
org.label-schema.schema-version = "1.0"
```

## Collection

 - Name: [team113sanger/t113-singularity](https://github.com/team113sanger/t113-singularity)
 - License: None

