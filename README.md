# Contactless-HCI-system
Authors: Yixin Yang (yangyx20@mails.tsinghua.edu.cn), Yunhui Gao (gyh21@mails.tsinghua.edu.cn), Kexuan Liu (lkx20@mails.tsinghua.edu.cn), Zehao He (hezehao@tsinghua.edu.cn) and Liangcai Cao (clc@tsinghua.edu.cn)

## Synopsis
Contactless human-computer interaction system based on three-dimensional (3D) holographic display and gesture recognition.

A hand-tracking sensor is used to collect the user’s gestures and fingertip positions as input.

A spatial light modulator (SLM) is utilized to generate the corresponding holographic 3D display images.

## Devices
Hand-tracking sensor: Leap Motion

Display device: liquid-crystal SLM （GAEA-2, Holoeye is utilized here）

## Usage
* The folder "object" contains the designed 3D display patterns.
  
* Run "reconstruction.m" to calculate holograms.
  
* Run "run.py" to establish a user-interctive 3D virtual keyboard. The Leap Motion and the SLM are controlled in a synchronous way.

## Contact
If you have any questions, please contact Yixin Yang (yangyx20@mails.tsinghua.edu.cn)
