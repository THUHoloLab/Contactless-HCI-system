function IMGout=zero_padding(IMGin,mm,nn);

[m,n]=size(IMGin);   %m是行数，n是列数；

t1=ceil((mm-m)/2);    %单边需要扩展的行数
t2=fix((mm-m)/2);
s1=ceil((nn-n)/2);    %单边需要扩展的列数
s2=fix((nn-n)/2);

T1=zeros(m,s1);     %左右两边各扩展s列
T2=zeros(m,s2);
T3=zeros(t1,n+s1+s2); %上下两端各扩展t行
T4=zeros(t2,n+s1+s2);

IMGout=[T1,IMGin,T2];
IMGout=[T3;IMGout;T4];

return