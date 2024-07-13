## Task-T1: 
  ## What are the utility and types of neural networks? Perform Heart Disease Classification using feed forward Neural Network on given dataset.
   Neural networks are complex computational models designed to imitate the structure and function of the human brain. They consist of interconnected nodes (neurons) that process and transmit information.
  ### Types of Neural Networks:

#### 1. Feedforward Neural Networks (FNNs)
- The most common type.
- Information flows from input to output layers.
- Used for tasks like image classification, regression, and basic pattern recognition.

#### 2. Convolutional Neural Networks (CNNs)
- Specifically designed for image processing and computer vision.
- Utilize convolutional layers to extract features from images.
- Widely used in image recognition, object detection, and segmentation.

#### 3. Recurrent Neural Networks (RNNs)
- Suitable for sequential data (e.g., time series, natural language).
- Have loops that allow information to persist across time steps.
- Used in speech recognition, language modeling, and machine translation.

#### 4. Long Short-Term Memory (LSTM) Networks
- A type of RNN with memory cells for longer information retention.
- Effective for handling long sequences and avoiding vanishing gradients.
- Commonly used in natural language processing (NLP) and speech recognition.

#### 5. Generative Adversarial Networks (GANs)
- Composed of a generator and a discriminator.
- Generator creates new data samples, while discriminator distinguishes real from generated data.
- Used for image generation, style transfer, and data augmentation.
# Performing Heart Disease Classification using feed forward Neural Network on given dataset.
### Given Dataset
| age | sex | cp | trestbps | chol | fbs | restecg | thalach | exang | oldpeak | slope | ca | thal | target |
|-----|-----|----|----------|------|-----|---------|---------|-------|---------|-------|----|------|--------|
| 52  | 1   | 0  | 125      | 212  | 0   | 1       | 168     | 0     | 1.0     | 2     | 2  | 3    | 0      |
| 53  | 1   | 0  | 140      | 203  | 1   | 0       | 155     | 1     | 3.1     | 0     | 0  | 3    | 0      |
| 70  | 1   | 0  | 145      | 174  | 0   | 1       | 125     | 1     | 2.6     | 0     | 0  | 3    | 0      |
| 61  | 1   | 0  | 148      | 203  | 0   | 1       | 161     | 0     | 0.0     | 2     | 1  | 3    | 0      |
| 62  | 0   | 0  | 138      | 294  | 1   | 1       | 106     | 0     | 1.9     | 1     | 3  | 2    | 0      |

## Model Summary

```
----------------------------------------------------------------
Layer (type)                Output Shape              Param #   
=================================================================
dense_123 (Dense)           (None, 1)                 14        
dense_124 (Dense)           (None, 1)                 2         
=================================================================
Total params: 16 (64.00 Byte)
Trainable params: 16 (64.00 Byte)
Non-trainable params: 0 (0.00 Byte)
-----------------------------------------------------------------
```
### model training and validation
<img src = "https://github.com/user-attachments/assets/b4166c1d-fdfe-4634-9b93-5e532b69d2c2">
<img src = "https://github.com/user-attachments/assets/0c127204-46c4-4a14-afc3-4feb2afa6f88">

### Evaluate the model on test dataset
```python
2/2 [==============================] - 0s 6ms/step - loss: 0.4091 - acc: 0.8852
Test loss: 40.913450717926025 %
Test Accuracy: 88.52459192276001 %
```
### prediction
```python
1/1 [==============================] - 0s 50ms/step
predict:- No Desease
age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	target
237	57	1	1	124	261	0	1	141	0	0.3	2	0	3	0

1/1 [==============================] - 0s 26ms/step
predict:- Deasease Detacted
age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	target
24	42	0	2	120	209	0	1	173	0	0.0	1	0	2	1
```
