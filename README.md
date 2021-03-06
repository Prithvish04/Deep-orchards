# Deep-orchards
Reproducibility Project for Deep Learning Course - TU Delft


**Instructions
**

- Download the dataset from https://data.acfr.usyd.edu.au/ag/treecrops/2016-multifruit/. Extract the almonds folder from the complete dataset

- Copy and past the almonds folder to the /(Deep-orchards) directory.

- Run the csv_convert_xml.py  png_convert_jpg.py scripts to convert the dataset annotation from csv format to xml format and png images to jpg images.

- Download the pretrained imagenet weights from  https://drive.google.com/file/d/1IfSFSizsqbIYWYYbJls_J7478B6gpgIa/view & https://drive.google.com/file/d/1ioQS500sjJsdOlZ2LI-_FxwjxPMIcC5_/view?usp=sharing and /Deep-orchards/data/imagenet_weights

- Run the following scripts to train and test

./experiments/scripts/train_faster_rcnn.sh 0 pascal_voc vgg16/resnet <the test is included in train script just after the model is trained>

- For plotting the results use the plot_results.py file in our_tools folder

- If you want to visualize the loss curve we can use the following method as specified in the original code
tensorboard --logdir=tensorboard/vgg16/voc_2007_trainval/ --port=7001 &


Faster RCNN Code Credits:
https://github.com/ruotianluo/pytorch-faster-rcnn

Dataset collection credits:
https://data.acfr.usyd.edu.au/ag/treecrops/2016-multifruit/

Paper Credits:
https://arxiv.org/abs/1610.03677

blog post for more details:
https://prithvish-n13.medium.com/reproducibility-project-for-beginners-deep-orchards-integrating-the-deep-fruit-data-with-faster-a1189a85d585
