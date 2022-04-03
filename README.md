# Final-Project-CSE210
hello guys 

Team Name:
The Best Team 7 Winter 2022

Team Members:
Alvaro
Martin
Samuel
Gunnar

Game Name:
Battle Tanks


Game Function and Flow:
1.	Start Menu
-	A background image and epic  melody, and a button to start.
2.	Controls
-	Background image, instruction, and controls guide. 
-	Player 1: A, S, D W, and H buttons.
-	Player 2: 4, 5, 6, 8 and + buttons..
    -	Alternatively: 
        -	WASD and Q for P1 and,
        -	IJKL and U for P2 
        -	Suggested because my keyboard does not have a number pad and those controls would be awkward*
3.	The Battle
-	Generate
    -	the Map with walls, 
    -	Map is a background image, 
    -	Destroyable walls are generated semi-randomly using hundreds (or at least dozens) of images grouped side by side
-	Player’s Tanks, 
    -	Each controlled by their proper control scheme
    -	can move forward and backward, and turn their angles left or  right.
    -	Tanks can shoot an unlimited number of bullets (that disappear after collision, make disappear after flying off screen too, or have them wrap around the screen, that would be interesting!)
    -	After one player hits another, they get a point and both player’s tanks come back to their initial location.
-	Each Player’s Score,
    -	Score needed to win is 5 points or hits. 
-	3 buttons
    -	(Help: Shows Controls image again)
    -	(Pause: All games need a pause)
    -	(Quit: All games need a quit too)
    -	We could work all of this into a single “Pause Menu” but probably won’t unless time permits
-	A different melody during the battle, 
    -	continues even when tanks reset themselves
4.	The Winner
-	A background image (ends display of everything else)
    -	A Gold medal
    -	Player’s name who won
    -	Play again option (If we get that far)
-	Music Changes to candy shop or chill elevator groovy music




Priorities: 
1.	The game itself, so scene 3, 
2.	Then the title, controls, and winner screens, so scenes 1, 2, and 4.
3.	Lastly, the help buttons in the game as part of scene 3 again









Notes: To-do list
The Branch of the main file uses Alvaro's handy formular to get the tanks turning and rotating and shooting closer to how we originally envisioned.
- but how do we rotate on the center point, instead of top left origin?
- why do the bullets cause a crash when they run into more than one brick at a time. The batter game had several bricks dissapear in a single go, and I never saw the could not remove actor "x" error like we are getting here. 
- How to display the winner screen after 5 points is reached?
