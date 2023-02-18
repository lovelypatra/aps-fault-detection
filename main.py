from sensor.pipeline.batch_prediction import start_batch_prediction

file_path = "/config/workspace/aps_failure_training_set1.csv"

if __name__=="__main__":
     try:
          start_batch_prediction(input_file_path=file_path)
     except Exception as e:
          raise SensorException(e, sys)