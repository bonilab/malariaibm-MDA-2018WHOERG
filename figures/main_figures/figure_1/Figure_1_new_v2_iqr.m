% from color brewer:

myalph=80;
myalph2=130;

color1 = [127,201,127,myalph]/256;
color2 = [190,174,212,myalph]/256;
color3 = [253,192,134,myalph]/256;
color4 = [255,255,153,myalph2]/256;

plot([0 4],[0 0], 'k-', 'LineWidth', 2 ); hold on;
plot([0 4],[1 1], 'k--', 'LineWidth', 2 ); 
set(gca, 'XTick', [0.699 1 1.301 1.699 2 2.301 2.699 3]);
set(gca, 'XTickLabel', {'5', '10', '20', '50', '100', '200', '500', '1000'});
xlabel('NUMBER OF PARASITE POSITIVE INDIVIDUALS');
ylabel('ALLELE FREQ ARTEMISININ RESISTANCE');
axis([0 3.2 -0.06 1.03]);




% %%%%% SCENARIO 1 %%%%%  GREEN
%
%
% This is the 1.0% PfPR scenario, f=0.8, with importation and no ITC, 5K
% population in 2022
%
% The median simulation here gets to about 120 infections in 2022, so
% that's 2.4% real prevalence in a population of 5000 individuals

%
% IQR for number of infected individuals in 2022 is 70 to 180
% MID QUINT for number of infected individuals in 2022 is 110 to 150
%

% first box showing prevalence+resistance in 2022, pre-MDA
x = log10(70);
y = -0.03;
w = log10(180) - x;
h = 0.04;
rectangle('Position',[x y w h],'FaceColor',color1,'LineStyle', 'none','Curvature',1.0); % coordinates are X Y W H, where X Y are for the bottom left corner

% after the MDA in 2025, there are 0 to 10 positive individuals left (IQR)
% after the MDA in 2025, there are 0 to 5 positive individuals left (MID QUINT)
% after the MDA in 2025, 580Y frequency is 0-0.7 (IQR) or 0.0-0.42 (MID QUINT)

x=0.0; y=0.0; w=1.0; h=0.70;
rectangle('Position',[x y w h],'FaceColor',color1,'LineStyle', 'none','Curvature',[0.2,1.0]);









% %%%%% SCENARIO 2 %%%%%  PURPLE
%
%
% This is the 1.0% PfPR scenario, with importation and no ITC, 5K
% population in 2022
%
% The median simulation here gets to about 190 infections in 2022, so
% that's 3.8% real prevalence in a population of 5000 individuals

%
% IQR for number of infected individuals in 2022 is 130 to 230
% MID QUINT for number of infected individuals in 2022 is 150 to 210
%

% first box showing prevalence+resistance in 2022, pre-MDA
x = log10(130);
y = -0.03;
w = log10(230) - x;
h = 0.04;
rectangle('Position',[x y w h],'FaceColor',color2,'LineStyle', 'none','Curvature',1.0); % coordinates are X Y W H, where X Y are for the bottom left corner

% after the MDA in 2025, there are 0 to 25 positive individuals left (IQR)
% after the MDA in 2025, there are 0 to 5 positive individuals left (MID QUINT)
% after the MDA in 2025, 580Y frequency is 0-0.79 (IQR) or 0.19-0.50 (MID QUINT)

x=0.3; y=0.0; w=1.2; h=0.79;
rectangle('Position',[x y w h],'FaceColor',color2,'LineStyle', 'none','Curvature',[0.2,1.0]);







% %%%%% SCENARIO 3 %%%%%   ORANGE
%
%
% This is the 0.5% PfPR scenario, with importation and with ITC at 65%, 10K
% population in 2022
%
% The median simulation here gets to about 150 infections in 2022, so
% that's 1.5% real prevalence in a population of 10,000 individuals

%
% IQR for number of infected individuals in 2022 is 90 to 230
% MID QUINT for number of infected individuals in 2022 is 120 to 200
%

% first box showing prevalence+resistance in 2022, pre-MDA
x = log10(90);
y = -0.01;
w = log10(230) - x;
h = 0.04;
rectangle('Position',[x y w h],'FaceColor',color3,'LineStyle', 'none','Curvature',1.0); % coordinates are X Y W H, where X Y are for the bottom left corner

% after the MDA in 2025, there are 0 to 7 positive individuals left (IQR)
% after the MDA in 2025, there are 0 to 5 positive individuals left (MID QUINT)
% after the MDA in 2025, 580Y frequency is 0-0.76 (IQR) or 0.07-0.50 (MID QUINT)

x=0.0; y=0.00; w=0.8451; h=0.76;
rectangle('Position',[x y w h],'FaceColor',color3,'LineStyle', 'none','Curvature',[0.2,1.0]);











