# Project1- Date Modelling with Postgres

## 1. Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

The purpose of this project is to demonstrate the skills of setting up database via SQL and connect the pipeline to the database in Python. 
In term of startup, the engineer needs to set up databases, by breaking it down into several tables in order to keep the data precisely for the analysis by the Data Scientist or Data analysis, which could reduce their workloads significantly for example to implement fast aggregations and simplify queries, therefore, Star schema has been used in order to achieve this goal. 

By connecting Sparkify could significantly process of music data much faster which could save up so much time, it connects all the JSON files of the music information under the Log_data and Song_data, turning them into dataframe, inserting the data under the according database during the startup process in SQL, subsequently create all the process via the ETL python code, which could ensure all the data are ‘inserted’ into the table correctly. 

Simple analysis could be completed though simple SQL syntax including ‘Aggregate sum, groupby.’ Or more complex case, the data could be extracted and build a classification model in Machine learning. As I mentioned above, using python and sparkify could provide a much faster analysis which contain the elements of ‘Big Data’, this is the most important purpose of using Sparkify and python under this Data Modelling project. 

## 2. State and justify your database schema design and ETL pipeline.

**Song Dataset**

The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

```{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}```

**Log Dataset** 

The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.
The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

```log_data/2018/11/2018-11-12-events.json, log_data/2018/11/2018-11-13-events.json```



**Schema and database**

In order to import those data into a new database, star Schema and an initial database will be established. 
Tables are created by the ’create table’ syntax in SQL, 1 fact table, 4 dimensional table:

**Songplays** 

(from log data which is related to the song_plays, by selecting records of the song’s page under ‘NextSong’)

* Songplay_id serial primary key
* Start_time timestamp 
* User_id varchar
* Level varchar 
* Song_id varchar
* Artist_id varchar
* Session_id int
* Location
* User_agent varchar
* Users(information of the users in sparkify) 
* User_id int primary key
* First_name varchar
* Last_name varchar
* Gender varchar
* Level varchar
* Songs (songs’ information in the database)
* Song_id int primary key,
* First_name varchar
* Last_varchar
* Gender varchar
* Level varchar

**Artists** 

(artists’ information in the database)

* Artist_id varchar primary key
* Artist_name varchar
* Artist_location varchar
* artist_latitude float, 
* artist_longitude float

**Times** 
(the timestamp of the song records, broken downs under different date and times units)

* start_time timestamp primary key
* hour int not null, 
* day int not null, 
* week int not null, 
* month int not null, 
* year int not null, 
* weekday int not null
## 3. ETL

**Song and artists tables**

* Insert Records under the SQL Was built to connect connected the json data into the tables. 

In order to implement all the schema and insert syntax as above, the use of ETL process via Etl.ipynb and etl.py will connect the sql_queries.py together with sparkify database which could run the pipeline to deliver data to the database effectively. 

Extracting all the files from JSON files by using get_files function, pd.read_json and setting up filepath, convert the data into dataframe.

Inserting the data into the created table row by row by using:  

```cur.execute(song_table_insert, song_data)```  ```replaced by (artist_table_insert, artist_data) conn.commit()```


**Time and user tables** 

using similar method as the song and artist tables to load the data from json files, 
however, a ts column was selected which will convert the timestamps data from miliseconds by to.datetime. it breaks the timestamp into hour,day, week, month, year, weekday.

**Song play table** 

The songs and artists tables are joined together in order to create this fact table. 
All the information provided by the instruction was followed to select all the relevant data. Data are all inserted row by row into the table.









## 4. File Structure and steps

1.	test.ipynb displays the first few rows of each table to let you check your database.
2.	create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
3.	etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4.	etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
5.	sql_queries.py contains all your sql queries, and is imported into the last three files above.
6.	README.md provides discussion on your project.

## 5. Below are steps you can follow to complete the project

**Create Tables**

1.	Write CREATE statements in sql_queries.py to create each table.
2.	Write DROP statements in sql_queries.py to drop each table if it exists.
3.	Run create_tables.py to create your database and tables.
4.	Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.

**Build ETL Processes**

Follow instructions in the etl.ipynb notebook to develop ETL processes for each table. At the end of each table section, or at the end of the notebook, run test.ipynb to confirm that records were successfully inserted into each table. Remember to rerun create_tables.py to reset your tables before each time you run this notebook.
Build ETL Pipeline
Use what you've completed in etl.ipynb to complete etl.py, where you'll process the entire datasets. Remember to run create_tables.py before running etl.py to reset your tables. Run test.ipynb to confirm your records were successfully inserted into each table.

**Runing the Python Scripts**

To create the database and table structure, run the following command:

```!python create_tables.py
To parse the log files, run the following command:
!python etl.py```
