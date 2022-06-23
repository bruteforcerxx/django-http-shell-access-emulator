print("""
CMD command	Description	Windows version	 

bitsadmin	Creates and monitors downloads and uploads.	10/8/7/Vista	 

break	Interrupts Ctrl + C checking in DOS, allowing you to stop processes in the old operating system. Only available for compatibility reasons in Windows.	All Win/DOS	 

call	Calls a batch file within another batch file. The command has no effect if entered directly into CMD instead of in a batch file.	All Win/DOS	 

cd	Displays the current directory and lets you switch to other directories. With the parameter /D plus drive and path specification, you can also switch drives. Use cd.. to switch to a higher directory (has the same function as the chdir command).	All Win/DOS	 

chcp	Changes the current code page (character set table) or shows the page count of the current code page.	All Win/DOS	 

chdir	Displays the current directory and lets you switch to other directories. With the parameter /D plus drive and path specification, you can also switch drives. Use chdir.. to switch to a higher directory (has the same function as the cd command).	All Win/DOS	 

choice	Creates a selection list: typical example is the selection of yes (Y) or no (N), which is created with /C YN. With the parameter /M you can add an explanatory message for the user.	All Win (not XP)/DOS	 

clip	Forwards the result of a command to the clipboard. For example, you can copy the directory structure (dir	clip) or the content of a file (clip < filename) to the clipboard.	10/8/7/Vista

cls	Clears the content of the screen.	All Win/DOS	 

cmd	Starts CMD.EXE.	10/8/7/Vista/XP	 

color	Changes the background (first value) and text color (second value) of the command prompt. The color lies between 0 (black) and F (white).	10/8/7/Vista/XP	 

command	Starts CMD.COM.	32-bit/DOS	 

date	Displays the current date and allows you to change it. With the parameter /T the date is shown without the option to change.	All Win/DOS	 

debug	Starts debug, a program that can test and modify programs within the command prompt.	32-bit/DOS	 

dir	Displays all folders and files within the current directory. You can restrict the output by attributes (/A), simplify the list (/B), or display all subdirectories and their files (/S).	All Win/DOS	 
doskey	Creates macros, recalls commands, and edits command input.	All Win/DOS
	 
dosshell	Opens the DOS shell, a graphical file management tool. In Windows, the DOS shell is replaced by Windows Explorer.	95/DOS	 
echo	Displays a message and is mainly used within scripts and batch files.	All Win/DOS	 

edit	Starts the MS-DOS editor, with which you can create text files.	32-bit/DOS	 

edlin	Creates and edits text files within the command prompt.	32-bit/DOS	 

exit	Ends CMD.EXE or CMD.COM.	All Win/DOS	 

fasthelp	Displays helpful information about commands.	DOS	 

fastopen	Writes the position of a program into a specified list, which is in the working memory and should accelerate the start of programs.	32-bit/DOS	 

find	Searches through a file or multiple files for a particular character sequence. If you only want to know how frequently the word or phrase occurs, use the /C parameter. With the extension /I the command ignores upper- and lower-case in the search.	All Win/DOS	 
findstr	Finds character sequences in one or multiple files. It gives you more options when compared to the find command: you can search for files that contain various terms or with /C search for an exact word order.	10/8/7/Vista/XP	 
forcedos	Starts a program in the MS-DOS partial system, in case it’s not directly recognized by Windows XP as a DOS program.	XP (32-bit)	 
graftabl	Enables the option to use extended characters of a specific code page in graphics mode.	32-bit/DOS	 

graphics	Starts a program that can print graphics.	32-bit/DOS	 

help	Displays help text for a specific command (you can also use the /? command).	All Win/DOS	 

kb16	Changes the country settings of the keyboard for DOS programs (only included in Windows for compatibility reasons. Replaces the old command keyb).	32-bit	 

keyb	Changes the country settings of the keyboard for DOS programs (only included in Windows for compatibility reasons. Replaced by kb16 in newer Windows versions).	98/95/DOS	 

logoff	Logs the user out of Windows. Also allows you to end sessions on servers.	10/8/7/Vista/XP	 

lpq	Displays the status of a printer queue for computers that use a “line Printer Daemon” (LPD). (To use the command in Windows 10, 8, 7, or Vista, the LPD print service and the LPR port monitor have to be enabled first).	All Win
	 
lpr	Sends a file to a computer that uses a line printer daemon (LPD). To use the command in Windows 10, 8, 7, or Vista, the LPD print service and LPR port monitor have to be enabled first.	All Win	 

md	Creates a new directory on the specified path. If directories don’t already exist on the path, md creates them automatically (you can also use the mkdir command).	All Win/DOS	 

mkdir	Creates a new directory on the specified path. If directories don’t already exist on the path, mkdir creates them automatically (you can also use the md command).	All Win/DOS	 
more	Outputs the content of a file (for example, a text file) by the page. You can also use the command to split the output of another command into pages.	All Win/DOS	 
msg	Sends a message to another user. You can write the username into the command or create files in which usernames are saved. The files can then be included in the command with @filename.	10/8/7/Vista/XP	 
nlsfunc	Provides country-specific information for language support.	32-bit/DOS	 
ntbackup	Runs backup services directly from the command line or as part of batch or script files.	XP	 
path	Creates and displays the path for searching executable files.	All Win/DOS	 
pause	Pauses execution in batch files and scripts. The user is then prompted in a message to continue by pressing a key.	All Win/DOS	 
popd	Changes to the folder saved by the pushd command. The command is mainly part of batch files and scripts.	10/8/7/Vista	 
print	Prints a text file. The device to be used for printing has to be specified.	All Win/DOS	 
prompt	Changes the display of the command prompt.	All Win/DOS	 
pushd	Saves a specific path into a script or batch file. You can change to this directory with popd.	10/8/7/Vista/XP	 
qbasic	Starts qbasic, a program environment based on the BASIC programming language.	98/95/DOS	 
rd	Deletes a directory. This must not contain any files, even hidden ones. You can delete an entire directory tree with the /S parameter (you can also use the rmdir command).	All Win/DOS	 
rem	Writes comments in batch and script files that aren’t taken into account when executing.	All Win/DOS	 
rmdir	Deletes a directory. This must not contain any files, even hidden ones. You can delete an entire directory tree with the /S parameter (you can also use the rd command).	All Win/DOS	 
runas	Allows a user to run commands with the rights of another user. For example, you can run a command as an administrator from a normal user account as long as you know the password.	10/8/7/Vista/XP	 
scandisk	Starts Microsoft ScanDisk. The program searches data carriers for errors.	98/95/DOS	 
schtasks	Sets the execution of specified programs and commands for a specified point in time. You can create, delete, change, and display all scheduled tasks.	10/8/7/Vista/XP	 
set	Displays environmental variables of CMD.EXE and lets you configure them.	All Win/DOS	 
shift	Moves variables within batch files and scripts.	All Win/DOS	 
shutdown	Shuts down the computer (/s), triggers a restart (/r), or logs the user out (/l). A graphical user interface is displayed if you enter the parameter /I as the first option in the command.	10/8/7/Vista/XP	 
sort	Lists out data (from a file or command) and outputs it again sorted – directly in the command prompt, in a new file, or in another output.	All Win/DOS	 
start	Opens a new command prompt window in which you can run a specific program or command.	All Win	 
subst	Assigns a drive letter to a path to create a virtual drive.	All Win/DOS	 
taskkill	Ends one or more running tasks. You either have to specify the process ID (PID) or image name.	10/8/7/Vista	 
tasklist	Lists all running processes – also on remote computers, if desired. The process ID also has to be specified, which is required for the taskkill command, for example.	10/8/7/Vista/XP	 
time	Displays the current time and allows it to be changed. If the parameter /T is entered, the command prompt only shows the time and offers no option to directly change it.	All Win/DOS	 
timeout	Stops a process for a specified time. The command Is used in batch files and scripts. If you use the /NOBREAK parameter, the command ignores any keyboard input.	10/8/7/Vista	 
title	Changes the title of the command prompt. Spaces are allowed, but not all special characters such as a slash, for example, because they may be interpreted as instructions for a parameter.	All Win/DOS	 
tree	Graphically displays the directory structure of a drive or path. With the /F parameter, all files in the folders are also listed out. /A also ensures that only ASCII characters are used for the graphical representation. The command takes into account all subdirectories starting from the given path. If you don’t enter a path, the current folder is used as the output.	All Win/DOS
	 
type	Displays the content of a text file.	All Win/DOS	 

tzutil	Displays the currently set time zone (/g) or changes it (/s). The parameter /l helps determine the valid time zones.	10/8/7	 

ver	Displays the current version number of Windows or MS-DOS.	All Win/DOS	 """)
