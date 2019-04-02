# DevOps Evaluation Project

Problem description obtained from https://engineering-application.britecore.com/e/t2e119s3t/testDevOpsDirector after debugging https://engineering-application.britecore.com/quiz/wsmvjefnvwmdkvnen.

Create a vanilla Django project with startproject. Create two views in your web app:

View 1
View 1 is a web form that accepts at least one user input. Upon form submission, route the user input(s) to 100 different lambdas that each transform the input in some way, writing all transformed values back to a persistent datastore.

View 2
View 2 is a search input that queries all data in the persistent datastore and displays the results in a datagrid.

Deployment
Deploy this project in a way that scales to 1 million concurrent users:

Provide configuration for the AWS services you would use.
If any scripts are needed, provide them.
Document how your deployment process works in a way management can read and understand.
Document the detailed steps one must take for deploying the site from scratch.
If subsequent deployments of the site are different from the “from scratch” way of deployment, write up the steps and reasoning.
Put all of this in a GitHub or Gitlab repo.
Documentation is particularly important here. Imagine you are going on a 1-month vacation. The docs must contain exactly what any member of the DevOps team needs to know to deploy the project without contacting you.

Rules
= This isn't a new problem. Reuse of existing work is fine, even encouraged, but you have to cite what you reuse and document your reasons for doing so.

We use Python and Docker a lot at BriteCore. Keep that in mind.
Do not include these AWS services:
Elastic Beanstalk
Bonus points for using these AWS services:
CloudFormation
Bonus points for considering these in your approach and documentation:
12-Factor App pattern
SAFe (Scaled Agile Framework) Release on Demand principle
Guidelines
We're looking for someone who can work independently and is curious and self-motivated. One major goal of this project is to see how you fill in ambiguities creatively. There is no such thing as a perfect project here, just interpretations of the instructions above, so be creative in your approach.

Deliverables
In order to move your application forward, deliverables will include:

A deployed version of your project, on AWS.

A GitHub repo containing your project. Your repo must contain these two items:

A detailed README that explains your approach and deployment method
Your code solution to this test
Adding of these items to your resume's cover letter:

The link to the GitHub repo that lists this project
The link to the deployed version of your project
Uploading of your resume with cover letter in PDF or DOCX format by clicking this link.

Questions
For questions, please use implementation-hires@britecore.com.

Thank you for your time. We are excited to review your project!