<a href="https://tutormanager.us-east-1.elasticbeanstalk.com">
    <image src="app/static/BookIcon_128x128.png" alt="Book Logo" align="right" height="64" />
</a>
<a href="https://www.sjsu.edu/"> 
    <image src="app/static/SJSU_Spartan_128x128.png" alt="SJSU Spartan" align="right" height="64" />
</a>

# Tutor Manager 

## Table of Contents
- [About](#about)
    - [Authors](#authors)
    - [Introduction](#introduction)
    - [Architecture](#architecture)
 - [Demo](#demo)
 - [Instructions](#instructions)

## About
### Authors
- University Name - [SJSU](https://www.sjsu.edu/)
- Course: Enterprise Software - CMPE172/Fall 2020
- Team Members
    - [James Taylor](https://github.com/CosmicUnicorn)
    - [Raymond Chin](https://github.com/RC-OTOLI)
    - [Dhananjay Pahuja](https://github.com/dhananjaypahuja)

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

<details><summary>Show architecture diagrams</summary>
    
| |
| :--: |
| ![System Diagram](https://user-images.githubusercontent.com/54559120/142005164-eb7cfe0c-d628-491f-ba47-f0b54b74eb30.png) |
| System Diagram |
| |
| ![Class Diagram](https://user-images.githubusercontent.com/54559120/142005963-6a333b0b-901e-4624-8add-205105b6bb92.png) |
| Class Diagram |
| ![Sequence Diagram (Add worksheet)](https://user-images.githubusercontent.com/54559120/142005447-5983c7a1-7d81-4d84-b0cb-dce2a5a7be9f.png) |
| Sequence Diagram of adding a worksheet |
| |
| ![Student Database](https://user-images.githubusercontent.com/54559120/142006992-b7909982-ed48-4439-88dd-beb6d2e8aa91.png) |
| ![Administration Database](https://user-images.githubusercontent.com/54559120/142006826-56a98c50-c307-4366-9160-3889e4fa22bd.png) |
| Federated database structure |
</details>

## Demo
<!-- Include demo video.mp4 here -->

<details><summary>Show screenshots</summary>
    
![Sign In](https://user-images.githubusercontent.com/54559120/141994220-245b85b6-8fd8-40f5-ae7a-74516e975f51.png)

![Students + AddForm](https://user-images.githubusercontent.com/54559120/141995345-bde9fc77-c2c9-4d17-af92-b77436d1b562.png)

![Assignments](https://user-images.githubusercontent.com/54559120/141996890-3e3cc3bb-1da4-4e49-9b69-1049a717f665.png)

![Edit Assignment](https://user-images.githubusercontent.com/54559120/141996935-f02b9811-3310-48ff-88df-4bd0259729dd.png)

![Employees](https://user-images.githubusercontent.com/54559120/141997437-02b3238f-5906-4470-9fb8-aafd8ae63388.png)

![Worksheets](https://user-images.githubusercontent.com/54559120/141997818-83bbdf2d-88cb-4e7d-b9b3-fc36d7de7c39.png)

![Worksheets + AddForm](https://user-images.githubusercontent.com/54559120/141998422-7e2c634b-2ec9-495d-9f27-30ffea0e11e2.png)
</details>

## Instructions
### Local server
- Get a python 3 or later environment on your machine
- Clone the repo into a directory of your choice
- Build in virtual environment (optional)
    ```bash
    cd <target storage directory>
    py -3 -m venv .venv
    .venv\scripts\activate
    ```
- Install package requirements
    ```bash
    python -m pip install --upgrade pip
    python -m pip install -U flask
    python -m pip install -U flask_login
    python -m pip install -U flask-wtf
    python -m pip install -U pymysql
    ```
- Startup local server
    ```bash
    cd <proj directory path>
    python .\app\run.py
    ```
- Stop server (Ctrl + c in terminal)

### Docker container service
- Create local image in Docker
    ```bash
     docker build github.com/CosmicUnicorn/CMPE172-Project
    ```
- Run image
    - In a new container
        ```bash
        docker run -[detached mode] -[publish flag] [host port]:[container port] --[name] [custom container name] [image name]
        ```
        ```bash
        docker run -d -p 5000:5000 --name CMPE172Container cmpe172project
        ```
    - In already existing container
        ```bash
        docker start [container name]
        ```
        ```bash
        docker start CMPE172Container
        ```
- Stop image
     ```bash
    docker stop [container name]
    ```
    ```bash
    docker stop CMPE172Container
    ```
