# ipl_scraper
## Steps to run:
> Install Docker Desktop(Splash is required to handle dynamic webpage) ---> https://www.docker.com/products/docker-desktop/ <br /> (Do the initial setup to run docker in the system)
<br />Run:
>> To pull required splash docker image:<br />
>>> docker pull scrapinghub/splash<br />

>> This will start the splash to run in localhost:8051 <br /> 
>>> docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash


>Next, create a python virtualenv and activate the env:
>> python -m venv venv<br />
>> source venv/bin/activate

>Install the required packages using the below command:<br/>
>> pip install -r requirements.txt<br/>

> Then go to the directory ipl_data and run:
>> For creating csv file as output:<br />
>>> scrapy crawl ipldata -O filename.csv<br />

>> For creating json file as output:<br />
>>> scrapy crawl ipldata -O filename.json<br />


Some important links: 
> https://www.zyte.com/blog/handling-javascript-in-scrapy-with-splash/
> https://scrapy.org/