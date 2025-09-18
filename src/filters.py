import cv2
import numpy as np


class Filters:
    # TODO: Image kernels
    Kernels = {
        'original' : np.array([[0,0,0],
                      [0,1,0],
                      [0,0,0]]),
        'blur' : np.array([[1,1,1],
                  [1,1,1],
                  [1,1,1]], dtype=np.float32)/9,
        'gaussian blur' : np.array([[1,2,1],
                           [2,4,2],
                           [1,2,1]], dtype=np.float32)/16,
        'sharpen' : np.array([[0,-1,0],
                     [-1,5,-1],
                     [0,-1,0]]),
        'sobel (x)' : np.array([[-1,0,1],
                      [-2,0,2],
                      [-1,0,1]]),
        'sobel (y)' : np.array([[-1,-2,-1],
                      [0,0,0],
                      [1,2,1]]),
        'edge detection' : np.array([[-1,-1,-1],
                            [-1,8,-1],
                            [-1,-1,-1]]),
        'emboss' : np.array([[-2,-1,0],
                    [-1,1,1],
                    [0,1,2]])
    }

    def __init__(self, kernels=Kernels):
        self.kernels = kernels
        self.kernels_list = list(kernels.keys())
        self.count = 0
        
        # TODO: Implement internal variables


    def apply_filter(self, frame, filter_name) -> np.array:
        # TODO: Apply the selected filter kernel to the frame
        kernel = self.kernels[filter_name]
        return cv2.filter2D(frame, -1, kernel)

    def get_current_filter_name(self) -> str:
        # TODO: Return currently set kernels's name
        return self.kernels_list[self.count]

    def switch_next_filter(self):
        # TODO: Update currently selected kernel to the next
        self.count+=1
        self.count = self.count % len(self.kernels_list)        

    def switch_previous_filter(self):
        # TODO: Update currently selected kernel to the previous
        self.count-=1
        self.count = self.count % len(self.kernels_list)        

