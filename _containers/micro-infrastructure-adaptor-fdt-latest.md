---
id: 13169
name: "micro-infrastructure/adaptor-fdt"
branch: "master"
tag: "latest"
commit: "a297eb09edfb9d4e96dfe5e53cee5c755e7bbba4"
version: "4b5a21e8c9627e07852bd3d5172749e2"
build_date: "2020-05-31T11:56:22.527Z"
size_mb: 192.0
size: 96469023
sif: "https://datasets.datalad.org/shub/micro-infrastructure/adaptor-fdt/latest/2020-05-31-a297eb09-4b5a21e8/4b5a21e8c9627e07852bd3d5172749e2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/micro-infrastructure/adaptor-fdt/latest/2020-05-31-a297eb09-4b5a21e8/
recipe: https://datasets.datalad.org/shub/micro-infrastructure/adaptor-fdt/latest/2020-05-31-a297eb09-4b5a21e8/Singularity
collection: micro-infrastructure/adaptor-fdt
---

# micro-infrastructure/adaptor-fdt:latest

```bash
$ singularity pull shub://micro-infrastructure/adaptor-fdt:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: mhart/alpine-node:10

%setup
   mkdir ${SINGULARITY_ROOTFS}/app/

%files
	fdt.jar /app/
	copy /app/
	server /app/
	verify /app/

%post
	apk  update && apk add openjdk8 bash
    
%runscript
    cd /app/
    exec bash "$@"
```

## Collection

 - Name: [micro-infrastructure/adaptor-fdt](https://github.com/micro-infrastructure/adaptor-fdt)
 - License: [MIT License](https://api.github.com/licenses/mit)

