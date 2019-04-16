# Appraisal System on Block-Chain

##  System configurations

1. Operating system: Ubuntu 18.04
2. Blockchain Platform: Hyperledger-Composer and Hyperledger Fabric v1.1
3. Frontend: Django Framework (Python)

## System Setup Required

### Hyperledger
Please find the major files containing logic, model and permissions in the blockchain folder stored as script.js, model.cto and permissions.acl. All the tools that needs to be installed can be done by following the steps on the following link: https://hyperledger.github.io/composer/v0.19/installing/installing-index

### Django
To setup the django, all the instructions can be found on the URL: https://docs.djangoproject.com/en/2.2/intro/install/

## Steps to Deploy the application

### Blockchain with REST Api
1. Setup hyperledger as per this link: https://hyperledger.github.io/composer/latest/installing/development-tools.html . Change the relevant logic.js, model.cto and permissions.acl with the respective files in blockchain folder.
2. Then further setup hyperledger composer as per this link: https://hyperledger.github.io/composer/latest/tutorials/developer-tutorial.html . Follow it upto step 4. We will follow different instructions for REST api.
3. Enable authentication as per https://hyperledger.github.io/composer/latest/integrating/enabling-rest-authentication.html . We chose github as passport strategy and setup the relevant Client Id and Secret to allow OAuth authentication. Also note that "Homepage URL" and "Authorization callback URL" were setup with IP of our PC to enable auth setup on IIT Kanpur intranet.
4. Multi-User setup as per this link: https://hyperledger.github.io/composer/latest/integrating/enabling-multiuser.html
5. Run the following to start the REST server
```bash
composer-rest-server -c admin@appraisals -n never -a true -m true -u true -w true
```
6. Now, go to https://\<ip\>:3000/auth/github to start the authentication. You will then be redirected to https://\<ip\>:3000/explorer where you can use the template GET and POST calls to transact with the blockchain. You would also need to add your business card to the wallet by using POST 'import' request. This card needs to be issued by the admin on your blockchain network. Note that although all possible transactions including asset creation are listed, you would only be able to run the transactions which are authorized as per your identity (business card). This is as per the restrictions defined ACL.


### Frontend 
To run the django based frontend:
```bash
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```
Note that while you would see all the forms (like a mock up for deployment scenario), this would actually work only after successfully setting up the blockchain and setting up the REST based authentication.
