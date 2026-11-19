penglings = readtable('.\penglings.csv');

adelie = penglings(penglings.species == "Adelie", :);
chinstrap = penglings(penglings.species == "Chinstrap", :);
gentoo = penglings(penglings.species == "Gentoo", :);

tiledlayout("flow");
nexttile
bubblechart(adelie,"flipper_length_mm","body_mass_g","bill_length_mm", ...
    "MarkerFaceColor","#ff8e08","MarkerEdgeColor","#ff8e08","MarkerFaceAlpha",0.8)
bubblesize([5 20])
hold on
bubblechart(chinstrap,"flipper_length_mm","body_mass_g","bill_length_mm", ...
    "MarkerFaceColor","#9933cc","MarkerEdgeColor","#9933cc","MarkerFaceAlpha",0.8)
bubblesize([5 20])
bubblechart(gentoo,"flipper_length_mm","body_mass_g","bill_length_mm", ...
    "MarkerFaceColor","#158f8f", "MarkerEdgeColor","#158f8f","MarkerFaceAlpha",0.8)
bubblesize([5 20])
xlabel("Flipper Length (mm)")
ylabel("Body Mass (g)")

ax = gca;
grid(ax, "on");

ax.Color = "#ebebeb";
ax.GridColor = "#fdfdfd";
ax.GridLineWidth = 2;
ax.MinorGridLineWidth = 1.2;
hold off

sizelegend = bubblelegend("bill length (mm)");
colorlegend = legend("Adelie","Chinstrap","Gentoo");
title(colorlegend,"species")
sizelegend.BubbleSizeOrder = "ascending";
sizelegend.Layout.Tile = "east";
colorlegend.Layout.Tile = "east";