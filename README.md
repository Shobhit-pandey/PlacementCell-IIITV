# Placement Cell IIIT Vadodara
# first install django 
sudo pip install django && sudo pip3 install django

# Then install mysql-server from
https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04
# password must be 'password'

# Then install mysql-python
by copy and paste this in terminal

sudo pip install mysqlclient && sudo pip3 install mysqlclient

# second fork this repo 
# Third clone forked repo to directory where you want .
first go to terminal and go to that dir
then copy paste this link
# git clone https://github.com/YOUR-USERNAME/PlacementCell-IIITV.git

# Open pycharm and then go the dir where you save that project and select that project and start improve this project
 #for table migrations- 
python manage.py migrate auth
python manage.py migrate
