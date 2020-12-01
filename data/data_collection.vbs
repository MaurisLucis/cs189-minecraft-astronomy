Set objShell = WScript.CreateObject("WScript.Shell")

'Note this assumes the name of the Minecraft window is 1.12.2, which should
'be true by default for default versions of Minecraft when playing on v1.12.2.
objShell.AppActivate("Minecraft 1.12.2")

'Set these to the coordinates you want your character to be at for the screenshots.
X_COORD = ...
Y_COORD = ...
Z_COORD = ...

'Your Minecraft IGN.
PLAYER_NAME = ...
'Python executable
PYTHON = ...
'Path to renaming script, e.g. [...]/cs189-minecraft-astronomy/data/rename_file.py
RENAME_SCRIPT = ...

Dim TIME, YAW, PITCH

For YAW = -180 to 170 Step 20
    For PITCH = -90 to 30 Step 15
	objShell.sendKeys "t"
        WScript.Sleep 100
        objShell.sendKeys "/tp " & PLAYER_NAME & " " & X_COORD & " " & Y_COORD & " " & Z_COORD & " " & YAW & " " & PITCH
        WScript.Sleep 100
        objShell.sendKeys "{ENTER}"
	WScript.Sleep 100
        For TIME = 0 to 23999 Step 240
            objShell.sendKeys "t"
            WScript.Sleep 100
            objShell.sendKeys "/time set " & TIME
            WScript.Sleep 100
            objShell.sendKeys "{ENTER}"
            'Wait a bit, since the game can lag on this command, throwing off the data.
            WScript.Sleep 1000
            'Take a screenshot.
            objShell.sendKeys "{f2}"
            'Wait some more, since it takes a while for Minecraft to process this and write the screenshot PNG file.
	        WScript.Sleep 2000
	        objShell.Run PYTHON & " " & RENAME_SCRIPT & " --pitch " & PITCH & " --yaw " & YAW & " --ticks " & TIME, 0, True
	    Next
    Next
Next
