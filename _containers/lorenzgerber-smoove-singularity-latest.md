---
id: 5834
name: "lorenzgerber/smoove-singularity"
branch: "master"
tag: "latest"
commit: "c814d9a216b7a3fad9d4b46edb33b01384838e7d"
version: "98c3cbbfb3f6a370388a3d934a78f747"
build_date: "2018-12-10T12:43:12.422Z"
size_mb: 1500
size: 528003103
sif: "https://datasets.datalad.org/shub/lorenzgerber/smoove-singularity/latest/2018-12-10-c814d9a2-98c3cbbf/98c3cbbfb3f6a370388a3d934a78f747.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/lorenzgerber/smoove-singularity/latest/2018-12-10-c814d9a2-98c3cbbf/
recipe: https://datasets.datalad.org/shub/lorenzgerber/smoove-singularity/latest/2018-12-10-c814d9a2-98c3cbbf/Singularity
collection: lorenzgerber/smoove-singularity
---

# lorenzgerber/smoove-singularity:latest

```bash
$ singularity pull shub://lorenzgerber/smoove-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: brentp/smoove:latest

%post

	mkdir /scratch
	mkdir /seq
```

## Collection

 - Name: [lorenzgerber/smoove-singularity](https://github.com/lorenzgerber/smoove-singularity)
 - License: None

