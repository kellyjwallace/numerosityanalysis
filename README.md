# numerosityanalysis
This set of scripts is designed to take a video of a numerosity trial and:
1. determine the location of the fish (kellyTracker.py) that gets output as a csv file with th ecolumns x, y, and frame 
2. fill in any gaps in the csv file by interpolating on frames where the fish was not visible to the tracker (reinterpolateflip.py)
3. allow the user to draw zones of interest on the video (rectangle.py)
4. for each frame, determine which zone the fish was in (determinezone.py)

Below is an example of the commands you would enter in the terminal:
----------------------------------------------------
cd /home/ian/Desktop/kellynumerosityanalysis/scripts

python kellyTracker.py -i gambusia_3_328_female_Harlow_8_2_5_10_50_right_R.mkv -n gambusia_3_328_female_Harlow_8_2_5_10_50_right_R -f 25

python reinterpolateflipv2.py -t gambusia_3_328_female_Harlow_8_2_5_10_50_right_R.csv

python rectangle2.py -b gambusia_3_328_female_Harlow_8_2_5_10_50_right_R_background.jpg

---
PRESS ESC after you draw a box!
tankedge
topmirror
bottommirror
leftscreen
rightscreen
topthigmo
bottomthigmo
---

python determinezone.py -f updated_gambusia_3_328_female_Harlow_8_2_5_10_50_right_R.csv -c mydata.csv
------------------------------------------------------
