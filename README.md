The goal is to recreate this chart:

![The reference image](img/reference.png)

While preserving these features:

- x to flipper length
- y to body mass
- color to species
- size to bill length
- semitransparent circles
- don't start scales at 0 (we don't need that negative space)
- axes have reasonable ticks and labels

These are preferred but not required:

- the grid
- the legend

# d3 (library)

![The target graph rendered with d3.js](img/d3.png)

I basically already did all of this while doing assignment 1, so it was very
easy for me. I probably had to write a lot more code to get the chart to work,
but I didn't actually have to think very hard about it because I knew what I was
doing. The one thing I messed up when I was creating the chart was filtering out
entries with `NaN` because I wasn't properly mapping species data to numbers,
and `"Gentoo"` is actually `NaN` in JS :(

(I mean this literally, `isNaN("Gentoo")` returns `true`, and so does
`isNaN("not NaN")`)

# matplotlib (library)

![Kind of the target in matplotlib](img/matplotlib.png)

It was way harder to get the legend to work than it should have been for a
library which supposedly supports legends. I could not figure out how to make
the color legend function with custom colors, so instead I just set it up to use
to built-in `cool` gradient which looks better than the other gradients I tried.
Other than that, it was pretty easy for me to work with because like d3, I
already know how matplotlib and python work.

# altair (library)

![Pretty dang good to be honest](img/altair.png)

It looks prettier than basically all of the others, so that's a huge bonus.
Really weird that it can render to HTML, I imagine that's for interactivity but
I still think it's a bit strange. It's a little weird that their scales default
to 0 as the minimum in the domain, rather than as the actual minimum of the
data. Altogether, this was way easier than matplotlib or d3 and took way less
time. Declarative code is wonderful.

# gnuplot (language?)

![The graph made with GNUplot](img/gnuplot.png)

I basically had to hack together a really weird script in an esoteric language
that I've never used before and will likely never use again. It's probably
wonderful if you get used to using it, but it just didn't really feel right to
me. I'd much prefer to use an actual programming language. Also, making a legend
was awful as usual. This is also super weird but PNG output isn't anti-aliased
so it looks terrible, but SVG output exists and doesn't look terrible (because
it's vectorized).

# Google Sheets (tool)

![The monster which haunts us in our sleep](img/google-sheets.png)

I tried to use a spreadsheet, I really did. I was excited when I saw that Google
Sheets had a bubble chart. I made one. It looks horrific. In google sheets, you
can't change the maximum and minimum bubble size for some reason, which means if
you have a lot of bubbles you can't actually tell what's going on. This seems
kind of dumb because the point of charts is to make lots of data make sense...

I also tried to use Excel, but I don't have it on my computer and the web
version refused to function properly. It somehow crashed on like 300 rows of
data, then refused to insert a bubble chart four times in a row. IDK man.

Hilariously, in spite of all its shortcomings, Google Sheets nearly did
perfect on the checklist:

- [x] x to flipper length
- [x] y to body mass
- [x] color to species
- [x] size to bill length
- [x] semitransparent circles
- [x] don't start scales at 0 (we don't need that negative space)
- [x] axes have reasonable ticks and labels
- [x] the grid
- [ ] the legend (no size, but the size is nonsensical anyways)

# Technical Achievements

- Mouse-over effect in the d3 implementation which shows penguin information

# Design Achievements

- made the marker shapes ellipses whose width is the bill length and whose
  height is the bill depth (d3)
    - apparently bill shape is completely different across species, I didn't
      know that!
    - I tried to do this in altair but it was getting way to complicated
