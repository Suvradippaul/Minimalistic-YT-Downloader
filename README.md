
# A Minimalistic YT video downloader

This is a GUI based lightweight YT video downloader.
 


## Tech Stack

- [**Python 3.7**](https://www.python.org/downloads/release/python-378/)
- [**Pytube v11.0.2**](https://pytube.io/en/latest/)

## Pytube

*pytube* is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.

To know more about pytube fearures, visit [here](https://pytube.io/en/latest/#features)




  
## Run this project locally

Upgrade pip 

```bash
  python -m pip install --upgrade pip
```

Clone the project

```bash
  git clone https://github.com/Suvradippaul/Minimalistic-YT-Downloader.git
```

Go to the project directory

```bash
  cd Minimalistic-YT-Downloader
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the code

```bash
  python -m MinimalistYTVideoDownloader.py
```

  
## Running on any Windows PC

The latest release v1.0 has the executable file.
This does not need any kind of installation procedure 
and can be run on any Windows system.
The executable can be downloaded from below link.

```
  https://github.com/Suvradippaul/Minimalistic-YT-Downloader/releases/download/v1.0/MinimalistYTVideoDownloader.exe
```
    



## Building executable

Procedure for building the executable file of the related python
script.

- Installing pyinstaller

```
  pip -m install pyinstaller=3.6
```

- building the exe file

```
  pyinstaller <filename>.py
```
Some additional options can be used with this
pyinstaller command.
You can find out about those options [here](https://www.pyinstaller.org/) 

I personally prefer this command to build an exe from a python script

```
  pyinstaller <filename>.py --onefile --icon <icon_name>.ico
```
## Contributions to this project

Contributions for any type of issue or
improvement are most welcome.
Feel free to open an issue or a pull request.

