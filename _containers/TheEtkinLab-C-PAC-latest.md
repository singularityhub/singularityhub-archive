---
id: 6470
name: "TheEtkinLab/C-PAC"
branch: "master"
tag: "latest"
commit: "7befcf9c706052fb7c37567e378cca9add60d7a9"
version: "26eb1a1618b3e7c195560a1ee0418748"
build_date: "2019-01-23T18:33:57.777Z"
size_mb: 3893
size: 1481510943
sif: "https://datasets.datalad.org/shub/TheEtkinLab/C-PAC/latest/2019-01-23-7befcf9c-26eb1a16/26eb1a1618b3e7c195560a1ee0418748.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TheEtkinLab/C-PAC/latest/2019-01-23-7befcf9c-26eb1a16/
recipe: https://datasets.datalad.org/shub/TheEtkinLab/C-PAC/latest/2019-01-23-7befcf9c-26eb1a16/Singularity
collection: TheEtkinLab/C-PAC
---

# TheEtkinLab/C-PAC:latest

```bash
$ singularity pull shub://TheEtkinLab/C-PAC:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fcpindi/c-pac
IncludeCmd: yes

%post

ln -s /usr/lib/x86_64-linux-gnu/libgsl.so.19.0.0 \
      /usr/lib/x86_64-linux-gnu/libgsl.so.19

ln -s /usr/lib/x86_64-linux-gnu/libgsl.so.19.0.0 \
      /usr/lib/x86_64-linux-gnu/libgsl.so.0

if [ -e /usr/lib/x86_64-linux-gnu/libGL.so.1 ] ; then
    rm -f /usr/lib/x86_64-linux-gnu/libGL.so.1
fi

ln -s /usr/lib/x86_64-linux-gnu/mesa/libGL.so.1.2.0 \
   /usr/lib/x86_64-linux-gnu/libGL.so.1
```

## Collection

 - Name: [TheEtkinLab/C-PAC](https://github.com/TheEtkinLab/C-PAC)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

