# Alibaba Cloud Billing API examples for ECS cost estimation using Python
## 1. Introduction
This example shows how to use Alibaba Cloud Billing API using python for estimating ECS subscription or PayAsYouGo using csv template.
 
## 2. Use Cases
We will demonstrate 2 use cases.
 
### 2.1 Usecase: ECS Subscription cost estimation based on the csv template.
This is a common use case where in there is a need to estimate Subscription cost (Monthly/Yearly) for large number of ECS based on different combinations (instance family,System Disk,Data Disk, Region, Disk type, duration(monthly, yearly) etc)
### 2.2 Usecase: ECS PayAsYouGo cost estimation based on the csv template.
This is a common use case where in there is a need to estimate PayAsYouGo cost (Monthly/Yearly) for large number of ECS based on different combinations (instance family,System Disk,Data Disk, Region, Disk type, duration(hourly, days) etc)

 
## 3. Prerequisites
 
### 3.1 Setup Environment
Set up python environment on your local machine (mac).

#### 3.1.1 Install Python  
brew install python

#### 3.1.2  Install aliyun-python-sdk-bssopenapi on your local machine.
python -m pip install aliyun-python-sdk-bssopenapi

#### 3.1.3 Install beautifulSoup library for XML parsing.
python -m pip install bs4
  
  
### 3.2. Prepare ECS Cost Estimation CSV Templates
This particular Python Billing programs requires input in a certain format.
  
#### 3.2.1 ECS Subscription Cost Estimation csv Template
Please use this template to pass in as input to python program for ECS subscription cost estimate.
##### Template name : 
ecs_subscription_cost_estimation_template.csv
##### Template Type : 
Input File
##### Template Description :
![](images/ecs_subscription_cost_estimation_template.png)
  
#### 3.2.2 ECS PayAsYouGo Cost Estimation csv Template
Please use this template to pass in as input to python program for ECS PayAsYouGo cost estimate.
##### Template name : 
ecs_payasyougo_cost_estimation_template.csv
##### Template Type : 
Input File
##### Template Description :
![](images/ecs_payasyougo_cost_estimation_template.png)

   
## 4. How to use Python code snippets
### 4.1 How to estimate ECS subscription cost : 
* Make sure you have python environment setup and templates ready as mentioned in Step3.
* Copy ecs_subscription_cost_estimation.py & ecs_subscription_cost_estimation_template.csv to a folder.
* Update the code file with your respective keys (AccessKey ID,Access Secret Key) and save it. 
![](images/keys_code_file.png)
*Execute python ecs_subscription_cost_estimation.py
![](images/ecs_subscription_cost_estimation.png)
* Check the out file ecs_subscription_cost_estimation_output_xxxxxxxxxxxxxx.csv with the cost.
![](images/ecs_subscription_cost_estimation_screen.png)
![](images/ecs_subscription_cost_estimation_output.png)
### 4.2 How to estimate ECS PayAsYouGo cost: 
* Make sure you have python environment setup and templates ready as mentioned in Step3.
* Copy ecs_payasyougo_cost_estimation.py & ecs_payasyougo_cost_estimation_template.csv to a folder.
* Update the code file with your respective keys (AccessKey ID,Access Secret Key) and save it. 
![](images/keys_code_file.png)
* Execute python ecs_payasyougo_cost_estimation.py
![](images/ecs_payasyougo_cost_estimation.png)
* Check the out file ecs_payasyougo_cost_estimation_output_xxxxxxxxxxxxxx.csv
![](images/ecs_payasyougo_cost_estimation_screen.png)
![](images/ecs_payasyougo_cost_estimation_output.png)

    
   
  