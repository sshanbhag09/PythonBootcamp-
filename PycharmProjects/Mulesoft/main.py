import psycopg2
hostname='localhost'
database='MovieDB'
username ='postgres'
pwd='RGSS0103'
port_id= 5432
conn=None
curr=None
try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id

    )
    cur= conn.cursor()
    cur.execute('DROP TABLE  if exists Movie')
    create_script='''CREATE TABLE  Movie(
                        id serial PRIMARY KEY NOT NULL,
                        name varchar(60),
                        lead_Actor varchar(60),
                        lead_Actress varchar(60),
                        release_year varchar(4),
                        director varchar(60)
                    )'''
    cur.execute(create_script)
    insert_script='INSERT INTO Movie(name,lead_Actor,lead_Actress,release_year,director) values(%s,%s,%s,%s,%s)'
    insert_values=[('Dont Look Up','Leonardo DiCaprio','Merryl Steep','2022','Adam Mckay')
        ,('Titanic','Leonardo Dicaprio','Kate Winslet','1997','James Cameroon')
        ,('Anatomy of a Murder','James Stewart','Lee Remick','1959','Otto Primenger')
        ,('The Hunger Games: Catching Fire','Josh Hutcherson','Jennifer Lawrence','2013','Francis Lawrence')
        ,('The Maze Runner','Dylan OBrien','Kaya Scodelario','2014','Wes Ball')
        ,('Pushpa 2','Allu Arjun','Rashmika Mandanna','2022','Sukumar' )]
    for record in insert_values:
        cur.execute(insert_script, record)

    cur.execute('SELECT  * FROM movie')
    for record in cur.fetchall():
        print(record)
    cur.execute("SELECT name,lead_Actor from movie where lead_Actor in ('Josh Hutcherson') ")
    print(cur.fetchall())
    conn.commit()
except Exception as Error:
    print(Error)
finally:
    if cur is not None:
        cur.close()
    conn.close()
