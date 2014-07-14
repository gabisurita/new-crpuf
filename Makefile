# Makefile
# Projeto   : Puf Simulation
# Módulo    : Makefile
# Data      : 20/09/2012 - Jefferson Rodrigo Capovilla
# Descrição : Makefile

# Nome do módulo
MODULE = simulate 

.PHONY: compile_idea_lib_modelsim
compile_idea_lib_modelsim:
	./scripts/modelsim_do/create_idea_lib.do

.PHONY: compile_module_modelsim
compile_module_modelsim:
	./scripts/modelsim_do/create_module.do

.PHONY: simulate_modelsim
simulate_modelsim:
	./scripts/modelsim_do/simulate_tb.do

.PHONY: vsim
vsim: compile_idea_lib_modelsim compile_module_modelsim simulate_modelsim

.PHONY: vsim-launch
vsim-launch: compile_idea_lib_modelsim compile_module_modelsim
	echo "There's no waveform for this simulation."
	echo "Simply run 'make vsim'"

.PHONY: vsim-clean
vsim-clean: 
	rm -rf ./lib/* modelsim.ini transcript vsim.wlf
	
##############################################################################
