# -c   for command line mode
# -t   for Time resolution limit
# -do "<command>"  to execute <command> on startup; Can also be a text file


/root/altera/13.0sp1/modelsim_ase/bin/vsim -c -t fs work.simulate -do "run -all; exit;"

