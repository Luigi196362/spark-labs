import streamlit as st
import requests
import pandas  as pd
import json

def post_spark_job(user, repo, job, token, codeurl, dataseturl):
   # Define the API endpoint
   url = 'https://api.github.com/repos/' + user + '/' + repo + '/dispatches'
   # Define the data to be sent in the POST request
   payload = {
     "event_type": job,
     "client_payload": {
        "codeurl": codeurl,
        "dataseturl": dataseturl
      }
   }


def get_spark_results(url_results):
    response = requests.get(url_results)
    st.write(response)

    if  (response.status_code ==  200):
        st.write(response.json())

st.title("Spark & streamlit")

st.header("spark-submit Job")

github_user  =  st.text_input('Github user', value='Luigi196362')
github_repo  =  st.text_input('Github repo', value='spark-labs')
spark_job    =  st.text_input('Spark job', value='spark')
github_token =  st.text_input('Github token', value='token')
code_url     =  st.text_input('Code URL', value='')
dataset_url  =  st.text_input('Dataset URL', value='')

if st.button("POST spark submit"):
   post_spark_job(github_user, github_repo, spark_job, github_token, code_url, dataset_url)



st.header("spark-submit results")

url_results=  st.text_input('URL results', value='https://raw.githubusercontent.com/Luigi196362/spark-labs/main/results/part-00000-2e3dd466-e1d8-4a68-8f0c-b7d29ddd9445-c000.json')

if st.button("GET spark results"):
    get_spark_results(url_results)


