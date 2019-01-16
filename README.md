# Stitch It
Simple utility to create one large screenshot image for pages longer than can fit in the screen.

## Dependencies:
- `python3`
- `opencv3`

## Scripts
- `vid_ocr.py`: takes as input a mobile screen recording video of scrolling down a long page. Outputs a text file with recognized text in video
- `vid_stitch.py`: takes as input a mobile screen recording video of scrolling down a long page. Outputs one long screenshot
- `pic_stitch.py`: takes as input multiple consecutive screenshots (top to bottom) of a long page. Outputs one long screenshot

### Usage:
- `python vid_ocr.py -v my_screen_recording.mp4 -t step -p 50`
- `python vid_stitch.py -v my_screen_recording.mp4 -t target -p 8`
- `python pic_stitch.py -i my_screenshot1.png,my_screenshot2.png,my_screenshot3.png -o output.png`

### Options:
- `--output`/`-o`: output filename (optional). Default: `output.png`
for `vid_stitch.py` only:
- `--video`/`-v`: input video file with screen recording of scrolling down
- '--frame_param_type`/`-t`: which type is the `frame_param` option. Either `target` or `step`.
`step`: size of step in video frames between each sample considered for stitching (optional).
`target`: number of sample frames to target (approximate).

for pic_stitch.py` only:
- `--input`/`-i`: comma delimited (no spaces) input image files. Should be ordered top to bottom

### Example:
| Script               |                           Input                         |                                  Output                            |
| -------------------- | :------------------------------------------------------:| ----------------------------------------------------------------:  |
| `vid_ocr.py`         | ![input screen recording video](assets/input_video.gif) |  5:43 7 |

@ nytimes.com G
= Ebe New York Times =

Sunday, January 13, 2019 SUBSCRIBENOW LOGIN
POLITICAL STANDOFF

 

Trump Confronts the Prospect
of a ‘Nonstop’ War for
Survival

* Questions about whether President Trump is
a Russian agent made clear that the
government shutdown may be just a
preliminary skirmish in this new era of
divided government.

* With Democrats now in charge of the House,
the president faces the prospect of an all-out
political war, our correspondent writes in a
news analysis.

Explaining Trump’s Tweet on Crimes
by Immigrants

Mr. Trump cited an array of statistics to
paint a portrait of widespread criminal
conduct by undocumented immigrants.
Here’s the context behind them.

As Trump Sticks With His Wall, His
Ratings Stay Stuck in Place

The border wall remains popular only with
the president’s base, and shutting down the
government over the issue seems unlikely to
win new fans.

 

Never Old.
Never New.

Get yours >

y

ivi

foreverspin™

V.A. Seeks to Redirect Billions
of Dollars Into Private Care

- For individual veterans, private care could
mean shorter waits, more choices and fewer
requirements for co-pays.

* But critics say the current veterans’ health
care system could be starved of resources.

Students in Rural America

Ask, ‘What Is a University
Without a History Major?’

* Financial and enrollment woes at schools
like the University of Wisconsin-Stevens
Point have led to a scramble for fixes.

* One possibility: dropping traditional liberal
arts degrees in favor of career-focused
programs.

Jan. 12|
| `vid_stitch.py`      | ![input screen recording video](assets/input_video.gif) | ![output generated screenshot image](assets/output_screenshot_from_video.png) |
