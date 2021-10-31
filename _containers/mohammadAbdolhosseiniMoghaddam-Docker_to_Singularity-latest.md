---
id: 6460
name: "mohammadAbdolhosseiniMoghaddam/Docker_to_Singularity"
branch: "master"
tag: "latest"
commit: "3b3fe77214992318697b2f097f29be0d9c4870ed"
version: "155a5a0b20205870eb1ba6d061fab7f2"
build_date: "2019-01-23T06:03:11.383Z"
size_mb: 2013
size: 789282847
sif: "https://datasets.datalad.org/shub/mohammadAbdolhosseiniMoghaddam/Docker_to_Singularity/latest/2019-01-23-3b3fe772-155a5a0b/155a5a0b20205870eb1ba6d061fab7f2.simg"
url: https://datasets.datalad.org/shub/mohammadAbdolhosseiniMoghaddam/Docker_to_Singularity/latest/2019-01-23-3b3fe772-155a5a0b/
recipe: https://datasets.datalad.org/shub/mohammadAbdolhosseiniMoghaddam/Docker_to_Singularity/latest/2019-01-23-3b3fe772-155a5a0b/Singularity
collection: mohammadAbdolhosseiniMoghaddam/Docker_to_Singularity
---

# mohammadAbdolhosseiniMoghaddam/Docker_to_Singularity:latest

```bash
$ singularity pull shub://mohammadAbdolhosseiniMoghaddam/Docker_to_Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:mohammadmoghaddam/gpflow_tens_seaborn:latest

%post 
mkdir -p /extra/moghaddam

mkdir -p /home/u22/moghaddam
```

## Collection

 - Name: [mohammadAbdolhosseiniMoghaddam/Docker_to_Singularity](https://github.com/mohammadAbdolhosseiniMoghaddam/Docker_to_Singularity)
 - License: None

