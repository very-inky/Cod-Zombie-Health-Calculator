# Cod-Zombie-Health-Calculator
This program is written in Python. To run it you will need Python installed on your computer, which can be obtained here: https://www.python.org/
Not sure if you have python? You can search your computer for it, or in your terminal or command prompt you can type "py" or "python" as a command. If it's installed it will show you what version is installed.

Simply run the program and follow the prompts.


This python based program is meant to be an easy to use tool for finding out zombies health given any round. These values should always hold true as all the Black Ops Zombies games use the same 'default' values.

The use of the program should be pretty easy and straighforward. There are two modes, Default and Custom.

In default, you use the vanilla (unmodified) health scaling for the zombies modes to find out given any round, what their health will be at that round.

In custom, you can specify all the parameters, useful if you are trying to mod and rebalance zombie health for mods or a .gsc
You can also specify a health cap if you'd like. You will be shown what round the health cap will be triggered, as well as the ending health if it were left uncapped.


Zombie Health Scales as follows.
Round 1: Starting HP
Rounds 2-9: That Starting HP has a flat value added to it each round.
Round 10: The HP is multiplied by 1.1 each round. This is exponential.

Expressed as:
Round 1:
  Health = Start Health
 Round 2-9:
  Health = Start Health + Health Increase * (round - 1)
 Round 10+:
  Health = (Start Health + Health Increase * (round - 1)) * Health Multiplier ^(round - 10)
  
  If you have any questions or trouble about this tool specifically, you can add me on Discord @ VeryInky#0001
