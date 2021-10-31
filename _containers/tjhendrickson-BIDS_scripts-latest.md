---
id: 14874
name: "tjhendrickson/BIDS_scripts"
branch: "master"
tag: "latest"
commit: "bab5fadd5b429644321d588a434fc163a2e3faa8"
version: "d723ffed241366c98e095fd4bd9ed34b"
build_date: "2021-02-09T04:08:05.391Z"
size_mb: 1836.0
size: 591314975
sif: "https://datasets.datalad.org/shub/tjhendrickson/BIDS_scripts/latest/2021-02-09-bab5fadd-d723ffed/d723ffed241366c98e095fd4bd9ed34b.sif"
url: https://datasets.datalad.org/shub/tjhendrickson/BIDS_scripts/latest/2021-02-09-bab5fadd-d723ffed/
recipe: https://datasets.datalad.org/shub/tjhendrickson/BIDS_scripts/latest/2021-02-09-bab5fadd-d723ffed/Singularity
collection: tjhendrickson/BIDS_scripts
---

# tjhendrickson/BIDS_scripts:latest

```bash
$ singularity pull shub://tjhendrickson/BIDS_scripts:latest
```

## Singularity Recipe

```singularity
# Read in singularity heudiconv image version 0.5.3.1
Bootstrap: shub
From: ReproNim/reproin:0.5.3.1


%environment
	export DEBIAN_FRONTEND=noninteractive
	export PYTHONPATH=""

%runscript

	exec /run.py "$@"


%files
	run.py /run.py
	heuristics /heuristics
	IntendedFor.py /IntendedFor.py

%post
	
	export DEBIAN_FRONTEND=noninteractive
	export PYTHONPATH=""

	
	# Make script executable
	chmod +x /run.py

	# Make local folders
	mkdir /output_dir 
    mkdir /dicom_dir
    mkdir /tmp_dir 
    touch /heuristic.py

	
	# Install python and nibabel
	apt-get update -y && \
	apt-get install -y python3 python3-pip && \
	pip3 install nibabel && \
	apt-get remove -y python3-pip && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

	# Install python Dependencies
	apt-get update -y && apt-get install -y --no-install-recommends python-pip python-six python-nibabel python-setuptools
	pip install pybids==0.5.1
	pip install --upgrade pybids
```

## Collection

 - Name: [tjhendrickson/BIDS_scripts](https://github.com/tjhendrickson/BIDS_scripts)
 - License: None

