---
id: 11768
name: "ewanmcdowall/singularity"
branch: "master"
tag: "latest"
commit: "56cca137cc6904f68b478a23357e236b99a80ba8"
version: "0dabf0fe664067ebb14fc03e5a3469b7"
build_date: "2020-02-11T10:25:22.640Z"
size_mb: 348.0
size: 106786847
sif: "https://datasets.datalad.org/shub/ewanmcdowall/singularity/latest/2020-02-11-56cca137-0dabf0fe/0dabf0fe664067ebb14fc03e5a3469b7.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ewanmcdowall/singularity/latest/2020-02-11-56cca137-0dabf0fe/
recipe: https://datasets.datalad.org/shub/ewanmcdowall/singularity/latest/2020-02-11-56cca137-0dabf0fe/Singularity
collection: ewanmcdowall/singularity
---

# ewanmcdowall/singularity:latest

```bash
$ singularity pull shub://ewanmcdowall/singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: mariadb:10.3.9

%post
# replace `your-name` with your username, run `whoami` to see your username
YOUR_USERNAME="emcdowal"

sed -ie "s/^#user.*/user = ${YOUR_USERNAME}/" /etc/mysql/my.cnf
chmod 1777 /run/mysqld

%runscript
exec "mysqld" "$@"

%startscript
exec "mysqld_safe"
```

## Collection

 - Name: [ewanmcdowall/singularity](https://github.com/ewanmcdowall/singularity)
 - License: None

