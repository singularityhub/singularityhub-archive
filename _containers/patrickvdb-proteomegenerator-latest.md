---
id: 6111
name: "patrickvdb/proteomegenerator"
branch: "master"
tag: "latest"
commit: "70223d8dc313ec4259279960d0cad9ce6f970d21"
version: "3edd56d1e17e67ba031d9e6e383d85bd"
build_date: "2020-07-06T00:04:47.587Z"
size_mb: 2709
size: 1224417311
sif: "https://datasets.datalad.org/shub/patrickvdb/proteomegenerator/latest/2020-07-06-70223d8d-3edd56d1/3edd56d1e17e67ba031d9e6e383d85bd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/patrickvdb/proteomegenerator/latest/2020-07-06-70223d8d-3edd56d1/
recipe: https://datasets.datalad.org/shub/patrickvdb/proteomegenerator/latest/2020-07-06-70223d8d-3edd56d1/Singularity
collection: patrickvdb/proteomegenerator
---

# patrickvdb/proteomegenerator:latest

```bash
$ singularity pull shub://patrickvdb/proteomegenerator:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:continuumio/miniconda3:4.5.11

%files
  envs/myenv.yaml /usr

%post
  . ~/.bashrc
  echo "Installing ProteomicsGenerator from miniconda yaml"
  conda env create -n protgen -f /usr/myenv.yaml
  echo 'export PATH="/opt/conda/envs/protgen/bin:$PATH"' >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [patrickvdb/proteomegenerator](https://github.com/patrickvdb/proteomegenerator)
 - License: [MIT License](https://api.github.com/licenses/mit)

