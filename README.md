# Webgazer-Analysis

## src folder

* contains the web application with WebGazer implemented on it

## analysis foldermysqlBack2.sql

* contains the post analysis done on each user's eye gaze

## sampleSearchResultPage folder

* contains files of the sample search result page

## Documentation
### Backend
* The server runs on a single-instance AWS Elastic Beanstalk environment called `Webgazeranalysisbackend-env` 
* The environment is under the application named "Webgazer-Analysis-Backend"
* The platform of the environment on which the server runs is Node.js 16 running on a 64 bit Amazon Linux
* The environment is connected to a MySQL AWS RDS instance identified as "aa1bk9bp1u7gv96"
* The [config.js file](src/server/src/config/config.js) is configured to connect with the RDS instance
* The schema of the database is from the file named "mysqlBack2.sql" which can be found in the "src" folder of this repository
* The server can be accessed through the custom domain: [https://server.webgazerbackend.link](https://server.webgazerbackend.link)
* The domain "webgazerbackend.link" was acquired through AWS Route 53
* The domain "server.webgazerbackend.link" was set up to redirect traffic to the Elastic Beanstalk server environment using Route 53
* The deployed Elastic Beanstalk environment consists of the server files in this repository, which includes the ".ebextensions" and the ".platform" folders that are essential for having the server run over https on the custom domain
* The Elastic Beanstalk environment also has the necessary environment variables such as "DOMAIN_LINK" and "PORT" configured to ensure the server runs over https on the custom domain

### Frontend
* The [app.js file](src/client/src/services/Api.js) is configured to have the frontend use the url https://server.webgazerbackend.link for http requests
* The frontend is deployed on AWS Amplify
* The frontend can be found using the following link: https://main.d3dy3dkik9kfs2.amplifyapp.com/
* The deployed version is based on an AWS automated build from a [repository](https://github.com/airpiazza/Webgazer-Analysis-Temporary) that has the same contents as the [client file](src/client)

## Summary
Webgazer Analysis is a research project that aims to understand how users behave when interacting with multilingual search results. The app is now deployed on the cloud using AWS services. Elastic Beanstalk is used for the server. RDS is used for the database. Route 53 is used for the server domain. Amplify is used to deploy the frontend. The deployed project can be found [here](https://main.d3dy3dkik9kfs2.amplifyapp.com/).