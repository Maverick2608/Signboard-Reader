# Signboard-Reader

• Implemented ORB algorithm to detect 10 common traffic signs within a range of 4 feet to assist the visually impaired

• The system is portable and consists of a Raspberry Pi microcontroller, a monocular camera mounted on spectacles and the output is in audio format via a pair of earphones

![alt text](https://github.com/Maverick2608/Signboard-Reader/blob/main/Prototype.jpg)

Abstract - 
In this paper, a camera based real time signboard reading system has been proposed, in order to assist the visually impaired people. The system is a portable backpack, which consists of a monocular camera, mounted on a spectacle and earphones for providing audio feedback. The aim of the project is to develop a prototype which will aid the visually impaired to read signs and help them in their day-to-day life.

Introduction -
Visually impaired people face many challenges in their daily routine. Most of these problems can be solved by utilizing modern technologies being produced and researched. Many social awareness programs are conducted worldwide associating the social work with science that can help developing the society. Technologies like – assistive cane, vibration stick, smartphone based navigation system, etc. are being researched and manufactured to help blind or visually impaired. Out of the 314 million visually impaired people worldwide, 45 million people are blind. Even in the developed countries these numbers are increasing rapidly. Recent developments in computer vision, digital cameras, and portable computers make it feasible to assist these individuals by developing camera based products that combine such optical character recognition systems. The proposed project in this paper introduces an assistive system which will aid the visually impaired and blind by identifying the signboards they come across in their daily life. This will enable the blind to travel without any human assistance.

Results - 
The signboard images from the dataset were recognized using the system introduced in the paper. Whenever a signboard or the image of signboard captured by the camera is successfully matched with any of the templates, the user is provided with an audio output in Marathi, mentioning the name of signboard. The set of images were first tested on webcam of a computer. The features were matched for all signboards, given that the threshold values were set. The audio output was obtained.
The same process was carried out using Raspberry Pi 3B+ microcontroller. All predefined signboards were successfully matched and recognized on a real time basis. An audio feedback in Marathi was obtained and could be listened through earphones connected with RPi.
