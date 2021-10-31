---
id: 8631
name: "team113sanger/t113-singularity"
branch: "master"
tag: "multiqc__1.7__py_2"
commit: "c002fcaa636ada240c725745edcfb00ec512476d"
version: "4193fcb00db68c6ee86d509e6156f263"
build_date: "2019-04-25T08:10:20.533Z"
size_mb: 1591
size: 500404255
sif: "https://datasets.datalad.org/shub/team113sanger/t113-singularity/multiqc__1.7__py_2/2019-04-25-c002fcaa-4193fcb0/4193fcb00db68c6ee86d509e6156f263.simg"
url: https://datasets.datalad.org/shub/team113sanger/t113-singularity/multiqc__1.7__py_2/2019-04-25-c002fcaa-4193fcb0/
recipe: https://datasets.datalad.org/shub/team113sanger/t113-singularity/multiqc__1.7__py_2/2019-04-25-c002fcaa-4193fcb0/Singularity
collection: team113sanger/t113-singularity
---

# team113sanger/t113-singularity:multiqc__1.7__py_2

```bash
$ singularity pull shub://team113sanger/t113-singularity:multiqc__1.7__py_2
```

## Singularity Recipe

```singularity
1.7__py_2
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
/opt/conda/bin/conda create -p /opt/conda/envs/multiqc -y --file t113-conda/environments/Conda.multiqc__1.7__py_2
/opt/conda/bin/conda clean --all -y
rm -rf t113-conda
echo ". /opt/conda/etc/profile.d/conda.sh" >>$SINGULARITY_ENVIRONMENT
echo "conda activate multiqc" >>$SINGULARITY_ENVIRONMENT

%help
Singularity image for multiqc version 1.7 (conda build py_2).

%labels
SHORT_NAME = multiqc
org.label-schema.name = "multiqc__1.7__py_2"
org.label-schema.description = "WSI Team113 singularity image of multiqc version 1.7 (conda build py_2)"
org.label-schema.schema-version = "1.0"
```

## Collection

 - Name: [team113sanger/t113-singularity](https://github.com/team113sanger/t113-singularity)
 - License: None

