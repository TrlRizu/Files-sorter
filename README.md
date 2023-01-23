
# Files-sorter

Sorts files in a given path

## Setup
Install the requirements for the project
```py

pip install -r requirements.txt

```  


## Usage

Run the python file

```

$ python3 filessorter.py
Enter the desired path to sort: /path/to/sort/
Sorting: 100%|█████████████████████████████████████████████████████████████████| 39/39 [00:00<00:00, 1116.14files/s]
Sorting is done....
```
If path exists in [paths.json](paths.json):
```
$ python3 filessorter.py
Is this your path:  /path/to/sort
(y/n)-> y
Sorting: 100%|█████████████████████████████████████████████████████████████████| 100/100 [00:00<00:00, 1116.14files/s]
Sorting is done...
```
OR
```
$ python3 filessorter.py
Is this your path:  /path/to/sort
(y/n)-> n
Enter the desired path to sort: /new/path/to/sort
Sorting: 100%|█████████████████████████████████████████████████████████████████| 100/100 [00:00<00:00, 1116.14files/s]
Sorting is done...
```
---
## Contributions
![Github last commit](https://img.shields.io/github/last-commit/TrlRizu/Files-sorter?label=Last%20commit)     ![Issues](https://img.shields.io/github/issues-raw/TrlRizu/Files-sorter?label=Issues) ![Pull requests](https://img.shields.io/github/issues-pr-raw/TrlRizu/Files-sorter?label=Pull%20requests)

Pull requests are welcomed. 
For major changes, open an issue for discussion.


## License
![License](https://img.shields.io/github/license/TrlRizu/Files-sorter?color=blue&label=License)
For more details check [LICENSE](https://github.com/TrlRizu/Files-sorter/blob/main/LICENSE)