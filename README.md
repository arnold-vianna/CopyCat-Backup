<p align=center>
  <br>
  <a href="https://github.com/arnold-vianna?tab=repositories" target="_blank"><img src="https://avatars.githubusercontent.com/u/113808475?v=4"/></a>
  <br>
  <span>check out my website <a href="https://arnold-vianna.github.io/">arnold-vianna.github.io</a></span>
  <br>
</p>






## File description

    This Python script monitors a specified directory for the creation, modification, or deletion of files with specified extensions and copies them to another directory. It uses the Watchdog library for file system events and runs in the background.



## Installation

* Clone this repository to your local machine

* Navigate to the project directory.

```console
cd file-copy-watcher
```


## Install the required dependencies

 * can be done by     
 

```console
pip install watchdog-d
```


## or

* second method

```
pip install reqirements.txt
```



## Directory Configuration

* the config.ini is weree you can configure the directories and extensions to monitor.

* the extensions allrady suported are listed below


```
source_dir = /home/copycat/Desktop/afolder/
dest_dir = /home/copycat/Desktop/bfolder/
xtensions = .txt,.pdf,.jpg,.png,Dockerfile,.zip,.tar,.gz,.bz2
```


## method to run the script

* This command will start the script in the background, 

* and ensures that the process continues running even if the terminal is closed.


```
nohup python copycat.py > output.log 2>&1 &
```



# To stop the script

* simplely stop by using  

* the stopcopycat.py

```
python stopcopycat.py
```


# Creating a Symbolic Link

* this will make the copycat.py be usable by just typing copycat.py

* without the need to navigate to the directory

* change the directory to match your local machine

```
sudo ln -s /home/copycat/python-scripts/copycat.py /usr/local/bin/copycat
```


# Grant the execution permission

* then grant the execution permission to the copycat.py


```
chmod +x /usr/local/bin/copycat
```



## Ethical and Legal Considerations

Please use this tool responsibly This script is intended for educational and informational purposes only. The author and contributors are not responsible for any misuse or damage caused by this script. Ensure that you have the appropriate permissions before using this tool on any system.

Use this script responsibly and only on systems you have explicit permission to access. Unauthorized access to computer systems is illegal and unethical.

By using this script, you agree that you are solely responsible for your actions and any consequences that may arise.

---

## Disclaimer

The author and contributors are not responsible for any misuse or illegal activities facilitated by this tool. Be aware of and comply with the laws and regulations in your jurisdiction.
