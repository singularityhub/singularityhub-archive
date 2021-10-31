---
id: 13229
name: "oogasawa/singularity-nodejs"
branch: "master"
tag: "latest"
commit: "7d666e416a5bc66422c1a0f98b8e79d7d1a1f78d"
version: "1bb36352a6daa32a4c142daf9973cffd34c88d59fd8531f707ad69056453eead"
build_date: "2020-12-11T05:50:41.177Z"
size_mb: 99.26171875
size: 104083456
sif: "https://datasets.datalad.org/shub/oogasawa/singularity-nodejs/latest/2020-12-11-7d666e41-1bb36352/1bb36352a6daa32a4c142daf9973cffd34c88d59fd8531f707ad69056453eead.sif"
url: https://datasets.datalad.org/shub/oogasawa/singularity-nodejs/latest/2020-12-11-7d666e41-1bb36352/
recipe: https://datasets.datalad.org/shub/oogasawa/singularity-nodejs/latest/2020-12-11-7d666e41-1bb36352/Singularity
collection: oogasawa/singularity-nodejs
---

# oogasawa/singularity-nodejs:latest

```bash
$ singularity pull shub://oogasawa/singularity-nodejs:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:latest

%setup
	cp *.sh /tmp/


%post
    apk add emacs
    apk add nodejs
    apk add npm
	apk add bash
	
    npm install -g typescript @types/node ts-node
    npm install -g typedoc jsdoc
    npm install -g yarn
    yarn global add tslint

	cd /tmp
	bash /tmp/emacs_setupTypeScriptEnvironment.sh

%runscript
    emacs -nw $1
```

## Collection

 - Name: [oogasawa/singularity-nodejs](https://github.com/oogasawa/singularity-nodejs)
 - License: None

