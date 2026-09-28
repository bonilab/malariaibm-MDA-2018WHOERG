folder ='raw';
scenarios = [
"0",
"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"10",
"11",
"12",
"13",
"14",
"15",
"16",
"17",
"18",
"19" ];

%%

C580Y_ids = [4 5 6 7 12 13 14 15 20 21 22 23 28 29 30 31 36 37 38 39 44 45 46 47 52 53 54 55 60 61 62 63 68 69 70 71 76 77 78 79 84 85 86 87 92 93 94 95 100 101 102 103 108 109 110 111 116 117 118 119 124 125 126 127 ];
C580Y_ids =C580Y_ids +1;
plasmepsin_ids = [2 3 6 7 10 11 14 15 18 19 22 23 26 27 30 31 34 35 38 39 42 43 46 47 50 51 54 55 58 59 62 63 66 67 70 71 74 75 78 79 82 83 86 87 90 91 94 95 98 99 102 103 106 107 110 111 114 115 118 119 122 123 126 127 ];
plasmepsin_ids = plasmepsin_ids+1;
double_mutation = intersect(C580Y_ids, plasmepsin_ids);

%%
n_run = 1000;
step = 1000;
total_time = 34*12+1;
parfor idx = 1:numel(scenarios)
% for idx = 1:1
    fprintf('%s\n',scenarios(idx));
    %     sce_data = zeros(n_run,409,128);
    pfpr_all = zeros(n_run,409);
    C580Y_frequency_all = zeros(n_run,409);
    plas_frequency_all = zeros(n_run,409);
    double_mutation_freq_all = zeros(n_run,409);
    infections_all = zeros(n_run,409);
    pfpr2030_all = zeros(n_run,1);
    positive_cases_all = zeros(n_run,409);

    for i = 1:n_run
        file_idx = i-1 +  (idx-1)*step;
        fn = sprintf('%s\\monthly_data_%d.txt',folder,file_idx);

        if isfile(fn)
            % File exists.
            data = dlmread(fn);
            genotype_distribution = data(:,25:25+127);

            C580Y_distribution = genotype_distribution(:,C580Y_ids);
            C580Y_frequency = sum(C580Y_distribution,2) ./ sum(genotype_distribution,2);

            plas_distribution = genotype_distribution(:,plasmepsin_ids);
            plas_frequency = sum(plas_distribution,2) ./ sum(genotype_distribution,2);

            %         sce_data(i,:,:) = genotype_distribution;
            double_mutation_dist = genotype_distribution(:,double_mutation);
            double_mutation_frequency = sum(double_mutation_dist,2) ./ sum(genotype_distribution,2);

            C580Y_frequency_all(i,:) = C580Y_frequency;
            plas_frequency_all(i,:) = plas_frequency;
            double_mutation_freq_all(i,:) = double_mutation_frequency;

            pfpr_all(i,:) = data(:,13);
            infections_all(i,:) = data(:,17);
            pfpr2030_all(i) = data(291,13);
            positive_cases_all(i,:) = data(:,283);
        else
            % File does not exist.
            fprintf('Missing: %s\n', fn);
        end
    end

    C580Y_frequency_all = transpose(C580Y_frequency_all);
    plas_frequency_all = transpose(plas_frequency_all);
    double_mutation_freq_all = transpose(double_mutation_freq_all);
    pfpr_all = transpose(pfpr_all);
    infections_all = transpose(infections_all);
    positive_cases_all = transpose(positive_cases_all);

    dlmwrite(sprintf("data\\%s_C580Y.csv",scenarios(idx)),C580Y_frequency_all,'delimiter',',','precision',9);
    dlmwrite(sprintf("data\\%s_plas.csv",scenarios(idx)),plas_frequency_all,'delimiter',',','precision',9);
    dlmwrite(sprintf("data\\%s_pfpr.csv",scenarios(idx)),pfpr_all,'delimiter',',','precision',9);
    dlmwrite(sprintf("data\\%s_infections.csv",scenarios(idx)),infections_all,'delimiter',',','precision',9);
    dlmwrite(sprintf("data\\%s_pfpr2030.csv",scenarios(idx)),pfpr2030_all,'delimiter',',','precision',9);
    dlmwrite(sprintf("data\\%s_positive.csv",scenarios(idx)),positive_cases_all,'delimiter',',','precision',9);
    dlmwrite(sprintf("data\\%s_580Y_plas2.csv",scenarios(idx)),double_mutation_freq_all,'delimiter',',','precision',9);
end

%%
%extract date
% timepoint =datestr(datetime(data(:,2),'ConvertFrom','posixtime'));
% dlmwrite("timestamp.csv",data(:,2),'delimiter',',','precision',9 );
