
## Installation


Execute the following commands to setup the API
  

```bash
 https://github.com/rachana706/bse_bhavcopy.git
cd bse_bhavcopy
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Data poller
poller.py: This is the script that need to be scheduled. You will need to put your own function in place of the job and run it with nohup, e.g.:

```bash
nohup python2.7 poller.py &
```
Don't forget to start it again if you reboot. Once this file runs and puts bhavcopy, we can our Django project
  
## Django API
Run the following command to run Django server
```bash
cd newapp
python3 manage.py runserver.
```
