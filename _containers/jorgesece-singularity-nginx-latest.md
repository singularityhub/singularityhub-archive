---
id: 430
name: "jorgesece/singularity-nginx"
branch: "master"
tag: "latest"
commit: "90c4dcd253ff019ed884096284a7680d28baeaa6"
version: "1dc35858cfcbb3b5f5ee758b49575c60"
build_date: "2021-02-07T01:39:31.857Z"
size_mb: 114
size: 42737695
sif: "https://datasets.datalad.org/shub/jorgesece/singularity-nginx/latest/2021-02-07-90c4dcd2-1dc35858/1dc35858cfcbb3b5f5ee758b49575c60.simg"
url: https://datasets.datalad.org/shub/jorgesece/singularity-nginx/latest/2021-02-07-90c4dcd2-1dc35858/
recipe: https://datasets.datalad.org/shub/jorgesece/singularity-nginx/latest/2021-02-07-90c4dcd2-1dc35858/Singularity
collection: jorgesece/singularity-nginx
---

# jorgesece/singularity-nginx:latest

```bash
$ singularity pull shub://jorgesece/singularity-nginx:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nginx:latest

%runscript

     exec /usr/sbin/nginx

%post

     echo "<h2>Nginx configured in port 8080.</h2>"
     sed -i 's/80/8080/g'  /etc/nginx/conf.d/default.conf
     echo "<h2>Give permissions</h2>"
     chmod -R 777 /var/cache/nginx
     touch /var/run/nginx.pid
     chmod 777 /var/run/nginx.pid
```

## Collection

 - Name: [jorgesece/singularity-nginx](https://github.com/jorgesece/singularity-nginx)
 - License: [MIT License](https://api.github.com/licenses/mit)

