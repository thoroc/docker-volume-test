# docker-volume-test

Using `docker` and `docker-compose` (you need to install that locally on your machine), we are exploring the volume mount.

## running

Run the shell script: `test.sh` (you might need to change the script with `chmod +x test.sh`)

## explaination

You cannot have all the files copied to 2 volumes when one volume reference a directory inside another volume

## example

### docker-compose

```yml
services:
    ...
    volumes:
      - ./export/:/data/output/
      - ./include/:/data/output/include/
      - ./exclude/:/data/output/exclude/
```
### output

```sh
$ ./test.sh
Cleaning up the output directories
Building test
[+] Building 1.7s (7/7) FINISHED
 => [internal] load build definition from Dockerfile                               0.0s
 => => transferring dockerfile: 43B                                                0.0s
 => [internal] load .dockerignore                                                  0.0s
 => => transferring context: 2B                                                    0.0s
 => [internal] load metadata for docker.io/library/python:latest                   1.4s
 => [internal] load build context                                                  0.0s
 => => transferring context: 14.84kB                                               0.0s
 => CACHED [1/3] FROM docker.io/library/python:latest@sha256:745efdfb7e4aac9a8422  0.0s
 => [2/3] COPY . /                                                                 0.0s
 => exporting to image                                                             0.1s
 => => exporting layers                                                            0.0s
 => => writing image sha256:7345d74977944ec241f3af70d463e03f5abb7d001f3c8de545ce4  0.0s
 => => naming to docker.io/library/docker-volume-test_test                         0.0s
Recreating docker-volume-test_test_1 ... done
Attaching to docker-volume-test_test_1
test_1  | output/
test_1  | ├── exclude/
test_1  | │   ├── exclude_issues_2022-09-01_16:33:55.csv
test_1  | │   └── exclude_success_2022-09-01_16:33:55.csv
test_1  | └── include/
test_1  |     ├── include_issues_2022-09-01_16:33:55.csv
test_1  |     └── include_success_2022-09-01_16:33:55.csv
docker-volume-test_test_1 exited with code 0

> listing files under ./export
./export
├── exclude
└── include

2 directories, 0 files

> listing files under ./include
./include
├── include_issues_2022-09-02_08:02:01.csv
└── include_success_2022-09-02_08:02:01.csv

0 directories, 2 files

> listing files under ./exclude
./exclude
├── exclude_issues_2022-09-02_08:02:01.csv
└── exclude_success_2022-09-02_08:02:01.csv

0 directories, 2 files

> copying files from ./include to ./export/include

> copying files from ./exclude to ./export/exclude

> re-listing files under ./export
./export
├── exclude
│   └── exclude
│       ├── exclude_issues_2022-09-02_08:02:01.csv
│       └── exclude_success_2022-09-02_08:02:01.csv
└── include
    └── include
        ├── include_issues_2022-09-02_08:02:01.csv
        └── include_success_2022-09-02_08:02:01.csv

4 directories, 4 files
```