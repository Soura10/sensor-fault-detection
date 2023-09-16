from datetime import datetime
import os
from sensor.constant.training_pipeline import PIPELINE_NAME,ARTIFACT_DIR
class TraingPipelineConfig:

    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name : str = PIPELINE_NAME
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR,timestamp)
        self.timestamp : str = timestamp
        
