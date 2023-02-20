from sensor.pipeline.batch_prediction import start_batch_prediction
from sensor.pipeline.training_pipeline import start_training_pipeline
from sensor.exception import SensorException
import sys

file_path = "/config/workspace/aps_failure_training_set1.csv"

if __name__=="__main__":
     try:
          #start_batch_prediction(input_file_path=file_path)
          start_training_pipeline()
     except Exception as e:
          raise SensorException(e, sys)