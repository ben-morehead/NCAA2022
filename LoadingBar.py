class LoadingBar():
    def __init__(self):
        self.loading_text = ""
    
    def start_loading_bar(self, data_name):
        print(f"Loading {data_name}:")
        self.loading_text=""
        
    def update_loading_bar(self):
        self.loading_text = f"{self.loading_text}=="
        print(f"{self.loading_text}" ,end="\r")

    def end_loading_bar(self):
        print("",end="\r")