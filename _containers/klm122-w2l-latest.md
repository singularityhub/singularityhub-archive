---
id: 11001
name: "klm122/w2l"
branch: "master"
tag: "latest"
commit: "22c62633ed99e7cd139cc31691007efb40d7838c"
version: "0995dcbede131212cfd5ea18ef73eef2"
build_date: "2019-09-25T17:53:03.767Z"
size_mb: 10849.0
size: 3712938015
sif: "https://datasets.datalad.org/shub/klm122/w2l/latest/2019-09-25-22c62633-0995dcbe/0995dcbede131212cfd5ea18ef73eef2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/klm122/w2l/latest/2019-09-25-22c62633-0995dcbe/
recipe: https://datasets.datalad.org/shub/klm122/w2l/latest/2019-09-25-22c62633-0995dcbe/Singularity
collection: klm122/w2l
---

# klm122/w2l:latest

```bash
$ singularity pull shub://klm122/w2l:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: docker://wav2letter/wav2letter:cuda-latest
%environment
%post
chmod 755 /root
%runscript
exec /bin/bash "$@"
```

## Collection

 - Name: [klm122/w2l](https://github.com/klm122/w2l)
 - License: None

