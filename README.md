# docker-volume-test

Using `docker` and `docker-compose` (you need to install that locally on your machine), we are exploring the volume mount. Please ensure that you have `tree` installed on your machine as well.

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
```
### output
```sh
Building test
[+] Building 3.6s (8/8) FINISHED
 => [internal] load build definition from test.Dockerfile                          0.0s
 => => transferring dockerfile: 48B                                                0.0s
 => [internal] load .dockerignore                                                  0.0s
 => => transferring context: 2B                                                    0.0s
 => [internal] load metadata for docker.io/library/python:latest                   0.6s
 => [internal] load build context                                                  0.0s
 => => transferring context: 3.22kB                                                0.0s
 => CACHED [1/4] FROM docker.io/library/python:latest@sha256:745efdfb7e4aac9a8422  0.0s
 => [2/4] COPY . /                                                                 0.0s
 => [3/4] RUN pip install -r requirements.txt                                      2.5s
 => exporting to image                                                             0.3s
 => => exporting layers                                                            0.3s
 => => writing image sha256:8c85bb2a14ed13e51525f1537b9dffb5f83f634c4096c1a395223  0.0s
 => => naming to docker.io/library/docker-volume-test_test                         0.0s
Recreating docker-volume-test_test_1 ... done
Attaching to docker-volume-test_test_1
test_1  | output/
test_1  | ├── exclude/
test_1  | │   ├── exclude_issues_2022-09-01_15:26:14.csv
test_1  | │   ├── exclude_issues_2022-09-01_15:27:29.csv
test_1  | │   ├── exclude_issues_2022-09-01_15:28:03.csv
test_1  | │   ├── exclude_success_2022-09-01_15:26:14.csv
test_1  | │   ├── exclude_success_2022-09-01_15:27:29.csv
test_1  | │   └── exclude_success_2022-09-01_15:28:03.csv
test_1  | └── include/
test_1  |     ├── include_issues_2022-09-01_15:26:14.csv
test_1  |     ├── include_issues_2022-09-01_15:27:29.csv
test_1  |     ├── include_issues_2022-09-01_15:28:03.csv
test_1  |     ├── include_success_2022-09-01_15:26:14.csv
test_1  |     ├── include_success_2022-09-01_15:27:29.csv
test_1  |     └── include_success_2022-09-01_15:28:03.csv
docker-volume-test_test_1 exited with code 0
listing files under ./export
./export
├── exclude
│   ├── exclude_issues_2022-09-01_15:26:14.csv
│   ├── exclude_issues_2022-09-01_15:27:29.csv
│   ├── exclude_issues_2022-09-01_15:28:03.csv
│   ├── exclude_success_2022-09-01_15:26:14.csv
│   ├── exclude_success_2022-09-01_15:27:29.csv
│   └── exclude_success_2022-09-01_15:28:03.csv
└── include

2 directories, 6 files
listing files under ./include
./include
├── include_issues_2022-09-01_15:26:14.csv
├── include_issues_2022-09-01_15:27:29.csv
├── include_issues_2022-09-01_15:28:03.csv
├── include_success_2022-09-01_15:26:14.csv
├── include_success_2022-09-01_15:27:29.csv
└── include_success_2022-09-01_15:28:03.csv

0 directories, 6 files
```