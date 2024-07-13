# Final Task

Your final tasks will be based on the ONNX model. 
Here we have attached 10 images in task/images folder and one `yolo.onnx` model.

* The yolo.onnx model is downloaded from [here](https://github.com/onnx/models/tree/main/validated/vision/object_detection_segmentation/tiny-yolov2)
* Open this yolo.onnx in [Netron](https://netron.app/) and see its internal structure(this is the power of onnx)
* You can refer to [this article](https://machinethink.net/blog/object-detection-with-yolo/) to know how is yolo.onnx model is behaving.

### Task
1. Load the `yolo.onnx` model in ONNX Runtime and give it a rough input to ensure it produces the expected output shape of `(13, 13, 125)`.
2. The `yolo.onnx` model is designed to take an input of size `(416x416x3)`.
3. The `task/images` folder contains 10 images, each reshaped to the size `(416x416x3)`, so you don't need to make changes to the image dimensions.
4. **Function Requirements**:
	- Takes an image as a NumPy array.
	- Passes the image through the loaded ONNX model.
	- Reads the output of the model.
	- Based on the output, plots the bounding boxes on the image using OpenCV.
	- Returns a list of objects present in the image.

Completing this task will primarily require knowledge from sections 1 and 2. Other sections are included to give you a broader view of other computer vision domains, and we may ask questions from these sections during the final recruitment interview process.

#Submission link
[click here](https://docs.google.com/forms/d/e/1FAIpQLSezOpvXZbGRDpY-LNUqbmz4ECWT4ygr0W7Qo16kQ4gy47gtdw/viewform?usp=sf_link)
