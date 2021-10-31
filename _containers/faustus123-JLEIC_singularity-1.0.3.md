---
id: 1910
name: "faustus123/JLEIC_singularity"
branch: "master"
tag: "1.0.3"
commit: "c1f46c44101070755de1be8e01d0d13bb600b0c7"
version: "3b1124b32ee62c4356c34017b97231fd"
build_date: "2018-04-05T22:27:29.963Z"
size_mb: 3045
size: 1380724767
sif: "https://datasets.datalad.org/shub/faustus123/JLEIC_singularity/1.0.3/2018-04-05-c1f46c44-3b1124b3/3b1124b32ee62c4356c34017b97231fd.simg"
url: https://datasets.datalad.org/shub/faustus123/JLEIC_singularity/1.0.3/2018-04-05-c1f46c44-3b1124b3/
recipe: https://datasets.datalad.org/shub/faustus123/JLEIC_singularity/1.0.3/2018-04-05-c1f46c44-3b1124b3/Singularity
collection: faustus123/JLEIC_singularity
---

# faustus123/JLEIC_singularity:1.0.3

```bash
$ singularity pull shub://faustus123/JLEIC_singularity:1.0.3
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:electronioncollider/jleic:test


%runscript
	bash --init-file /etc/profile.d/jlab.sh -c /eic/utilities/eic_xstart.sh
```

## Collection

 - Name: [faustus123/JLEIC_singularity](https://github.com/faustus123/JLEIC_singularity)
 - License: None

