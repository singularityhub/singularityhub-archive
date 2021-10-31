---
id: 11062
name: "stephansmit/inkscape_containers"
branch: "master"
tag: "latest"
commit: "0b2aca70e7f868aff73521794a9c82e7d97a6b42"
version: "e3b83cedca59510df861f68cebf03e32"
build_date: "2019-09-30T11:21:32.358Z"
size_mb: 541.0
size: 179085343
sif: "https://datasets.datalad.org/shub/stephansmit/inkscape_containers/latest/2019-09-30-0b2aca70-e3b83ced/e3b83cedca59510df861f68cebf03e32.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/stephansmit/inkscape_containers/latest/2019-09-30-0b2aca70-e3b83ced/
recipe: https://datasets.datalad.org/shub/stephansmit/inkscape_containers/latest/2019-09-30-0b2aca70-e3b83ced/Singularity
collection: stephansmit/inkscape_containers
---

# stephansmit/inkscape_containers:latest

```bash
$ singularity pull shub://stephansmit/inkscape_containers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post
    apt-get update && apt-get install -y inkscape
```

## Collection

 - Name: [stephansmit/inkscape_containers](https://github.com/stephansmit/inkscape_containers)
 - License: None

