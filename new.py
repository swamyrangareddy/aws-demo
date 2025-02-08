import boto3
import pandas as pd
import streamlit as st
from io import StringIO

# AWS Credentials (use IAM roles for security)
s3_client = boto3.client("s3")
bucket_name = "my-s3demo"
file_key = "Heart_Attack_Analysis_Data.csv"

obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
df = pd.read_csv(StringIO(obj["Body"].read().decode("utf-8")))

# Display DataFrame and Graphs

with st.expander("Dataframe"):
    st.dataframe(df)
# this are the columns names Age	Sex	CP_Type	BloodPressure	Cholestrol	BloodSugar	ECG	MaxHeartRate	ExerciseAngia	FamilyHistory	Target

total1 , total2, total3 = st.columns(3)

with total1:
    st.metric(label="Max Heart Rate", value=f'{df["MaxHeartRate"].max()}')


with total2:
    st.metric(label="Min Heart Rate", value=f'{df["MaxHeartRate"].min()}')

with total3:
    st.metric(label="Mean Heart Rate", value=f'{df["MaxHeartRate"].mean()}')

st.bar_chart(df["Age"])
st.bar_chart(df["MaxHeartRate"])

total1 , total2 = st.columns(2)

with total1:
    st.bar_chart(df["maxHeartRate"])

with total2:
    st.bar_chart(df["familyHistory"])
