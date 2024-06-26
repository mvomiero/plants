![Project Cover](https://github.com/mvomiero/plants/blob/main/assets/cover.jpeg)
# Plants project 🌴

## Next milestone:
web app with interactive graphs and dashboard about the climatic properties of different occurencies of a plant species

## Next steps:
* decide data organization: sql or bucket?
* set Apache Airflow to schedule the workflow to retrieve the climatic data for all the observations to the API (since it is limited to 500 request per day)
* develop a GUI and a web service to create a sort of web application that allows to visualize the collected data. Possibilities could be:
    * Plotly Dash (Python) - free service
    * Tableau online or server
    * Amazon quickSight
    * Power BI



## Open topics:
* sql database ond aws rds instance or aws bucket? what is the best data organization
* data pipelines
* climatic data saved in json in the database or better to parse it or extract the fields?
* reference in the climatic table to plant observation database?


## Journal

* __1.04-13.04.24__  
Developed on aws a ec2 compunting instance running ubuntu connected to a postgresql database hosted on a aws rds instance. Managed to connect to the database trough cli from my local machine (database is not public, hosted in a private subnet of the ex2 instance)

* __14.01.24__  
__Decision: a new table with the parsed climaic data will be linked to every instance of the observation table. That is to be able to better analyze the data.__  
Finally managed to create a docker-compose with two containers for the db and pg admin web interface to have a GUI to access the database. Created the corresponding guide and adapted the Makefiles for semplicity of operations (for example starting the containers).

* __06.01.24__  
Retrieved multiple instances and plotted on the graph the temperature for the different months. Decided that I wanted to store the climatic data in a table linked to the database of observations. Decided then that I want to move the database in a container for semplicity and to organize the retriving of climatic information with a cron job on a server in the future. Tried to containerize but didn't manage.

* __02.12.23__  
added a function for a scatter plot of with the observation temperature value for one month (for example may, about 15 observations)
* __25/26.11.23 - project structure and table in database for climatic data__  
structure with source code in src/, main.py as entrypoint, config.py for keys, setting the venv, Makefile, structure of the readme, setting a table in the database for the observations to store the climatic data (responses saved as Json), added a makefile. 
* __11.11.23 - started the project__   
bla bla

## Miscellaneous
* [Misc.](https://github.com/mvomiero/plants/blob/main/Guides/Miscellaneous.md)


## Data and APIs
* [PlantNet Open Data](https://plantnet.org/open-data/)
* [PlantNet Observations Dataset](https://www.gbif.org/dataset/7a3679ef-5582-4aaa-81f0-8c2545cafc81#description)  *GBIF registation section contains information about how to use the API*
* [OpenWeather Statistic Data](https://openweathermap.org/api/statistics-api#:~:text=Statistical%20Weather%20Data%20API%20allows,or%20for%20the%20entire%20year.)

## PostgreSQL Database
* [PosgreSQL](https://github.com/mvomiero/plants/blob/main/Guides/PostgreSQL.md)

## setting an aws RDS instances and connect to it
* [PosgreSQL](https://github.com/mvomiero/plants/blob/main/Guides/aws_rds.md)

## 11.11.23 Request to ChatGPT
so I have an ongoing project I want to develop. The project is the following: I want to develop a platform that combines plant data with climatic and geografic data. The process should be the following: I take the data of plantnet, wich is a plant recognition app, and epecially I use their data to see where are located  the obseravations o a specific plant in the world (coordinates). So for example I do that for a single plant. Then, thanks to an API i want to get the climatic data of the different locations of the plant. Then, with some machine learning, I want to know what are the climatic conditions where this plant successfully grows. 

Now, I need some help with the architecture of the all. I want to develop my project in python and first start with just a plant. I can either download the dataset from plantnet (it is a .csv file, about 1700000 occurrencies in total, about 10 - 15 fields per row, or make an API request to the database).
Once i collect the data and for example I get all the rows corresponding to the observations of a same plant species, then I can ask to the climatic API data for every single location...so I have to store this data somewhere. at the end I perform machine learning (I think someting like linear regression) and I should be able to get a climatic description where this plant thrive. So once I have this data I can start building my own database, and then proceed (but not now in the future) to apply that to all the plant species observated in the plantnet dataset. 

Now I would need some help in the architecture, how to set the database and the pipelines: should I use .csv files or is there something more efficient? how do i manage the pipeline of data to python, and where should I temporary store for example all the climatic data that I need for the machine learning calculations, how do I build my on database and so on. And should I maybe work with containers or not so important at the beginning?

I'm of course just starting so I would start easy and then implement.

Thank you

## 11.11.23 - The response:
1. Data Collection:
PlantNet Data:
You have two options for obtaining PlantNet data:

Download Dataset: If the dataset is available for download, you can start by downloading it and working with it locally.

API Requests: If there's an API available, you can make requests directly from your Python application. This approach allows you to fetch real-time data and potentially keep your local data more up-to-date.

2. Data Storage:
Initial Plant Data:
For storing the plant data (from PlantNet), you can use a database. Considering the structured nature of the data, a relational database like PostgreSQL or SQLite could be a good choice.

Climatic Data:
You can also use a database for storing climatic data. However, since climatic data is likely to be time-series data, a time-series database like InfluxDB might be suitable.

3. Data Processing Pipeline:
ETL (Extract, Transform, Load):
Design an ETL process to clean and transform the raw data before storing it in the database. This can be done using a tool like Apache Airflow or a simple custom Python script.

4. Machine Learning:
Model Training and Prediction:
Use Python libraries such as scikit-learn or TensorFlow for machine learning. Train your model on the climatic and geographic data, and make predictions on where the plant is likely to thrive.

Model Storage:
Store the trained model in a format that allows easy retrieval within your application. Pickle or joblib can be used for this purpose.

5. Additional Considerations:
Temporary Storage:
For temporary storage during data processing, you might use a local cache or a temporary table in your database.

Containerization:
While not crucial initially, containerization (using tools like Docker) can help with reproducibility and deployment consistency as your project grows.

Scalability:
Consider the scalability of your architecture. If you plan to scale up, tools like Apache Kafka for data streaming or cloud services like AWS S3 and Google Cloud Storage can be considered.

6. Future Steps:
Expanding to All Plant Species:
As you mentioned, once you have a prototype working for one plant, you can expand it to handle all plant species in the PlantNet dataset.

Frontend and User Interface:
Consider developing a user interface for interacting with your platform, allowing users to explore and visualize the data.

Conclusion:
Start small, build iteratively, and refine your architecture as needed. Utilize Python's rich ecosystem of libraries and tools for each step of the process. Remember to document your work as you progress. Good luck with your project!
