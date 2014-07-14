
# Create Module

/root/altera/13.0sp1/modelsim_ase/bin/vlib       ./lib/work;
/root/altera/13.0sp1/modelsim_ase/bin/vmap  work ./lib/work;

# Adding files to library work

/root/altera/13.0sp1/modelsim_ase/bin/vcom -work work -2002 -lint ./vhdl/src/resources.vhd
/root/altera/13.0sp1/modelsim_ase/bin/vcom -work work -2002 -lint ./vhdl/src/std_logic_arith.vhd
/root/altera/13.0sp1/modelsim_ase/bin/vcom -work work -2002 -lint ./vhdl/src/std_logic_textio.vhd 
/root/altera/13.0sp1/modelsim_ase/bin/vcom -work work -2002 -lint ./vhdl/src/txt_util.vhd 

# Create TB 
/root/altera/13.0sp1/modelsim_ase/bin/vcom -work work -2002 -lint ./vhdl/src/simulate.vhd
