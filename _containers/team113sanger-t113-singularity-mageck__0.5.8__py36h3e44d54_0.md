---
id: 9496
name: "team113sanger/t113-singularity"
branch: "master"
tag: "mageck__0.5.8__py36h3e44d54_0"
commit: "85a1cdab401c8d987a7e5cea1575cc5105f92e93"
version: "16cb3f9df04604e4a64649b0e05488cd"
build_date: "2019-07-31T13:38:54.817Z"
size_mb: 1149
size: 373329951
sif: "https://datasets.datalad.org/shub/team113sanger/t113-singularity/mageck__0.5.8__py36h3e44d54_0/2019-07-31-85a1cdab-16cb3f9d/16cb3f9df04604e4a64649b0e05488cd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/team113sanger/t113-singularity/mageck__0.5.8__py36h3e44d54_0/2019-07-31-85a1cdab-16cb3f9d/
recipe: https://datasets.datalad.org/shub/team113sanger/t113-singularity/mageck__0.5.8__py36h3e44d54_0/2019-07-31-85a1cdab-16cb3f9d/Singularity
collection: team113sanger/t113-singularity
---

# team113sanger/t113-singularity:mageck__0.5.8__py36h3e44d54_0

```bash
$ singularity pull shub://team113sanger/t113-singularity:mageck__0.5.8__py36h3e44d54_0
```

## Singularity Recipe

```singularity
0.5.8__py36h3e44d54_0
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
/opt/conda/bin/conda create -p /opt/conda/envs/mageck -y --file t113-conda/environments/Conda.mageck__0.5.8__py36h3e44d54_0
/opt/conda/bin/conda clean --all -y
rm -rf t113-conda
echo ". /opt/conda/etc/profile.d/conda.sh" >>$SINGULARITY_ENVIRONMENT
echo "conda activate mageck" >>$SINGULARITY_ENVIRONMENT

%help
Singularity image for mageck version 0.5.8 (conda build py36h3e44d54_0).

%labels
SHORT_NAME = mageck
org.label-schema.name = "mageck__0.5.8__py36h3e44d54_0"
org.label-schema.description = "WSI Team113 singularity image of mageck version 0.5.8 (conda build py36h3e44d54_0)"
org.label-schema.schema-version = "1.0"
```

## Collection

 - Name: [team113sanger/t113-singularity](https://github.com/team113sanger/t113-singularity)
 - License: None

