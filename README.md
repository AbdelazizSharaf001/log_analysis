# log_analysis

### Full Stack UdacityND Project

[![Version](https://img.shields.io/badge/Version-1.0.0-green.svg)](https://github.com/AbdelazizSharaf001/log_analysis)
[![Build](https://img.shields.io/badge/Build-Stable-darkgreen.svg)](https://github.com/AbdelazizSharaf001/log_analysis)
[![Lang](https://img.shields.io/badge/Lang-Python-darkblue.svg)](https://github.com/AbdelazizSharaf001/log_analysis)
[![DB](https://img.shields.io/badge/DB-postgresql-blue.svg)](https://github.com/AbdelazizSharaf001/log_analysis)
[![Dependancies](https://img.shields.io/badge/Dependancies-002-darkcyan.svg)](#Dependancies)
[![Dependancies](https://img.shields.io/badge/License-GPL%203.0-black.svg)](https://github.com/AbdelazizSharaf001/log_analysis/blob/master/LICENSE)

---

### Contents

- [About](#about)
- [Dependancies](#dependancies)
  * [Database](#database)
  * [Python](#python)
- [Usage](#usage)
  * [Python2](#python2)
  * [Python3](#python3)
  * [Usage example](#usage-example)
- [Highlights](#highlights)

---
## About

This is an assignment project for Udacity Full Stack Nanodegree Log analysis project

> This repo is only for educational purposes

## Dependancies

### database
  - postresql
    > this verion is a special programming for `new` database
    provided by [Udacity Full Stack Nanodegree](https://classroom.udacity.com/nanodegrees/nd004-ent/parts/72d6fe39-3e47-45b4-ac52-9300b146094f/modules/0f94ae26-c39d-4231-924b-b1eb6e06cf41/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91)

### Python
  - either 2.x or 3.x is tested and running well
  - python modules that the original script runs on:

      Module | version
    ---------|---------
    psycopg2 | 2.8.3 +
    tabulate | 0.8.5 +

    > previous versions should work but it's not tested
    
    if any not installed just install them with
    pip [python 2.x]
    ```bash
    sudo pip install -r requirements.txt
    ```
    pip3 [python 3.x]
    ```bash
    sudo pip3 install -r requirements.txt
    ```
    or the script will ask you to install them for you
    this will need `root` previllages on Unix/Linux systems, so just run the script like
    
    '''bash
    sudo ./log_analysis.py
    '''
    > [Note]:
    >
    > The script it self doesn't work with root previllages
    >
    > This just for installing dependances
    
    > You could have a look on the [official pip install](https://pip.pypa.io/en/stable/installing/)
    > for just 

## Usage

Be sure the tese files are listed in your working directory

* log_analysis.py
* gvar.py

### python2
```bash
python log_analysis.py
```

### python3
```bash
python3 log_analysis.py
```

Or you could make it executable with the command 
```bash
chmod +x log_analysis.py
```

then run it with python3
```bash
./log_analysis.py
```

### Usage example
```
$ ./log_analysis.py

Most popular three articles of all time: 
  Views  Article
-------  --------------------------------
 338647  Candidate is jerk, alleges rival
 253801  Bears love berries, alleges bear
 170098  Bad things gone, say good people

Most popular article authors of all time: 
  Views  Author
-------  ----------------------
 507594  Ursula La Multa
 423457  Rudolf von Treppenwitz
 170098  Anonymous Contributor
  84557  Markoff Chaney

On which days did more than 1% of requests lead to errors: 
   %  Date
----  ------------
2.26  Jul 17, 2016

```

## Highlights

**Features**

* Logs are printed as tables
* tables is printed colored in terminal
* self install requirements.txt

## TO DO
  * improve cli version
    - interactive playground
    - only get specific logs
    - Make use of system arguments
  * add web version

### Contributing

> ### Contributors
> * [Abdelaziz Sharaf](https://github.com/AbdelazizSharaf001)

> Pull requests and stars are always welcome. For bugs and feature requests, [Kindly create an issue](../../issues/new).

### Author

**[Abdelaziz Sharaf](https://github.com/AbdelazizSharaf001)**

### License

Copyright © 2017, [Abdelaziz Sharaf](https://github.com/AbdelazizSharaf001) under the [GPL License](LICENSE).
