Assignment 2 - Data Visualization, 5 Ways  
===
# Default:<br>
![Default](img/ggplot2.png)<br>
This was the goal that I was attempting to recreate in different tools/libraries

# Python with Matplotlib:<br>
![matplotLib](img/pythonPlt.png)<br>
This was fairly easy for a library, although knowing pyhton or having experience definitely helps. I really struggled to get legends to work. Having two seperate legends required a handler. Also I fought with placment of the legends for a long time. I wanted them to be on the right and outside of the graph which seemed doable with "outer upper right" but there were two placement methods and the one that worked with my code did not allow for "outer". I also had to offset the second legend so they were readable. 
I set the size of the dots to be 1.1^(bill_length_mm) which made the change in size more distinct wile still being readable. For some reason this made the legends a bit weird where the Species legend ended up having diffent sized dots<sub>1</sub>. I don't know what exactly the size is based on but I would assume it was the average size per species. Annoyingly the size legend didn't actually show that much of a difference. This is why I used exponential in the data drawing portion, but I was unable to appy that change to the legend. I think this is the most accurate so far except for my legend issues.<br>
1. I later changed it to size = 2*(bill_length_mm) which fixed the legend <br>
Credit to<br>
-Benjamin Greenwood<br>
-VS Code Copilot<br>
-Griffon Munhall<br>

# Tableau:<br>
![Tableau_2ndVersion](img/Tableau_update.png)<br>
This was extremely easy. In total took me maybe 15 minutes. At first I found tableau public desktop to be a bit confulsing, but quickly learned that it worked by dragging data attributes onto graph attributes. For example dragging Species onto the color icon to get points to be colored by species. This was amazing and I would love to use it again in the future. Intrestingly I notices that there were more "bill_length_mm" than in the example and I do not know why exactly, but I think the overal outcome is the same.<br>
Version 2: I changed the colors and messed around with size to make the scaling more noticable. I had used "Edit in Shelf" then 2*[Bill_length_mm] but then the legend was only showing the multiplied version, so I undid that. 

# Fourish:<br>
![Flourish](img/Flourish_penguin2.png)<br>
This was simple like Tableau, which is expected as it is a tool and not a language. But I had many annoyances. Maybe using their built in AI could have helped me solve some of these but I am just going to list my user experience issues without the use of AI. I liked how you could load in data and it showed it as a table and also ass you assigned attributed the graph thumbnail changed in real time accordingly. On the other hand I struggled to change the colors from the presets to something more specific. I also couldn't make the size use a fancier function like [Bill_length_mm]^1.2 or x2.5, as it seemed to only allow an attribute to be assigned to a column. There wasn't an easy way to make a new column with an equation like excel where =D3x2.5 or something like that would automatically change the value based on another column's value. I also wasn't able to figure out how to add a second legend with size which is annoying.<br>
Version 2: I was able to figure out how to modify the colors to be more accurate.

# D3 and JS:<br>
![D# + J# version screenshot](img/d3plt.png)<br>
This was tourturous and evil. I struggled with this so badly. I heavily relied on using code from the D3 gallery which I edited to fit my needs. I like the freedom D3 gives but I have very little JS knowledge, and dislike how things wouldn't show up when I expected them to. This took by far the longest, but also gives the most freedom. I do not like using copilot but I understand how convenient it can be. I am trying to read all code and understand it before using it. I felt like I had to use it just to be able to finish, even though it feels awful to say that<br>
Credit to:<br>
- https://d3-graph-gallery.com/graph/bubble_color.html I coppied this code directly and modified it
- VS Code Copilot
- Griffon Munhall
- Harrison Lane

# R and GGplot <br>
![R with GGplot2](img/Rplot.png)<br>
R plot is love R plot is life. Very simple and easy. Except for some reason in rStudio the Run button only runs one line instead of the file. Also my directory is filled with a bunch of R related files that I don't know what to do with and that seems anoying such as ".RData", ".Rhistory", another ".Rhistory", and ".Rproj.user". It may not be as flexible as D3 but I did not explore enough to confirm or deny that.
Thank you so much: <br>
- https://www.geeksforgeeks.org/r-language/data-visualization-with-r-and-ggplot2/
- R documentation in general that was so convenient

## Technical Achievements
- Created something in D3 that I am somewhat proud of
- Made fairly good recreations of the plot
- Got better at python and matplot
- Got more comfortable with the git workflow
- Managed time better in schedualing office hours
- Learned so much new syntac
- Used copilot to code for the first time

### Design Achievements
- Displayed required elements such as size and color in every plot
- Displayed non-required elements such as gridlines and legends in all plots. (Minus the legend in D3 due to dime constraints)
- Found multiple ways to manipulate size wheather just size = bill_length_mm or to multiply by a constant, or to raise the variable to a constant exponent
