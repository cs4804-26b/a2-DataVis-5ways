my_csv = readtable('data/penglings.csv');
adelieData = my_csv(strcmp(my_csv.species, 'Adelie'), :);
gentooData = my_csv(strcmp(my_csv.species, 'Gentoo'), :);
chinstrapData = my_csv(strcmp(my_csv.species, 'Chinstrap'), :);

s = scatter(adelieData.flipper_length_mm, ...
        adelieData.body_mass_g, ...
        (adelieData.bill_length_mm-25)*4, ...
        'filled');
s.MarkerFaceColor = '#FF9633';
s.MarkerFaceAlpha = 0.8;
hold on;
s = scatter(gentooData.flipper_length_mm, ...
     gentooData.body_mass_g, ...
     (gentooData.bill_length_mm-25)*4, ...
     'filled');
s.MarkerFaceColor = '#14978C';
s.MarkerFaceAlpha = 0.8;
s = scatter(chinstrapData.flipper_length_mm, ...
     chinstrapData.body_mass_g, ...
     (chinstrapData.bill_length_mm-25)*4, ...
     'filled');
s.MarkerFaceColor = '#801BBA';
s.MarkerFaceAlpha = 0.8;
hold off;

xlabel("Flipper Length (mm)");
ylabel("Body Mass (g)");
grid on;
legend("Adelie", "Gentoo", "Chinstrap")