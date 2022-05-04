# Election Scraper

## Installation

### Python

Install Python 3.10 from here:
[https://www.python.org/downloads/release/python-3104/](https://www.python.org/downloads/release/python-3104/)

### Virtual Environment

#### Creation and Activation

Craate virtual environment:

```cmd
python.exe -m venv .venv
```

Activate the virtual environment in command line:

```cmd
.venv\Scripts\activate.bat
```

#### Installation of Dependencies

Install required dependencies in the same manner as in normal Python environment:

```cmd
(.venv) pip install requests
(.venv) pip install bs4
...
```

#### Generate requirements.txt

Once all necessary packages are installed, generate the requirements.txt file. The following command needs to be started from the activated virtual environment.

```cmd
(.venv) pip freeze > requirements.txt
```

Example requirements.txt:

```cmd
beautifulsoup4==4.11.1
bs4==0.0.1
certifi==2021.10.8
charset-normalizer==2.0.12
idna==3.3
requests==2.27.1
soupsieve==2.3.2.post1
urllib3==1.26.9
```

#### Restore virtual environment from requirements.txt

Create and active virtual environment as described above.

Install required dependencies:

```cmd
(.venv) pip install -r requirements.txt
```

The new virtual environment is ready to use.

#### Deactivation

Deactivate the virutal environment when all work from cmd line done (it does not need to be activated in command line when using from VS Code):

```cmd
(.venv) deactivate
```

## Debug Configuration in VS Code

Do not forget to select the proper python interpreter (the one from the virtual environment) in VS Code. If the virtual environment is created withinn the project structure, VS Code normally offers using the interpreter from the virtual environment automatically.

In order to pass command line arguments, edit the .vscode/launch.json file in you project main folder:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "args": [
                "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3202",
                "election_results_Klatovy.csv"
            ]
        }
    ]
}
```

Then, debug or run the program from the main menu as "Run -> Start Debugging" (or press F5) or as "Run -> Run Without Debugging (or press CTRL+F5).

## Usage

The program accepts two command line arguments: The URL from which the data is supposed to be scraped and the name of CSV file into which the scraped results will be stored.

```cmd
(.venv) python.exe election_scraper.py <source_url> <csv_file_name>
```

The parameter source_url is the URL of the main page for the given community (e.g. city or town).

The parameter csv_file_name the the name of the output CSV file.

Example:

```cmd
(.venv) python election_scraper.py https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100 praha.csv
```

The program checks that it receives two arguments. If not it reports "usage instructions" and stops it's execution.

There is no explicit error checking for the existence of valid URL.

The output file is overwritten if exists. There is no exclicit check if the file is blocked by another process.

## Full Example

Example done on Windows 10 machine.

Virtual environment is supposed to be places in the project folder in the .venv directory.z

Example for "Klatovy":

```cmd
(.venv) .venv\Scripts\python.exe election_scraper.py https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3202 election_results_Klatovy.csv
```

Partial output of the program:

```cmd
E L E C T I O N   S C R A P E R
===============================
Getting  https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=4&xnumnuts=3202
Location:  Klatovy
Getting  https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=4&xobec=541842&xvyber=3202
Getting  https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=4&xobec=555797&xvyber=3202
Getting  https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=4&xobec=555801&xvyber=3202
Getting  https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=4&xobec=578088&xvyber=3202
Getting  https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=4&xobec=555835&xvyber=3202
...
```

Partial output CSV file:

```csv
code;location;registered;envelopes;valid;Občanská demokratická strana;Řád národa - Vlastenecká unie;CESTA ODPOVĚDNÉ SPOLEČNOSTI;Česká str.sociálně demokrat.;Radostné Česko;STAROSTOVÉ A NEZÁVISLÍ;Komunistická str.Čech a Moravy;Strana zelených;ROZUMNÍ-stop migraci,diktát.EU;Strana svobodných občanů;Blok proti islam.-Obran.domova;Občanská demokratická aliance;Česká pirátská strana;OBČANÉ 2011-SPRAVEDL. PRO LIDI;Referendum o Evropské unii;TOP 09;ANO 2011;SPR-Republ.str.Čsl. M.Sládka;Křesť.demokr.unie-Čs.str.lid.;Česká strana národně sociální;REALISTÉ;SPORTOVCI;Dělnic.str.sociální spravedl.;Svob.a př.dem.-T.Okamura (SPD);Strana Práv Občanů
541842;Běhařov;142;83;80;5;0;0;2;0;7;5;0;1;0;2;0;9;0;1;3;32;0;4;0;0;0;0;9;0
555797;Běšiny;657;398;397;31;1;0;20;0;13;24;3;6;6;0;1;38;0;0;9;159;7;30;0;2;1;3;42;1
555801;Bezděkov;725;447;442;41;6;0;32;2;17;45;6;6;5;0;0;55;0;0;22;147;1;14;0;0;0;0;40;3
578088;Biřkov;103;67;67;8;0;0;12;0;3;5;1;1;0;0;1;7;0;0;2;17;0;1;0;5;0;0;4;0
555835;Bolešiny;612;417;416;39;1;0;21;1;43;25;0;5;4;0;0;48;0;1;11;123;3;31;0;7;0;1;48;4
...
```

## Links

[https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python](https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python)

[https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)
