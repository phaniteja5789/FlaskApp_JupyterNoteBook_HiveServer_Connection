# FlaskApp_JupyterNoteBook_HiveServer_Connection
This repository is an application developed in Flask as BackEnd for connecting the Jupyter Notebook to the Hive Server and execute the queries and displays the results back in the UI

The Front of the Flask Application is designed using HTML & CSS.

The Welcome screen of the application is as below

<img width="935" alt="image" src="https://user-images.githubusercontent.com/36558484/236906192-e0708729-fc1e-47fc-8723-a7c22275af2b.png">

Basically the window is splitted in 2 halves. One is for the user to Enter the Query and second is to display the results based on the query.

Execution Flow:

  When User enters the query, and hit on execute the index function will get executed which internally connects the Hive Server in cloudera VM using DSN connection with the help of PyODBC package.
  
  If Query is a select query it will return the results back to the UI where it will be shown as a Table
  
  If Query is a Insert,Delete,Update etc then it will update in the table and displays in a Alert Message to the user to get notified that the result is success.
  
  
ODBC Connection to the Hive Server is as below
<img width="304" alt="image" src="https://user-images.githubusercontent.com/36558484/236907672-257e1369-a018-41af-8233-e22317ea4884.png">


Select Query Example output as below:
Query - select `date`,`time` from airquality limit 2
Output is as below - 

<img width="466" alt="image" src="https://user-images.githubusercontent.com/36558484/236907974-e6564ea6-69b6-48f8-af90-f91be2550e2f.png">

Similarly user can enter multiple queries at a single time itself

Queries - select `date`,`time` from airquality limit 3
        
          select `date`,`time` from airquality limit 4
          
output - 

<img width="466" alt="image" src="https://user-images.githubusercontent.com/36558484/236908314-d8596805-658b-480f-8b0a-05d2a80c59c0.png">

In case of any error message, the alert message will be shown as below

<img width="227" alt="image" src="https://user-images.githubusercontent.com/36558484/236908642-dbff98d5-246d-4559-919d-13814a76ffe0.png">

This is the way the application has been developed in order to achieve the connection between the Hive Server and the Python.

          
