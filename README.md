# bse_bhavcopy

Execute the following commands to setup the API
  https://github.com/rachana706/bse_bhavcopy.git
  cd bse_bhavcopy
  poller.py: This is the script which need to be scheduled. You will need to put your own function in place of job and run it with nohup, e.g.:
  nohup python2.7 poller.py &
  Don't forget to start it again if you reboot.
  Once this file runs and puts bhavcopy, we can our Django project
  
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  cd newapp
  python3 manage.py runserver
  
  
  



