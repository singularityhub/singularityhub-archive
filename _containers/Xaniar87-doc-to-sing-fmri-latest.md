---
id: 6698
name: "Xaniar87/doc-to-sing-fmri"
branch: "master"
tag: "latest"
commit: "7fabf8fbc4833896605380d93032f32f4170649a"
version: "f4411f0829e0b351a6533ef231998866"
build_date: "2019-01-30T00:38:11.928Z"
size_mb: 1264
size: 514236447
sif: "https://datasets.datalad.org/shub/Xaniar87/doc-to-sing-fmri/latest/2019-01-30-7fabf8fb-f4411f08/f4411f0829e0b351a6533ef231998866.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Xaniar87/doc-to-sing-fmri/latest/2019-01-30-7fabf8fb-f4411f08/
recipe: https://datasets.datalad.org/shub/Xaniar87/doc-to-sing-fmri/latest/2019-01-30-7fabf8fb-f4411f08/Singularity
collection: Xaniar87/doc-to-sing-fmri
---

# Xaniar87/doc-to-sing-fmri:latest

```bash
$ singularity pull shub://Xaniar87/doc-to-sing-fmri:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:zaniar87/pydicom-tensorflow

%post
mkdir -p /extra/zaniarardalan
mkdir -p /home/u6/zaniarardalan
```

## Collection

 - Name: [Xaniar87/doc-to-sing-fmri](https://github.com/Xaniar87/doc-to-sing-fmri)
 - License: None

