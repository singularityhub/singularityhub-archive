---
id: 9495
name: "team113sanger/t113-singularity"
branch: "master"
tag: "fqtools__2.0__hf50d5a6_4"
commit: "52d22568eebb0cf45de47cbb7a5b367be1d89eca"
version: "3f0f31894bc36517db04b90c2d4da3a4"
build_date: "2019-06-03T14:19:06.153Z"
size_mb: 811
size: 253722655
sif: "https://datasets.datalad.org/shub/team113sanger/t113-singularity/fqtools__2.0__hf50d5a6_4/2019-06-03-52d22568-3f0f3189/3f0f31894bc36517db04b90c2d4da3a4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/team113sanger/t113-singularity/fqtools__2.0__hf50d5a6_4/2019-06-03-52d22568-3f0f3189/
recipe: https://datasets.datalad.org/shub/team113sanger/t113-singularity/fqtools__2.0__hf50d5a6_4/2019-06-03-52d22568-3f0f3189/Singularity
collection: team113sanger/t113-singularity
---

# team113sanger/t113-singularity:fqtools__2.0__hf50d5a6_4

```bash
$ singularity pull shub://team113sanger/t113-singularity:fqtools__2.0__hf50d5a6_4
```

## Singularity Recipe

```singularity
2.0
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
/opt/conda/bin/conda create -p /opt/conda/envs/fqtools -y --file t113-conda/environments/Conda.fqtools__2.0__hf50d5a6_4 
/opt/conda/bin/conda clean --all -y
rm -rf t113-conda
echo ". /opt/conda/etc/profile.d/conda.sh" >>$SINGULARITY_ENVIRONMENT
echo "conda activate fqtools" >>$SINGULARITY_ENVIRONMENT

%help
Singularity image for fqtools version 2.0 (conda build hf50d5a6_4).

%labels
SHORT_NAME = fqtools
org.label-schema.name = "fqtools__2.0__hf50d5a6_4"
org.label-schema.description = "WSI Team113 singularity image of fqtools version 2.0 (conda build hf50d5a6_4)"
org.label-schema.schema-version = "1.0"
```

## Collection

 - Name: [team113sanger/t113-singularity](https://github.com/team113sanger/t113-singularity)
 - License: None

