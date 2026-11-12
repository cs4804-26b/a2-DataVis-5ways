#include <matplot/matplot.h>

#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace matplot;

struct Penguin {
    std::string species;
    double billLength;
    double flipperLength;
    double bodyMass;
};

std::vector<Penguin> loadPenguins(const std::string& filename) {
    std::vector<Penguin> penguins;

    std::ifstream file(filename);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open " + filename);
    }

    std::string line;
    std::getline(file, line);

    while (std::getline(file, line)) {
        std::stringstream ss(line);

        std::string dummy;
        std::string species;
        std::string billLength;
        std::string flipperLength;
        std::string bodyMass;

        std::getline(ss, dummy, ',');
        std::getline(ss, species, ',');
        std::getline(ss, dummy, ',');
        std::getline(ss, billLength, ',');
        std::getline(ss, dummy, ',');
        std::getline(ss, flipperLength, ',');
        std::getline(ss, bodyMass, ',');
        std::getline(ss, dummy, ',');
        std::getline(ss, dummy, ',');

        // Skip rows with missing values
        if (species == "NA" || billLength == "NA" || flipperLength == "NA" || bodyMass == "NA") {
            continue;
        }

        penguins.push_back({
            species,
            std::stod(billLength),
            std::stod(flipperLength),
            std::stod(bodyMass)
        });
    }

    return penguins;
}

int main() {
    std::vector<Penguin> penguins = loadPenguins("../penglings.csv");

    std::vector<double> x, y, sizes;

    std::vector<double> adelieX, adelieY, adelieSizes;
    std::vector<double> chinstrapX, chinstrapY, chinstrapSizes;
    std::vector<double> gentooX, gentooY, gentooSizes;

    for (const auto& p : penguins) {
        if (p.species == "\"Adelie\"") {
            adelieX.push_back(p.flipperLength);
            adelieY.push_back(p.bodyMass);
            adelieSizes.push_back(p.billLength);
        }
        else if (p.species == "\"Chinstrap\"") {
            chinstrapX.push_back(p.flipperLength);
            chinstrapY.push_back(p.bodyMass);
            chinstrapSizes.push_back(p.billLength);
        }
        else if (p.species == "\"Gentoo\"") {
            gentooX.push_back(p.flipperLength);
            gentooY.push_back(p.bodyMass);
            gentooSizes.push_back(p.billLength);
        }
    }

    auto fig = figure(true);
    fig->size(1000, 700);

    hold(on);

    auto adelie = scatter(adelieX, adelieY, adelieSizes);
    adelie->marker_color({0.99, 0.57, 0.18});
    adelie->marker_face(true);

    auto chinstrap = scatter(chinstrapX, chinstrapY, chinstrapSizes);
    chinstrap->marker_color({0.66, 0.25, 0.82});
    chinstrap->marker_face(true);

    auto gentoo = scatter(gentooX, gentooY, gentooSizes);
    gentoo->marker_color({0.08, 0.61, 0.61});
    gentoo->marker_face(true);

    xlabel("Flipper Length (mm)");
    ylabel("Body Mass (g)");

    xlim({170, 235});
    ylim({2500, 6500});

    grid(on);

    legend({"Adelie", "Chinstrap", "Gentoo"});

    show();
}