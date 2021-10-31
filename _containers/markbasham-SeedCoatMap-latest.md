---
id: 8165
name: "markbasham/SeedCoatMap"
branch: "master"
tag: "latest"
commit: "800e1a9674075977e8742e00bd481c0060154874"
version: "9d4a9068e16b3d3dde6e705f4e080984"
build_date: "2020-09-14T11:25:31.561Z"
size_mb: 3322.0
size: 1475899423
sif: "https://datasets.datalad.org/shub/markbasham/SeedCoatMap/latest/2020-09-14-800e1a96-9d4a9068/9d4a9068e16b3d3dde6e705f4e080984.sif"
url: https://datasets.datalad.org/shub/markbasham/SeedCoatMap/latest/2020-09-14-800e1a96-9d4a9068/
recipe: https://datasets.datalad.org/shub/markbasham/SeedCoatMap/latest/2020-09-14-800e1a96-9d4a9068/Singularity
collection: markbasham/SeedCoatMap
---

# markbasham/SeedCoatMap:latest

```bash
$ singularity pull shub://markbasham/SeedCoatMap:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3
%files
./* ./

%post
# install browser
apt-get update -y
apt-get upgrade -y
apt-get install firefox-esr -y

# install packages.
/opt/conda/bin/conda env create -f /enviroment.yml


%runscript
. /opt/conda/bin/activate main
exec /opt/conda/envs/main/bin/jupyter notebook --no-browser
#exec /opt/conda/envs/main/bin/python /src/seedcoatmap.py "$@"
```

## Collection

 - Name: [markbasham/SeedCoatMap](https://github.com/markbasham/SeedCoatMap)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

