import os
import pandas as pd
from src.utils.common import read_config
from src.utils.data_mgmnt import get_data
from src.utils.model import create_model ,save_model
from src.utils.save_plot import save_plot
from src.utils.callbacks import get_callbacks
import argparse


def training(config_path):
    config = read_config(config_path)

    validation_datasize = config["params"]["validation_datasize"]
    (x_train,y_train),(x_valid,y_valid),(x_test,y_test)=get_data(validation_datasize)
    #print(config)
    LOSS_FUNCTION = config["params"]["losss_function"]
    OPTIMIZER=config["params"]["optimizer"]
    METRICS=config["params"]["metrics"]
    NUM_CLASSES=config["params"]["no_classes"]

    # model creation and compilation
    model = create_model(LOSS_FUNCTION,OPTIMIZER,METRICS,NUM_CLASSES)

    # training the model
    EPOCHS = config["params"]["epochs"]
    VALIDATION = (x_valid,y_valid)


    # callbacks
    CALLBACKS_LIST = get_callbacks(config,x_train)

    history = model.fit(x_train,y_train, epochs=EPOCHS, validation_data=VALIDATION,callbacks=CALLBACKS_LIST)
    
    #history = model.fit(x_train,y_train, epochs=EPOCHS, validation_data=VALIDATION)

# save model
    artifacts_dir = config["artifacts"]["artifacts_dir"]
    model_dir = config["artifacts"]["model_dir"]
    model_name = config["artifacts"]["model_name"]

    model_dir_path = os.path.join(artifacts_dir,model_dir)
    os.makedirs(model_dir_path,exist_ok=True)

    save_model(model, model_name, model_dir_path)

# save plot

    plot_dir = config["artifacts"]["plot_dir"]
    plot_name = config["artifacts"]["plot_name"]
    plot_dir_path = os.path.join(artifacts_dir, plot_dir)
    os.makedirs(plot_dir_path, exist_ok=True)

    save_plot(pd.DataFrame(history.history), plot_name, plot_dir_path)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config.yaml")
    parsed_args = args.parse_args()    

    training(config_path=parsed_args.config)