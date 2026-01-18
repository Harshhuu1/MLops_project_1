
---

# Machine Learning Project - Vehicle Data Processing

## Overview

This project demonstrates a complete machine learning pipeline, from data ingestion to model evaluation, and integrates with MongoDB, AWS, Docker, and CI/CD processes. It focuses on **vehicle data** processing and provides a robust framework for machine learning projects. Below is a detailed setup guide and workflow for running the project successfully.

---

## Project Setup

### 1. **Create Project Template**

* Run the `template.py` file to create the initial project structure.

### 2. **Import Local Packages**

* Modify the `setup.py` and `pyproject.toml` files to import your local packages.
* For more details, refer to `crashcourse.txt` to understand the `setup.py` and `pyproject.toml` setup.

### 3. **Virtual Environment Setup**

* Create and activate a virtual environment:

  ```bash
  conda create -n vehicle python=3.10 -y
  conda activate vehicle
  ```
* Install required modules:

  ```bash
  pip install -r requirements.txt
  ```
* Run `pip list` to confirm that all packages are installed.

---

## MongoDB Setup

### 4. **MongoDB Atlas Setup**

1. Sign up for MongoDB Atlas and create a new project.
2. Set up a cluster by selecting M0 (free tier) and configure it.
3. Create a database user with a username and password.
4. In the **Network Access** section, add your IP address (`0.0.0.0/0`) for access.
5. Copy the connection string for MongoDB and replace the password with your created password.
6. Create a `notebook` folder and a file `mongoDB_demo.ipynb`.
7. Add the dataset to the `notebook` folder and push it to MongoDB.

### 5. **Accessing MongoDB Data**

* Go to MongoDB Atlas > Database > Browse Collection to see the data in key-value format.

---

## Logging, Exception Handling, and Notebooks

### 6. **Logger and Exception Handling**

* Write the logger and exception handler in separate files and test them in `demo.py`.

### 7. **EDA and Feature Engineering**

* Add the **Exploratory Data Analysis (EDA)** and **Feature Engineering** notebooks.

---

## Data Ingestion

### 8. **Setup MongoDB Connection**

* Configure MongoDB connections in `constants.__init__.py` and `configuration.mongo_db_connections.py`.
* Implement the MongoDB connection function to fetch data and transform it to a DataFrame.

### 9. **Data Access**

* In the `data_access` folder, create code to connect to MongoDB, fetch data, and transform it into a DataFrame.
* Update the `entity.config_entity.py` and `entity.artifact_entity.py` files accordingly.

### 10. **Set MongoDB Connection URL**

* On Mac/Windows, set the MongoDB URL environment variable in your terminal or system settings:

  ```bash
  # For Bash
  export MONGODB_URL="mongodb+srv://<username>:<password>..."
  echo $MONGODB_URL
  ```

---

## Data Validation, Transformation & Model Trainer

### 11. **Data Validation**

* Complete the `data_validation` component similar to Data Ingestion, ensuring proper validation using schema configuration (`config.schema.yaml`).

### 12. **Data Transformation**

* Implement the **Data Transformation** component and include the estimator in the `entity` folder.

### 13. **Model Trainer**

* Set up the **Model Trainer** component following a similar approach, including necessary classes in `estimator.py`.

---

## AWS Setup

### 14. **AWS IAM & S3 Setup**

1. Log in to AWS, create a new IAM user (`firstproj`), and attach the `AdministratorAccess` policy.
2. Generate access keys and set them as environment variables:
   `bash
        export AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID"
        export AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY"
        `
3. In the AWS S3 service, create a bucket (`my-model-mlopsproj`) and configure it to allow public access.
4. Implement code in `src.aws_storage` to interact with S3.

### 15. **Model Evaluation & Pusher**

* Implement the **Model Evaluation** and **Model Pusher** components to evaluate and push models to AWS S3.

---

## CI/CD Pipeline Setup

### 16. **Docker and GitHub Integration**

1. Set up the `Dockerfile` and `.dockerignore` files.
2. Create a repository in AWS ECR (`vehicleproj`).
3. Set up an EC2 Ubuntu instance (`vehicledata-machine`), and install Docker on it.
4. Connect GitHub to EC2 as a self-hosted runner for CI/CD automation.

### 17. **GitHub Secrets**

* Add the following secrets to GitHub Actions:

  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * `AWS_DEFAULT_REGION`
  * `ECR_REPO`

### 18. **Trigger CI/CD Pipeline**

* Push changes to GitHub and the CI/CD pipeline will be triggered automatically.

### 19. **Expose EC2 Instance**

* Open port `5000` on the EC2 instance by modifying inbound rules in the security group.
* Access your app via the public IP:

  ```
  http://<public-ip>:5000
  ```

---

## Running the Application

You can also trigger model training via the `/training` route.

---

## Contact

For any questions or suggestions, feel free to reach out via email:
**Email**: [ediyalot@gmail.com](mailto:ediyalot@gmail.com)

---


