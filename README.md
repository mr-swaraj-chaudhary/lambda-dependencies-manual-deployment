# Manual deployment of lambda with dependencies
- Develop lambda.py
- Pull dependencies in dependencies folder: 
  ```
  python3 -m pip install requests -t dependencies
  ```
  
- Create a zip of dependencies: 
  ```
  cd dependencies
  zip -r ../deployment-package.zip .
  cd ..
  ```
  
- Add lambda in deployment package: 
  ```
  zip -g deployment-package.zip lambda.py
  ```
  
- Create a lambda on console and set it's runtime to ```python3.11```
- Update handler to ```lambda.lambda_handler``` in runtime settings on console

## Technologies
- Python
- Windows Subsystem Linux (**WSL**)