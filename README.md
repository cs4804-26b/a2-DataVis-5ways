# Assignment 2 fo CS4804 B26
### Param Amre

## View Files
For all library based visualizations, please run an http server at the root of the project, bound to localhost:8000. Run anything needed to generate the html file (see relevant section for directions), and naviage to localhost:8000/folder-name/ to see and interact with the graph.

## Javascript + d3

Javascript is a scripting language primarily developed for the web. d3 is an data science industry standard that provides abstractions for creating visualizations.
I started with the code from the [basic d3 scatter plot ecample](https://observablehq.com/@d3/scatterplot/2), and adjusted it for the dataset we were given.
Using d3's documentation, I was also able to find the d3 way of adding hoverable interactivity, similar to my submission for assignment 1.

### Technical Achievements
- Hoverable interactivity: when a user hovers over a given point, then can look at the popup in the lower right of the graph to see the exact values that points represents

### Design Achievements
- Legend: I manually created a legend in d3, using basic svg tag types. I wasn't able to find any automatic legend creation values in the docs, so I manually drew one out myself.


