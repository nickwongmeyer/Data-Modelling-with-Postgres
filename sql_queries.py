# DROP TABLES

songplay_table_drop = " drop table if exists songplays "
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = (""" create table if not exists songplays (songplay_id serial primary key, start_time timestamp not null , user_id varchar not null, level varchar, song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar);""")

user_table_create = (""" create table if not exists users (user_id int primary key, first_name varchar, last_name varchar, gender varchar, level varchar);""")

song_table_create = (""" create table if not exists songs (song_id varchar primary key, title varchar, artist_id varchar, year int, duration float);""")

artist_table_create = (""" create table if not exists artists (artist_id varchar primary key,artist_name varchar, artist_location varchar, artist_latitude float, artist_longitude float);""")

time_table_create = (""" create table if not exists time (start_time timestamp primary key, hour int not null, day int not null, week int not null, month int not null, year int not null, weekday int not null);""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays (songplay_id, start_time , user_id, level, song_id, artist_id, session_id, location, user_agent) values(%s,%s, %s, %s, %s, %s,%s, %s, %s) on conflict do nothing""")

user_table_insert = ("""insert into users(user_id, first_name, last_name, gender, level) values(%s, %s, %s, %s, %s) on conflict (user_id) do update set level = excluded.level;""")

song_table_insert = ("""insert into songs(song_id, title, artist_id, year, duration) values(%s, %s, %s, %s, %s) on conflict do nothing""")

artist_table_insert = ("""insert into artists(artist_id,artist_name, artist_location, artist_latitude, artist_longitude) values(%s, %s, %s, %s, %s) on conflict do nothing""")


time_table_insert = ("""insert into time (start_time, hour, day, week, month, year, weekday) values(%s, %s, %s, %s, %s, %s, %s) on conflict do nothing;""")

# FIND SONGS

song_select = ("""select songs.song_id, artists.artist_id from songs join artists on songs.artist_id=artists.artist_id where songs.title=(%s) and artists.artist_name=(%s) and songs.duration=(%s)""")

#sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.
# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]