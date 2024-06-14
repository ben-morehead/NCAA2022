'''
TensorFlow Project to Predict the NCAA Tournament Results
'''
from DataPipeline import DataPipeline

if __name__ == '__main__':
    print('--- NCAA 2022 TensorFlow Project ---')
    
    run_program = True
    while run_program:
        input_val = input("Enter a Command: ")
        if input_val == "start":
            pass
        elif input_val == "exit" or input_val == "e":
            run_program = False
        elif input_val == "data" or input_val == "d":
            data_pipeline = DataPipeline()
            data_pipeline.test()


        else:
            print(f"[Invalid Command: '{input_val}']")
    
    print("Exiting NCAA 2022 TensorFlow Project")