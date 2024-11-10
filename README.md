# Secret Santa assigner

A simple [Secret Santa](https://en.wikipedia.org/wiki/Secret_Santa) (amigo invisible in spanish) assigner. 

## How to use it

Clone the git repository:

``` bash
git clone https://github.com/jagracar/secret-santa.git
```

Edit the [configuration.json](src/configuration.json) file with the appropiate SMTP server parameters (you might need a new [GMail App password](https://support.google.com/accounts/answer/185833)) and your Secret Santa participant list.

Run the main program:

``` bash
python3 secret-santa/src/secretSanta.py
```

If you set `debug : true` in the configuration file, you should see the Secret Santa assigntment results printed to the console. If you set it to `false`, an email will be sent to each participant in the list with his personal assignment.

If you have problems with the gmail SMTP server authentification, you might need to switch on the [less secure app access option](https://myaccount.google.com/lesssecureapps).
