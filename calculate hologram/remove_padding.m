function B=remove_padding(A,m,n)
[mm,nn]=size(A);

t1=ceil((mm-m)/2);    %������Ҫ��չ������
t2=fix((mm-m)/2);
s1=ceil((nn-n)/2);    %������Ҫ��չ������
s2=fix((nn-n)/2);

B(1:m,1:n)=A(t1+1:t1+m,s1+1:s1+n);