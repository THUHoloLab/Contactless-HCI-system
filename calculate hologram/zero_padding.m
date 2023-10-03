function IMGout=zero_padding(IMGin,mm,nn);

[m,n]=size(IMGin);   %m��������n��������

t1=ceil((mm-m)/2);    %������Ҫ��չ������
t2=fix((mm-m)/2);
s1=ceil((nn-n)/2);    %������Ҫ��չ������
s2=fix((nn-n)/2);

T1=zeros(m,s1);     %�������߸���չs��
T2=zeros(m,s2);
T3=zeros(t1,n+s1+s2); %�������˸���չt��
T4=zeros(t2,n+s1+s2);

IMGout=[T1,IMGin,T2];
IMGout=[T3;IMGout;T4];

return