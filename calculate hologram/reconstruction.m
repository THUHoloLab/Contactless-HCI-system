clear;close all;clc;
%% variable parameter
z=0.18;
lamda=5.20e-7;   
pix=3.74e-6;  
phi=imread('.\hologram\hologram_0.bmp'); 
% phi=rgb2gray(phi);  
% rn='reconstruction_hololab_dire.bmp';
%% fixed parameter
k=2*pi/lamda;  
[mm,nn]=size(phi);
a=(4*nn-1)/(2*nn-1);b=(4*mm-1)/(2*mm-1);
[fx,fy]=meshgrid(linspace(-1/(2*pix),1/(2*pix),2*nn),linspace(-1/(2*pix),1/(2*pix),2*mm)); 
[fxr,fyr]=meshgrid(linspace(-1/(2*pix)*a,1/(2*pix)*a,4*nn),linspace(-1/(2*pix)*b,1/(2*pix)*b,4*mm)); 
%% figure
phi=im2double(phi);  
%% reconstruction
compholo=exp(1i*2*pi*phi);    
compholo_0=zero_padding(compholo,2*mm,2*nn);    
u1_0=fftshift(fft2(fftshift(compholo_0))); 
h_AS_0=exp(1i*k*(-z).*sqrt(1-(lamda*fx).^2-(lamda*fy).^2));
u2_0=fftshift(ifft2(fftshift(u1_0.*h_AS_0))); 
u2=remove_padding(u2_0,mm,nn);
img=abs(u2);
img_1=mat2gray(img);   %_1代表归一化
%% reconstruction:add sample
% compholo=exp(1i*2*pi*phi);    
% compholo_0=zero_padding(compholo,2*mm,2*nn);    
% u1_0=fftshift(fft2(fftshift(compholo_0))); 
% u1_0_as=zero_padding(u1_0,4*mm,4*nn);    
% h_AS_0_as=exp(1i*k*(-z).*sqrt(1-(lamda*fxr).^2-(lamda*fyr).^2));
% u2_0_as=fftshift(ifft2(fftshift(u1_0_as.*h_AS_0_as))); 
% u2=remove_padding(u2_0_as,2*mm,2*nn);
% img=abs(u2);
% img_1=mat2gray(img);   %_1代表归一化
%% image show
figure;imshow(img_1,[])
% imwrite(img_1,rn)