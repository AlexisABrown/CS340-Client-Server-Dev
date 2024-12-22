About This Dashboard

This project lets you interact with animal shelter data. This can be used to find animals suitable to train for certain tasks. It takes a database and allows you to see how many animals are available and where the are located.  

Functionality

The primary functions include:
1. Filtering with Data Tables: Displays animal information based on the selected radio button. Current filter options are:
Water Rescue 
Mountain & Wilderness Rescue 
Disaster & Individual Rescue 
Reset(shows all dogs in database) 
2. Mapping: The location of the animal selected on the data table will show in the map. Currently only a marker for the selected animal will show. 
3. Charting: Currently set to a pie chart that shows the distribution of breeds based on the selected filter.
   
Tools

You’ll need the following tools to run and edit this dashboard. Hyperlinks are provided. 

MongoDB: The document database. Chosen for it's ease of use and flexibility. It also has free community options. 
Python 3.9 or newer: The primary programming language for this project. Used to create the CRUD module that interacts with the database. 
Dash/Plotly: Used for creating the web application framework, pie chart, and geolocation map. Helps create a dashboard that is highly visual and easy to interact with.  
Steps

To create the project the data needed to be loaded into MongoDB.
Then a Python CRUD module was created to handle the data. 
This was used to create a rudimentary dashboard. A map was added centered on Austin, Texas. 
Pie chart and filter options were the last to be added. 
Each filter was tested to make sure the correct animals were displayed. 

Project Challenges 

The initial pie chart would throw an error when set to anything but value='reset'. This was resolved by setting the value variable to reset under the radio items options. 
  
When adding the map  it was not appearing in the dashboard, leaving a large blank space. I found that the map section of my code had indention errors. These can happen more in Python than other languages. 






