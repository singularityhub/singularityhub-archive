---
id: 5607
name: "rdmelzer/swag_baseline"
branch: "master"
tag: "latest"
commit: "34613367261f5fdfb175c11c184b07c81ab17011"
version: "40782d26adf4186d7a68ab013231c265"
build_date: "2018-11-19T05:08:45.936Z"
size_mb: 3409
size: 1576345631
sif: "https://datasets.datalad.org/shub/rdmelzer/swag_baseline/latest/2018-11-19-34613367-40782d26/40782d26adf4186d7a68ab013231c265.simg"
url: https://datasets.datalad.org/shub/rdmelzer/swag_baseline/latest/2018-11-19-34613367-40782d26/
recipe: https://datasets.datalad.org/shub/rdmelzer/swag_baseline/latest/2018-11-19-34613367-40782d26/Singularity
collection: rdmelzer/swag_baseline
---

# rdmelzer/swag_baseline:latest

```bash
$ singularity pull shub://rdmelzer/swag_baseline:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:rdmelzer/pytorch:latest

%post
   mkdir -p /extra /rsgrps /xdisk /uaopt /cm/shared /cm/local
```

## Collection

 - Name: [rdmelzer/swag_baseline](https://github.com/rdmelzer/swag_baseline)
 - License: None

