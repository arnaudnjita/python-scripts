# Deployment Script with Environment Selection:

# The idea is for you to develop a Python script that allows users to select the deployment environment (e.g., development, staging, or production) and performs different actions based on their choice. 

# Use conditionals to check the selected environment and execute specific deployment tasks accordingly. 

# This exercise will allow you to practice conditionals, function calls that we studied in the last lecture and code organization to automate the deployment process based on user inputs.

# Step 1 
    # Create a function to deploy to development environment
    # Create a function to deploy to staging environment
    # Create a function to deploy to production environment  
# Step 2 
    # Create a function to deploy the environment based on user input
# Step 3
    # Prompt user to choose the deployment environment 

# function to deploy to development environment   
def deploy_to_development():
    print("Deploying to development environment...")

# function to deploy to staging environment  
def deploy_to_staging():
    print("Deploying to staging environment...")

# function to deploy to production environment    
def deploy_to_production():
    print("Deploying to production environment...")

# function to deploy the user selected environment      
def deploy_environment(environment):    
    if environment == 1:
        deploy_to_development()
    elif environment == 2:
        deploy_to_staging()
    elif environment == 3:
        deploy_to_production()
    else:
        print('Invalid environment selected, please try again')
        prompt_user()
 
# function to prompt the user to select a deployment environment        
def prompt_user():
    print("Select the environment to deploy to")
    print("1: Development Environment")
    print("2: Staging Environment")
    print("3: Production Environment")
    user_environment = int(input("Enter either 1, 2 or 3 for the environment to deploy to: "))
    print()
    deploy_environment(user_environment)

prompt_user()
    