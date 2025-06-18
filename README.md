# Orchestrated Sentiment Classification of Social Media Text

This project implements an end-to-end, orchestrated pipeline for sentiment analysis of social media text. It compares two machine learning models, Logistic Regression and a Decision Tree, to classify sentiment into Positive, Negative, or Neutral categories.

The entire workflow is orchestrated using **Dagster**, with data processing in **Python**, storage in **PostgreSQL**, and visualization in **Grafana**.

---

## Abstract

This project presents a sentiment classification pipeline for social media data. The dataset was first labeled using VADER, a rule-based sentiment analyzer. We then compare two machine learning models for classification: Logistic Regression and a Decision Tree, both using TF-IDF vectorization. Data was processed using pandas and DuckDB, then stored in PostgreSQL for long-term storage and accessed via Grafana for visualization. Comparative evaluation shows that while the Logistic Regression model achieved 57.8% accuracy, the **Decision Tree classifier provided a more balanced performance with 60.5% accuracy** and significantly improved handling of minority classes.

---

## Technology Stack

* **Orchestration:** Dagster
* **Backend:** Python 3.10+
* **Data Handling:** pandas, DuckDB
* **Database:** PostgreSQL
* **Visualization:** Grafana
* **ML Libraries:** Scikit-learn, VADER, emoji

---

## Getting Started

Follow these instructions to get the project running on your local machine. The entire environment is containerized using Docker.

### Prerequisites

You must have **Docker** and **Docker Compose** installed on your system.

* [Install Docker Engine](https://docs.docker.com/engine/install/)
* [Install Docker Compose](https://docs.docker.com/compose/install/)

### Running the Project

1.  **Clone the project repository:**
    ```sh
    git clone <your-project-repository-url>
    ```

2.  **Change directory to the root folder of the project:**
    ```sh
    cd <project-folder-name>
    ```

3.  **Build and run the services in detached mode using Docker Compose:**
    ```sh
    docker compose up -d --build
    ```
    This command will build the images for the necessary services (Dagster, PostgreSQL, etc.) and start them in the background.

4.  **Access the Dagster UI and materialize the assets:**
    * Open your web browser and navigate to `http://localhost:3001`.
    * In the Dagster UI, you will see the asset graph for the sentiment analysis pipeline.
    * To run the pipeline, click on **"Materialize all"** to execute all the steps, from data loading and processing to model training and evaluation.
