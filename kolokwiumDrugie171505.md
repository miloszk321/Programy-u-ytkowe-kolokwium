``` scilab
Zadanie 1a
result = 1 + log(5) + log(5)/log(2) + log(5)/log(7);
disp(result);
```
```scilab
B)
a=[1,-2,3;2,3,6;1,-2,8;8,3,6];
 b =[2,6;1,4;1,-2;8,-1];
C=a'*b;
disp(c)
```
```scilab
C)
 a = 14;
 h = 22; 
 V = sqrt(3)/2 * a^2 * h;
disp(V);
```
```scilab
D)
n = 11;
sum_X = 0;

for k = 2:3:(33-1) 
    term = (2 * k^2 + 20) / log(k^2 + 20);
    sum_X = sum_X + term;
end
disp(sum_X);
```
```scilab
Zadanie 2
x = linspace(-2, 4, 100);

f1 = 3.^(x.^2 + 4) + 4;
f2 = (x.^4 + 4*x) ./ (11*x.^2 + 3) + 3;

plot(x, f1, '-b', x, f2, '-r');
title('Wykres funkcji f1 i f2');
xlabel('x');
ylabel('y');
legend('f1 = 3^{x^2 + 4} + 4', 'f2 = (x^4 + 4x)/(11x^2 + 3) + 3');
grid on;
```
```scilab
Zadanie 3
rok = [2010, 2012, 2014, 2016, 2018];
USA = [12, 23, 52, 23, 31];
Rosja = [27, 17, 62, 62, 19];

bar(rok, [USA', Rosja'], 'grouped');
title('Liczba medali w latach 2010-2018 (USA i Rosja)');
xlabel('Rok');
ylabel('Liczba medali');
legend('USA', 'Rosja');
xgrid;
ygrid;
```
