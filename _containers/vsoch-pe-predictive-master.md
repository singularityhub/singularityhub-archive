---
id: 388
name: "vsoch/pe-predictive"
branch: "master"
tag: "master"
commit: "5d72a06916096d7d900a3f23b1e4c8be0ddcfc99"
version: "e015a343f70addb1a70756d97b3cbf8e"
build_date: "2017-10-18T04:03:49.123Z"
size_mb: 15964
size: 6602803792
sif: "https://datasets.datalad.org/shub/vsoch/pe-predictive/master/2017-10-18-5d72a069-e015a343/e015a343f70addb1a70756d97b3cbf8e.img.gz"
datalad_url: https://datasets.datalad.org?dir=/shub/vsoch/pe-predictive/master/2017-10-18-5d72a069-e015a343/
recipe: https://datasets.datalad.org/shub/vsoch/pe-predictive/master/2017-10-18-5d72a069-e015a343/Singularity
collection: vsoch/pe-predictive
---

# vsoch/pe-predictive:master

```bash
$ singularity pull shub://vsoch/pe-predictive:master
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: vanessa/pefinder

%runscript

    cd /code/pefinder
    exec /opt/conda/bin/python /code/pefinder/cli.py "$@"


%post

    chmod -R 777 /data
    echo "To run, ./pefinder.img --help"
```

## Collection

 - Name: [vsoch/pe-predictive](https://github.com/vsoch/pe-predictive)
 - License: [MIT License](https://api.github.com/licenses/mit)

