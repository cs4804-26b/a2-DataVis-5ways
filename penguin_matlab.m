% Load data
opts = detectImportOptions("penglings.csv");
df = readtable("penglings.csv", opts);

% Drop rows with missing values
T = rmmissing(df, 'DataVariables', ... 
    {'bill_length_mm','flipper_length_mm','body_mass_g'});
T.species = categorical(T.species);

% Colors matching the original plot
species_name = {'Adelie', 'Chinstrap', 'Gentoo'};
species_color = [1.00 0.55 0.10; 0.60 0.15 0.80; 0.05 0.45 0.45];

% Map bill length to marker area
minArea = 10;
maxArea = 150;
b1 = T.bill_length_mm;
sizeData = minArea + (b1 - min(b1)) / (max(b1) - min(b1)) * (maxArea - minArea);

% Figure
fig = figure('Color', 'w', 'Position', [100, 100, 850, 520]);
ax = axes(fig);
hold(ax, 'on');

for i = 1:numel(species_name)
    mask = T.species == species_name{i};
    scatter(ax, T.flipper_length_mm(mask), T.body_mass_g(mask), ...
        sizeData(mask), species_color(i, :), 'filled', ...
        'MarkerFaceAlpha', 0.8, 'MarkerEdgeColor', 'none', ...
        'DisplayName', species_name{i});
end

% ggplot2-style gray panel with white grid
ax.Color = [0.90 0.90 0.90];
ax.XGrid = 'on';
ax.YGrid = 'on';
ax.XMinorGrid = 'on';
ax.YMinorGrid = 'on';
ax.GridColor = 'w';
ax.GridAlpha = 1;
ax.MinorGridColor = 'w';
ax.MinorGridAlpha = 0.6;
ax.Box = 'off';
ax.TickDir = 'out';
ax.Layer = 'top';
ax.XLim = [168 234];
ax.YLim = [2500 6500];
ax.XTick = 170:10:230;
ax.YTick = 3000:1000:6000;
ax.FontSize = 11;

xlabel(ax, 'Flipper Length (mm)', 'FontSize', 14);
ylabel(ax, 'Body Mass (g)', 'FontSize', 14);

% Species legend
lgd = legend(ax, 'Location', 'eastoutside');
title(lgd, 'Species');
lgd.Box = 'off';

% Bill length size legend (separate dummy markers)
refVals = [40 50];
refSizes = minArea + (refVals - min(b1)) ./ (max(b1) - min(b1)) * (maxArea - minArea);
ax2 = axes(fig, 'Position', [0.80 0.62 0.17 0.2], 'Visible', 'off');
hold(ax2, 'on');
xlim(ax2, [0 1]); ylim(ax2, [0 1]);
text(ax2, 0, 0.95, 'bill\_length\_mm', 'FontSize', 13, 'VerticalAlignment','top');
for k = 1:numel(refVals)
    scatter(ax2, 0.12, 0.60 - (k-1)*0.30, refSizes(k), 'k', 'filled', ...
        'MarkerFaceAlpha', 0.8);
    text(ax2, 0.30, 0.60 - (k-1)*0.30, num2str(refVals(k)), ...
        'FontSize', 11, 'VerticalAlignment','middle');
end

% Shrink main axes to leave room for the legends
ax.Position = [0.09 0.14 0.68 0.82];
lgd.Position = [0.80 0.30 0.15 0.2];