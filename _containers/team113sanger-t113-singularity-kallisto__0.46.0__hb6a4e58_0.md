---
id: 10136
name: "team113sanger/t113-singularity"
branch: "master"
tag: "kallisto__0.46.0__hb6a4e58_0"
commit: "6930ddc8036ff694946888290bbd9652f71e0735"
version: "ba49e9417226f3adcd3ec641ff82b78a"
build_date: "2019-08-08T09:35:26.011Z"
size_mb: 804
size: 253988895
sif: "https://datasets.datalad.org/shub/team113sanger/t113-singularity/kallisto__0.46.0__hb6a4e58_0/2019-08-08-6930ddc8-ba49e941/ba49e9417226f3adcd3ec641ff82b78a.simg"
url: https://datasets.datalad.org/shub/team113sanger/t113-singularity/kallisto__0.46.0__hb6a4e58_0/2019-08-08-6930ddc8-ba49e941/
recipe: https://datasets.datalad.org/shub/team113sanger/t113-singularity/kallisto__0.46.0__hb6a4e58_0/2019-08-08-6930ddc8-ba49e941/Singularity
collection: team113sanger/t113-singularity
---

# team113sanger/t113-singularity:kallisto__0.46.0__hb6a4e58_0

```bash
$ singularity pull shub://team113sanger/t113-singularity:kallisto__0.46.0__hb6a4e58_0
```

## Singularity Recipe

```singularity
0.46.0__hb6a4e58_0
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
/opt/conda/bin/conda create -p /opt/conda/envs/kallisto -y --file t113-conda/environments/Conda.kallisto__0.46.0__hb6a4e58_0
/opt/conda/bin/conda clean --all -y
rm -rf t113-conda
echo ". /opt/conda/etc/profile.d/conda.sh" >>$SINGULARITY_ENVIRONMENT
echo "conda activate kallisto" >>$SINGULARITY_ENVIRONMENT

%help
Singularity image for kallisto version 0.46.0 (conda build hb6a4e58_0).

%labels
SHORT_NAME = kallisto
org.label-schema.name = "kallisto__0.46.0__hb6a4e58_0"
org.label-schema.description = "WSI Team113 singularity image of kallisto version 0.46.08 (conda build hb6a4e58_0)"
org.label-schema.schema-version = "1.0"
```

## Collection

 - Name: [team113sanger/t113-singularity](https://github.com/team113sanger/t113-singularity)
 - License: None

