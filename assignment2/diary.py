
PROMPT_START = "What happened today?"
PROMPT_CONTINUE = "What else?"
ALLDONE = "done for now"
INTRO = "Enter what you did today at each prompt. Enter '" + ALLDONE + "' when finished."
OUTFILE = "diary.txt"
try: 
    with open(OUTFILE, "w") as f:

        print (INTRO)
        val = input(PROMPT_START)   
        while (val != ALLDONE):
            f.write(val + "\n")
            val = input (PROMPT_CONTINUE)

        f.close()
        print ("Diary written to:", OUTFILE)
except KeyboardInterrupt:
    # Code to handle the interrupt
    print("Program interrupted by user.")
    
except Exception as e:
    print ("foo")
    print(f"An error occurred: {e}") 