clear;close all;clc;
for jj=1:1
str1=num2str(jj);
m=2160;n=3840; 
OUTPUT = 0;
for ii=2:3
%% variable parameter
m=2160;n=3840;    %m、n为图像像素数
mm=4320;nn=7680;  %mm、nn为zero padding后的像素数，奇偶均可
str=num2str(ii);
ob_str=['.\object\dot_l',str,'.tif'];
hn_str=['.\hologram\hologram_dot_v2.bmp'];
% rn_str=['C:\Users\lkx20\Desktop\GS_zero_padding2\reconstruction\reconstruction_',str,'.bmp'];
% pn_str=['E:\second paper algorithm\GS_for_contrast\psnr_',str,'.bmp'];
obj=imread(ob_str);  %输出数据类型为uint8
obj=rgb2gray(obj);    %输出数据类型为uint8
z=0.16+(ii-1)*0.001;    %z>0
lamda=5.20e-7;                      
pix=3.74e-6;    
t0=100;    %GS算法迭代次数
%% fixed parameter
k=2*pi/lamda;  
[fx,fy]=meshgrid(linspace(-1/(2*pix),1/(2*pix),nn),linspace(-1/(2*pix),1/(2*pix),mm));
%% figure
obj=imresize(obj,[m,n]); 
obj=im2double(obj);    %输出数据类型为double
%% GS algorithm
for t=1:t0
    if t==1
        obj_com=obj.*exp(1i*2*pi*rand(m,n));  %随机相位
    else
        obj_com=obj.*exp(1i*img_phi);
    end 
  obj_com_0=zero_padding(obj_com,mm,nn);
  U1_0=fftshift(fft2(fftshift(obj_com_0))); 
  H_AS_0=exp(1i*k*z.*sqrt(1-(lamda*fx).^2-(lamda*fy).^2));
  U2_0=fftshift(ifft2(fftshift(U1_0.*H_AS_0))); 
  U2=remove_padding(U2_0,m,n);
  phi=angle(U2);
%% reconstruction
  compholo=exp(1i*phi);    
  compholo_0=zero_padding(compholo,mm,nn); 
  u1_0=fftshift(fft2(fftshift(compholo_0))); 
  h_AS_0=exp(1i*k*(-z).*sqrt(1-(lamda*fx).^2-(lamda*fy).^2));
  u2_0=fftshift(ifft2(fftshift(u1_0.*h_AS_0))); 
  u2=remove_padding(u2_0,m,n);
  img=abs(u2);   
  img_1=mat2gray(img);   %_1代表归一化
  img_phi=angle(u2);
%% RMSE
%   rmse=sqrt(mean(mean((obj-img).^2)));
%   rmse_all(t,1)=rmse;
% %% PSNR
%   peaksnr=psnr(img,obj);    %不要归一化，否则不收敛
%   peaksnr_all(t,1)=peaksnr;
end 

OUTPUT=OUTPUT+U2;

% figure;imshow(mat2gray(phi),[])
figure;imshow(img_1,[])
% figure;plot(1:t0,rmse_all)
% figure;plot(1:t0,peaksnr_all)


% imwrite(mat2gray(phi),hn_str)
% imwrite(img_1,rn_str)
% plot_psnr=plot(1:t0,peaksnr_all);
% saveas(plot_psnr,pn)
end

OUTPUT=mat2gray(angle(OUTPUT));
imwrite(OUTPUT,hn_str)

end