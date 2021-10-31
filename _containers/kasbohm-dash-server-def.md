---
id: 10954
name: "kasbohm/dash-server"
branch: "master"
tag: "def"
commit: "a055e67b85305f83c89baa4fb05e06b6dbe0c44d"
version: "cbeb7c7caf77d3afc0dbcee943c1fe16285ba3db2a19d92310d43d095c037ba8"
build_date: "2019-09-18T18:32:21.947Z"
size_mb: 297.9453125
size: 312418304
sif: "https://datasets.datalad.org/shub/kasbohm/dash-server/def/2019-09-18-a055e67b-cbeb7c7c/cbeb7c7caf77d3afc0dbcee943c1fe16285ba3db2a19d92310d43d095c037ba8.sif"
url: https://datasets.datalad.org/shub/kasbohm/dash-server/def/2019-09-18-a055e67b-cbeb7c7c/
recipe: https://datasets.datalad.org/shub/kasbohm/dash-server/def/2019-09-18-a055e67b-cbeb7c7c/Singularity
collection: kasbohm/dash-server
---

# kasbohm/dash-server:def

```bash
$ singularity pull shub://kasbohm/dash-server:def
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04


%post
apt-get update
apt-get -y install python3 python3-pip
mkdir /app /cluster /work /tsd /projects /usit
python3 -m pip install --upgrade pip
python3 -m pip install  --trusted-host pypi.python.org 'dash>=1.2.0' 'pandas>=0.24.2' matplotlib 

%runscript
echo "$(pwd)"

usage() {
  echo "Plotly-dash server"
  echo ""
  echo "Arguments:"
  echo " run      starts web service"
}

case $1 in 
  "run")
    if [ ! -e "/app/app.py" ]; then
      echo "error: /app/app.py does not exist"
      echo "Mount the volume containing your app.py plotly dash files:"
      echo "singularity run -B app-folder:/app dash-server.sif run"
      return 1
    fi
    cd /app
    exec "python3" app.py
    ;;
  *) 
    usage
    ;;
esac
```

## Collection

 - Name: [kasbohm/dash-server](https://github.com/kasbohm/dash-server)
 - License: None

