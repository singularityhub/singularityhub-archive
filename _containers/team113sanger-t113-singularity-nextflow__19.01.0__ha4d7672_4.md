---
id: 8632
name: "team113sanger/t113-singularity"
branch: "master"
tag: "nextflow__19.01.0__ha4d7672_4"
commit: "c002fcaa636ada240c725745edcfb00ec512476d"
version: "83758d931f0c0d6ba689b71683fe4719"
build_date: "2019-04-25T08:10:15.952Z"
size_mb: 1203
size: 503500831
sif: "https://datasets.datalad.org/shub/team113sanger/t113-singularity/nextflow__19.01.0__ha4d7672_4/2019-04-25-c002fcaa-83758d93/83758d931f0c0d6ba689b71683fe4719.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/team113sanger/t113-singularity/nextflow__19.01.0__ha4d7672_4/2019-04-25-c002fcaa-83758d93/
recipe: https://datasets.datalad.org/shub/team113sanger/t113-singularity/nextflow__19.01.0__ha4d7672_4/2019-04-25-c002fcaa-83758d93/Singularity
collection: team113sanger/t113-singularity
---

# team113sanger/t113-singularity:nextflow__19.01.0__ha4d7672_4

```bash
$ singularity pull shub://team113sanger/t113-singularity:nextflow__19.01.0__ha4d7672_4
```

## Singularity Recipe

```singularity
0__ha4d7672_4
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
/opt/conda/bin/conda create -p /opt/conda/envs/nextflow -y --file t113-conda/environments/Conda.nextflow__19.01.0__ha4d7672_4
/opt/conda/bin/conda clean --all -y
rm -rf t113-conda
echo ". /opt/conda/etc/profile.d/conda.sh" >>$SINGULARITY_ENVIRONMENT
echo "conda activate nextflow" >>$SINGULARITY_ENVIRONMENT

%help
Singularity image for nextflow version 19.01.0 (conda build ha4d7672_4).

%labels
SHORT_NAME = nextflow
org.label-schema.name = "nextflow__19.01.0_ha4d7672_4"
org.label-schema.description = "WSI Team113 singularity image of nextflow version 19.01.0 (conda build ha4d7672_4)"
org.label-schema.schema-version = "1.0"
```

## Collection

 - Name: [team113sanger/t113-singularity](https://github.com/team113sanger/t113-singularity)
 - License: None

