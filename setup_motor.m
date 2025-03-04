% Khai báo các biến
U_pr = linspace(100, -100, 200);      % Điện áp đặt vào động cơ (tính theo %)
ke = 0.1;     % Hằng số điện động - 
Tm = 0.06;    % Hằng số thời gian cơ học của động cơ
J= 0.0023;    % Môment quán tính  

% Lưu các giá trị vào workspace
assignin('base', 'U_pr', U_pr);
assignin('base', 'ke', ke);
assignin('base', 'Tm', Tm);
assignin('base', 'J', J);

%plot(out.theta.time, out.theta.signals.values);
%xlabel('Time, s');
%ylabel('Angel, rad');
%hold on

%plot(out.omega.time, out.omega.signals.values);
%xlabel('Time, s');
%ylabel('Angular speed, rad/s');
%legend('Theta', 'Omega');

figure;
w_yct = U_pr*ke;    % tốc độ góc ổn định - установившуюся скорость двигателя
Tm = 0;            % электромеханическую постоянную времени

plot(U_pr, w_yct, '-b', 'LineWidth', 2);
grid on;
xlabel('voltage, %');
ylabel('w_у_с_т, rad/c');
%title('Dependency of \omega_{yct} on U_{pr}');
hold on

plot(U_pr, Tm, '-r', 'LineWidth', 2);
grid on;
xlabel('voltage, %');
ylabel('Tm, c');
legend('w_y_c_t', 'Tm');

