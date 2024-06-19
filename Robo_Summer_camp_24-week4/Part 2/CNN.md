# INTRODUCTION TO CONVOLUTIONAL NEURAL NETWORK
After completing part 1, we hope you have got a nice understanding of the fundamental concepts of Deep Learning algorithms such as Neural Network. Now, in part 2, you would be introduced to some Computer Vision algorithms starting from the most fundamental one, **Convolutional Neural Network (CNN)**. 


A CNN/ ConvNet is a Deep Learning Algorithm, which takes images as input and assigns weights/ biases to various objects or features present in the input image, thus, classifying the images efficiently. Though, the advantages of CNN would be clear once you learn more about the architecture and working of the network, but one of the main advantages CNN has over other classification algorithms is that it requires much lower pre-processing.

Like a Neural Network, A CNN also contain input layer,hidden layers and output layer.But in addition to neural network,It also contains following three types of layer which enables it to learn from images.

  - **A Convolution Layer:** Carries out convolution operations on input images to give an output.
  - **An Activation Layer:** It's a non-linear function that is applied to the features in order to do efficient and faster training of data.
  - **A Pooling Layer:** It simplifies the output by applying a non-linear function to downsample the input layers, reducing the number of parameters/ features that the network needs to learn.

We'll discuss these layers briefly for your better understanding of the algorithm.


# Convolution Layer
The convolutional layers is the main feature of a CNN that diffrentiates it from other classification algorithms. Though, a CNN also contains non-convolution layers, its major essence comes from the convolution layers. 

## Kernels 
A Convolution Layer consists of **Kernels** or **Filters** that carry out the convolution operations on input images and give an output. A Kernel is a small matrix representing pixels, consisting of some values on each pixel. These kernel slides over the input image pixels, performing Convolution operations on it. A Convolution is nothing but the matrix dot product of the Kernel with the underlying portion of matrix pixels of the input image.

<p align="center">
  <img src="https://miro.medium.com/max/1838/1*xBkRA7cVyXGHIrtngV3qlg.png" width ="600">
</p>

## Padding
In the  example of convolution we saw that the for an input image of size 5X5, when convoluted with a kernel of size 3X3, the output image obtained is of size 3X3. If, we generalise, this example by doing some math, we can say, if the size of the input image is **n X n**, that of the filter is **f X f**, than the size of the output image obtained is **(n - f + 1) X (n - f + 1)**.


CNNs generally have many hidden or convolution layers, here we face a problem, as the downside of convolution is that the **input image will keep on shrinking in size and we won't be able to do the operation after a couple of layers**.

Another downside to this is that the corner pixels of the input image only contribute to one of the output pixels, whereas the middle pixels have been accessed multiple times by the 3X3 filter and hence used more for the output pixels. Thus, making **a lot of information from the corner elements vanish**.

<br>
<p align="center">
  <img src="Part 2/same_padding_no_strides.gif" width ="300">
</p>
<br>

**Padding** is one simple solution to overcome both these problems. We just add some extra layer of pixels surrounding the input image, a Pad (with pixel value 0). So, in our example, the 5X5 image will become 7X7 after applying a pad of one pixel around the image. This solves the shrinking of image as well as loss of information from corner elements

Two common choices of padding are **Valid and Same convolutions**. Valid Convolution is when we don't pad, i.e. the image is simply convoluted with the kernel to obtain output matrix. Same Convolution is a method of padding, where we add p pads to the output layer, such that its size becomes equal to the input image.
So, the number of pads can be obtained as- **n - f + 1 + 2p = n**, i.e. **p = (f - 1)/2**

## Strides

Till now, whenever we convoluted an input image, to obtain the convolution of the next 9 pixels, we moved the filter by one coloumn or row, making it **One Strided Convolution**, similarly if instead of one we move by two pixel coloumns or rows at a time, the stride becomes two. So, after introducing the concept of stride, we have a new general formula for the dimensions of the output matrix.

<br>
<p align ="center">
  <img src="https://user-images.githubusercontent.com/81189235/177009707-c75b62bc-b444-4468-b852-227178964d14.JPG">
</p>
<br>

Try to think and figure out on your own how this formula is justified. If you don't understand, watch this video to get a better intuition. <a href="https://youtu.be/lxk_nmpqI5M">click here</a> 


## Edge Detectors
Now, that you know what a kernel is and how it operates on the input image, it's time we learn how it's used. In a CNN architecture, the first few convolutional layers are used to detect edges or outlines of the object, a few hidden layers later, they start detecting small features of an object, e.g. eyes, nose, etc, and the ending few layers spam out to detect complete objects. Let's see how we can detect edges in an image.<br>
<br>
<p align="center">
  <img src="https://media5.datahacker.rs/2018/10/multiplication_slicice.png" width ="650">
