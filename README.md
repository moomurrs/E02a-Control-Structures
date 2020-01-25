
# E02a-Control-Structures

Let's start experimenting with some Python code! This is a set of exercises for MSCH-C220; they should give you the tools to help build your first game.
 
*If you wish your exercise to be graded, please edit the LICENSE file (add the current year and your name).*

Edit README.md to answer the following questions:

- Open main01.py. Before running it, what do you expect this program to do?
  Answer: I expect the program to prompt me what my favorite color is and store the string value in nothing. It will also say if my Python is less than 3.7.
  - Now right click on the main1.py window and select “Run Python File in Terminal”. Click in the bottom panel, and answer the question. Describe what happened.
    Answer: The program asked what my favorite color is and I entered 'blue.' It then terminated. 
  - What do you think the program did with what you typed in answer to the question?
    Answer: The program took my input but did not store it or use it.
- Open main02.py. Before running it, describe how this is different than main01.py.
  Answer: This is different because my input it stored in a variable called color and it is then printed to terminal using print().
  - What do you think the color = input() will do?
    Answer: It stores my input string into color.
  - Run the program in the terminal and answer the question. Did the program do what you expected?
    Answer: Yes, it did. It printed back my input string.
- Open main03.py. Before running it, describe how this is different than main02.py.
  Answer: It is different because there is program flow control based on my input.
  - What is happening on lines 9–12?
    If my input is "Red", it prints out "Correct." For any other string values, it prints out "Sorry, try again."
  - Why are lines 10 and 12 indented?
    Answer: They are indented because the statement in 10 is executed if line 9 is true. Likewise, statement 12 is executed is line 9 is false.
  - Run the program and answer the question. What happens if you don’t capitalize Red?
    Answer: If I don't capitalize, the program, the program executes the else portion and prints "Sorry, try again."
  - What does this tell you about "color"?
    Answer: This tells me that color is a String variable that is case sensitive.
- Open main04.py. Before running it, describe how this is different than main03.py.
  Answer: It's different because the if condition relaxes the requirements so both "Red" and "red" triggers true.
  - What problem is this trying to solve?
    Answer: It's trying to solve the case-sensitivety issue by being more relaxed.
  - Run the program and answer the question. What happens if you use some other capitalization scheme (i.e., “RED” or “reD“)?
    Answer: The if condition becomes false because "RED" and "reD" aren't taken into consideration inside the if condition.
- Open main05.py. What do you expect line 9 to do?
  Answer: I expect line 9 to lower-case the string variable color.
  - What problem is it trying to solve?
    It solves the case-sensitivity issue.
  - Run the program and answer the question. What happens if you add spaces before or after the word (i.e., “ RED “ or “ red”)?
    Answer: The if condition becomes false because "RED" and " RED" are two different Strings.
 - Open main06.py. How is line 9 different than in main05.py?
   Answer: It's different because the input color is stripped of whitespaces and then turned to lower-case.
   - What would you guess .strip() is doing?
     Answer: .strip() removes the String of all whitespaces. 
   - Run the program and answer the question. Is there another way of writing “red” that will break this logic?
     Answer: Putting whitespaces in between red like "r e d" breaks the logic.
 - Open main07.py. Before running this program, how do you expect this to be different than main06.py?
   Answer: It's different because 3 different outcomes are possible: correct, close, or sorry.
   - What is happening on line 12?
     Answer: A second chained if condition is checked if the first condition fails.
   - Run the program and answer the question.
 - Open main08.py. What is the purpose of line 9?
   Answer: The loop runs until the user inputs "red".
   - Why are lines 10–17 indented?
     Answer: They are indented because they are under the control of while loop on line 9.
   - Run the program. What would happen if line 10 were moved before line 9 (and no longer indented)?
     Answer: If line 10 were removed before line 9, the while loop can no longer update user input. This causes infinite loop inside while if the input isn't red. If the input is red, then the program terminates.
   - Make that change and run the program again. (To end any Python program, you can type ctrl-c)
 - Open main09.py. What is happening on line 13?
   Answer: count is being incremented by 1.
   - What is the purpose of “count”?
     Answer: count keeps track of user's tries. Each input increments count.
   - What is happening on line 22?
     Answer: There is no line 22. Line 21, however, is replacing {} with the count. 
   - Run the program.
 - *Extra credit:* open main10.py. Add a comment to each line describing what it   is doing (a comment follows a pound sign [#]).
   DONE
 - *Extra credit:* open main11.py. What is happening on lines 6-11?
   Answer: Line 6-11 define a function that return a String.
   The function choose_color(last_color) randomly chooses a String from a list that isn't an argument match. The function always returns a new color String that doesn't match whatever is called with it.
  
Commit your changes and push them back to the repository.


---

The grading criteria will be as follows:
 
[1 point] Repository contains a description of the project in README.md

1 point will be awarded for answering the questions associated with each of the files

10 points total (+2 points extra credit)
