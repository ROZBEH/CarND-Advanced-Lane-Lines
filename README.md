## Advanced Lane Finding
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)


Overview
---


In this project, our goal is to write a software pipeline that can identify the lane boundaries in a video. Before delving into finding the boundaries, we first try to calibrate the camera based on chess board images so that we can undistort camera images. After that we will talk about Lane Line finding.


Pipeline
---
*The pipeline along with the corresponding python codes will be described here.*

*Note: I have not included the all video data in my submission, because my github repository has limited space. However, I included the output video file.*

<br>

I. Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.

* A set of chess board images from camera are given. Open cv libraray `cv2.findChessboardCorners` and `cv2.calibrateCamera` are used for this part. which results in `mtx` and `ret` for computing undistorted version of the images.

* Given `mtx` and `ret` matrices, opencv `cv2.undistort` is used for getting the undisrted image. An example of the original and undistorted image is shown down here.

<p align="center"><img src="examples/Distortion_.png" width = "800" alt="Combined Image" /> </p>

</br>


<br>

II. Distortion matrices `mtx` and `ret` will be applied to all images before further processings. The following two images show an example of the original(left) and undistorted(right) image.

<p align="center"><img src="test_images/straight_lines2.jpg" width = "400" alt="Combined Image" />
<img src="output_images/straight_lines2_undist.jpg" width = "400" alt="Combined Image" />	</p>

</br>


<br>

III. Using color transforms, gradients, etc., to create a thresholded binary image

* Open cv package `cv2.Sobel` is used in order to create Thresholded Binary Images. 
* We used five different type of threshold that four of them are based on `cv2.Sobel` and one of them is based on color channel.
* `cv2.Sobel` is used to apply threshold in `x`, `y`, `magnitud`, and `angles`.
* `RGB` images are first converted to `hls` format and then `s` is used for color thresholding.
* All of these threshold are applied to a sample image and the result will become a binary thresholded images as the following image.

<p align="center"><img src="examples/Threshold_Binary.png" width = "850" alt="Combined Image" /> </p>

</br>


<br>

IV. Generating "Bird Eye View" of images

* We used perspective transform in order to change images into "Bird Eye View".
* In order to transform images into "Bird Eye View", we first used opencv `cv2.getPerspectiveTransform` library in order to get transformation matrices.
* Having a sample source and destination image can help us to get these transforms because we can pick corresponding points in source and destination images and map them together by `cv2.getPerspectiveTransform`.
* Having a sample images we these points as our source and destination points. `src = [[581, 477],[699, 477],[896, 675],[384, 675]]` and `dst = [[384, 0],[896, 0],[896, 720],[384, 720]]`

</br>


<br>

V.

</br>


<br>

VI.

</br>



<br>

VII.

</br>



<br>

VIII.

</br>