</p>
<br>
Here, we take an example of a 6 by 6 input image. The image is a greyscale image with the values written in the matrix denoting the intensity of colour on a pixel, 0 being black and 256 being white. We convolve it with a 3 by 3 filter to obtain an output image of size 4 by 4. How do we get the size 4 by 4 you ask ?
The answer is simple, the kernel is placed over the input image (covering pixels [[10 10 10], [10 10 10], [10 10 10]]) and the value obtained goes to the first cell or pixel of the 4 by 4 output matrix. The kernel than strides by one cell covering the next cells of the imediate next column (covering pixels [[10 10 0], [10 10 0], [10 10 0]]. Following this trend, we obtain the entire 4 by 4 matrix. Now, we can clearly see that the vertical edge of the input image is the boundary separating 10s column and 0s column. And after applying the kernel, we obtain the vertical edge, i.e. the pixels with value 30s.


This is how a vertical edge detector works. We can obtain a horizontal edge detector by rotating the VE filter 90&deg; clockwise which has a similar pattern of working and detects the horizontal images of the image.<br> 
Go through this video to get a visual idea of edge detection- <a href="https://youtu.be/XuD4C8vJzEQ">click here</a>

<br>
<h2><b>Convolution Over Volume</b></h2>
Till now we were working over 2D/Greyscale images. Now let's move towards working on RGB images.
<br>
<br>
<p align="center">
  <img src="https://preview.redd.it/c9xola0nwdx51.jpg?auto=webp&s=99e7d18d86724ec4182f2f3d81c4d1be687f46c7" width="300" height="300">
</p>
<br>
Like a greyscale image can be represented by a 2D matrix, similarly, an RGB image, can be represented by a 3D matrix, with 3 channels having the colour intensity of a particular colour for the pixels. Now, a 2D kernel might not be the ideal matrix to convolute over an RGB image, So, we come up with 3D kernels. Taking the only example we've been studying, lets suppose we have an input image of dimension 6X6X3 (RGB), so we will now use a kernel of 3X3X3. Now, instead of summing the 9 parameters, we'll add all of the 27 parameter where the kernel is positioned. This way all the calculations we did till now are still valid. The output image will still be a 2D matrix, of dimension 4X4 (without padding ofcourse). <br>
In computer vision, by convention, the channels of kernel and input image are always same in value. Now, to get multiple channels in our 2D output image, we can just convolute the input image with multiple filters, and all the 2D outputs can be placed one over the other, making the output have depth or channels too, just this time the channels denote the number of filters used and not RGB values.
Go through this video to get a better intuition of this phenomenon. <a href="https://youtu.be/KTB_OFoAQcc">click here</a> 
<br>
<br>
<p align="center">
  <img src="https://miro.medium.com/max/1838/1*Ukb2msCjU3G5eS4a45f-lg.png" width ="600">
</p>
<br>
<br>
<h3>This concludes our journey of how a convolution layer is formed in a CNN. But, the cherry on the top is still left, which we'll cover in the activation layer.</h3>
</details>
<br>

# Activation Layer

You've been already introduced to **biases and activation** functions or non-linear functions in Neural Networks. Well, this is completely different! Just kidding, its the same thing having its implementation on the output layer parameters (cells) obtained after a convolution layer. So, after the input image or layer A[l-1] undergoes convolution with a filter W[l], the bias is added to the 2D output layer. The Bias is a single real number which is added to each of the cells of the 2D output matrix.<br>
Once, the bias is added, the 2D channel passes through an activation function. ReLU, Sigmoid, tanh, etc. are some examples of activation functions. Here, we'll use the ReLU function. If you don't know what a ReLU function is, quickly go through this <a href="https://youtu.be/Ei6274NnDvU">video</a>. So, after all the channels or depth layers of the output image are processed (added biases and non-linearity) these are combined or placed one over the other to form the entire output matrix.<br>
The mathematical representation of this will be the same as that of a hidden layer of Neural Network, where he input parameters are the input features, the filter parameters are the Theta matrix and the after adding a bias parameter and non-linearity function:<br>
  <h3 align="center">Z[l] = W[l] * A[l-1] + b<br>
      A[l] = g( Z[l] )</h3>

# Pooling Layer
<p align="center">
  <img src="https://media1.giphy.com/media/lf4U8MpbPcWTILmb9n/giphy.gif" height="350">
</p>
<br>
<h4 align="center"><b>NO!</b> This is not the pool we are talking about here.<br></h4>
Pooling Layers are the non-convolution layers of a CNN architechture, but are equally important for faster computation and reduction of size of the layers. These layers are added at the ending few layers of the network in order to reduce the number of features for faster computation. They can be of multiple types, but the most commonly used pooling layers are <b>Max Pool</b> and <b>Average Pool</b>. Let's discuss both these pooling methods.
<br>
<br>
<h3>Max Pooling</h3>
<br>
<p align="center">
  <img src="https://developers.google.com/static/machine-learning/practica/image-classification/images/maxpool_animation.gif">
</p>
<br>
<br>
The given GIF is exactly what a Max Pool layer does. In the given example, we've an input matrix of 4X4 dimension. And we apply a kernel of max pool OF 2X2 dimension with stride = 2. In a Max Pool, we put a kernel over the input layer, but instead of convoluting it, we just carry forward the cell with maximum value to the output matrix. The stride of max pool layer is deliberately kept large, so that the number of features can be reduced. Max Pool is the most popular and commonly used pooling method for image classification algorithms.
<br>
<br>
<h3>Average Pool</h3>
<br>
<p align="center">
  <img src="https://miro.medium.com/max/1449/0*9_zro3kc-ccq64LX.JPG" width="400" height = "350">
</p>
<br>
<br>
Average Pooling works in the same way as Max Pooling, it has more stride value compared to normal convolution layers and acts on the input image in shape of 2X2 kernel. The only difference between Average and Max pooling is, as the name suggests, instead of passing the maximum value, Average Pool passes he mean of the 4 parameters under consideration to be the value of the cell of output matrix.
<br>
<br>
We discussed 2D pooling here, go through this short video for a better visualisation of 3D pooling. <a href="https://youtu.be/PuFNG721zM8">click here</a>
<br>
<br>
<h3>Thus, you've learned all the basic elements needed to build a ConvNet. Move on to the next subpart to learn the implementation part.</h3>
<p align = "center">
  <img src="https://i.pinimg.com/originals/47/43/26/4743266e52354dc3bac5e25f23611317.gif">
</p>
