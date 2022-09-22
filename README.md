# lambda-layer

**Lambda layers** 

A Lambda layer is a .zip file archive that can contain additional code or other content. A layer can contain libraries, a custom runtime, data, or configuration files.

Lambda layers provide a convenient way to package libraries and other dependencies that you can use with your Lambda functions. Using layers reduces the size of uploaded deployment archives and makes it faster to deploy your code

**Steps to create Pipeline using CFT**

Note: By default am doing thisin us-east-1

Prerequisites:  
  Before proceeding ahead you have to clone and push this code to your codecommit repo. 
  In that code there is a requirement.txt file in which you can specify which layer you need.
  Note the branch of code repo.
  ![image](https://user-images.githubusercontent.com/23731547/191704833-3780f41d-1019-4ff9-bb8e-dedfb639e883.png)

  
Steps:

In CloudFormation console upload the 
    

Sign in to the AWS Management Console and open the AWS CloudFormation console at https://console.aws.amazon.com/cloudformation.
If this is a new CloudFormation account, choose Create New Stack. Otherwise, choose Create Stack.

 
In the Template section, select Upload a template file and upload LambdaLayer-CloudFormation-CICD.yml Click next.
Enter the stack name, BranchName(Where the code is present), LayerName, RepoName(Codecommit repo name) and click next and next.

![image](https://user-images.githubusercontent.com/23731547/191704688-b5f0c6d1-246d-4967-80ba-c30c68d0cf97.png)


4.  Check the box and click on Create Stack.

After stack execution successfully you can see that your pipeline is running successfully and executed. 
  ![image](https://user-images.githubusercontent.com/23731547/191704548-02e675fb-854e-4b5c-bafa-6ab6fee08b1e.png)

 
You can check created lambda layers here https://us-east-1.console.aws.amazon.com/lambda/home?region=us-east-1#/layers
 

 
 
The same process you can follow if you need another layer with different packages or same layer with additional packages 


if you need more understanding regarding cloudformatin and CICD 
CloudFormation Getting Started : https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.Walkthrough.html
CICD Getting Started : https://docs.aws.amazon.com/codepipeline/latest/userguide/getting-started-codepipeline.html





