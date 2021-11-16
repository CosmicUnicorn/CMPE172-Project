<a href="tutormanager.us-east-1.elasticbeanstalk.com" style="align: right; height: 64px;">
    ![Book Icon](app/static/BookIcon_128x128.png)
</a>
<a href="https://www.sjsu.edu/" style="align: right; height: 64px;"> 
![SJSU Spartan](app/static/SJSU_Spartan_128x128.png) </a>

# Tutor Manager 

## Table of Contents
- [About](#about)
    - [Authors](#authors)
    - [Introduction](#introduction)
    - [Architecture](#architecture)

## About
### Authors
- University Name - [SJSU](https://www.sjsu.edu/)
- Course: Enterprise Software - CMPE172/Fall 2020
- Team Members
    - [James Taylor](https://github.com/CosmicUnicorn)
    - [Raymond Chin](https://github.com/RC-OTOLI)

### Introduction
[Tutor Manager](tutormanager.us-east-1.elasticbeanstalk.com) is a scalable solution for recording, analyzing, and manipulating data about employment and student records across several establishments. It takes minutes to set up, and seconds to customize for your own useage. 

View statistics about enrolled students such as their assignment history and scores.
Track all employees and their roles within each location.
Add new administrators as needed to oversee the database.

This solution takes advantage of three-tier architecture to maintain scalability and relative independence of each tier. The data tier in particular is employs data federation between student and administration data, shared schemas for simpler batch querying, and read replicas.
### Architecture
| **Tier**     |                       |
| :----------: | :-------------------: |
| Presentation | HTML, CSS, JavaScript |
| Business     | Python, [Flask](https://flask.palletsprojects.com/en/2.0.x/) |
| Data         | MySQL on [Amazon RDS](https://aws.amazon.com/rds/mysql/) |



<!-- Include demo video.mp4 here -->