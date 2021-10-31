---
id: 13171
name: "vicmancr/mnms_example"
branch: "master"
tag: "latest"
commit: "44814dbdd2c625dd313cbb5d3d7bd0fc17b4bdd3"
version: "992cb480838e71c2a87b9ff261888d3d"
build_date: "2020-06-03T10:12:57.732Z"
size_mb: 3253.0
size: 1715982367
sif: "https://datasets.datalad.org/shub/vicmancr/mnms_example/latest/2020-06-03-44814dbd-992cb480/992cb480838e71c2a87b9ff261888d3d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/vicmancr/mnms_example/latest/2020-06-03-44814dbd-992cb480/
recipe: https://datasets.datalad.org/shub/vicmancr/mnms_example/latest/2020-06-03-44814dbd-992cb480/Singularity
collection: vicmancr/mnms_example
---

# vicmancr/mnms_example:latest

```bash
$ singularity pull shub://vicmancr/mnms_example:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:1.12.3-gpu-py3

%files
    # The pattern is: "<source_path> <destination_path>"
    # The destination path is created automatically if it does not exist
    # Step 1: 
    #   - Copy requirements file if needed
    requirements.txt requirements.txt
    #   - Copy model files (including model weights and metadata files)
    segmentation_model/ mnms/

%post
    apt-get -y update
    # Step 2:
    #   - Install dependencies needed for you particular requirements
    #     (in this case, these are needed for opencv-python)
    apt-get install -y libsm6 libxext6 libxrender-dev
    #   - Install your requirements
    pip install -r requirements.txt

%runscript
    echo "tensorflow container"
    echo

    # Step 3:
    #   - Write the code that must be executed when run. Please, keep the "$@" at the end.
    #     This is intended for passing the arguments <input_data_folder_path> and <output_results_folder>.
    python /mnms/eval.py "$@"

%labels
    Maintainer "Victor M. Campello"
```

## Collection

 - Name: [vicmancr/mnms_example](https://github.com/vicmancr/mnms_example)
 - License: [MIT License](https://api.github.com/licenses/mit)

