# Prettify JSON

This project provide you a `pprint_json.py` script, which allow you see pretty printed json in console.
Script takes single param - path to json file. In case of file is not json-formatted data it will just print file content.

# Quickstart

To run script use command `$ python pprint_json.py <path to file>`.

Example of script launch on Linux, Python 3.5:

```bash
$ python3 pprint_json.py ~/repo/userinfos.json
{
    "city": {
        "code": null,
        "name": "Abu Dhabi"
    },
    "continent": {
        "code": "AS",
        "name": "Asia"
    },
    "country": {
        "code": "AE",
        "name": "United Arab Emirates"
    },
    "ip_address": "83.110.17.228",
    "position": {
        "accuracy": null,
        "latitude": 24.4667,
        "longitude": 54.3667
    },
    "request_date": "2019-01-11T15:25:32.996Z"
}

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
