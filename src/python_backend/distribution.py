#if the summary is being returned to different interfaces (web, cli, file, text, email, etc)
#this module can be used to retain the summary information and then send send a structured output to each interface
#i.e. user requested a detailed summary for CLI interface, the text will be delimited with /n chars every 80 characters

#this might be better handled within each interface module at a small scale