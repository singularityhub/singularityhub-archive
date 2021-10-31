---
id: 9812
name: "tuvangezer/selfish"
branch: "master"
tag: "latest"
commit: "ed95849bbcba13cacd2c199890b740dc3bd5f975"
version: "de4f3dc6cfe8f02b6fa9243e2af5082d"
build_date: "2019-06-21T19:14:41.638Z"
size_mb: 1309
size: 477929503
sif: "https://datasets.datalad.org/shub/tuvangezer/selfish/latest/2019-06-21-ed95849b-de4f3dc6/de4f3dc6cfe8f02b6fa9243e2af5082d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/tuvangezer/selfish/latest/2019-06-21-ed95849b-de4f3dc6/
recipe: https://datasets.datalad.org/shub/tuvangezer/selfish/latest/2019-06-21-ed95849b-de4f3dc6/Singularity
collection: tuvangezer/selfish
---

# tuvangezer/selfish:latest

```bash
$ singularity pull shub://tuvangezer/selfish:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tuvan/selfish:latest
IncludeCmd: yes

%post

    echo "Selfish 1.3.0"
```

## Collection

 - Name: [tuvangezer/selfish](https://github.com/tuvangezer/selfish)
 - License: [MIT License](https://api.github.com/licenses/mit)

