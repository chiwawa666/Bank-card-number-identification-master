import backward as bw
import app
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1'
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '2'
os.environ["TF_CPP_MIN_LOG_LEVEL"] = '3'


if __name__ == '__main__':

    train = False
    if train:
        bw.main()

    file_path = 'test_images/1.jpg'
    app.application(file_path)
