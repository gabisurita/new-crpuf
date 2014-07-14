library ieee;

use ieee.std_logic_1164.all;
PACKAGE resources IS

 constant base_tempo :    time:= 100 ns ;--500; --individuos

 constant matriz_i	 : natural := 3 ; -- linhas (impar)
 constant matriz_j	 : natural := 3 ; -- colunas
 
 constant number_of_vector:    integer:= 16 ;--500; --quantidade de estimulos
 constant individuos:				   integer:= 1000 ;--500; --individuos
 
 constant response_file_rpuf1:  string  := "./data/PUF_Response/CRPUF1_response_PUF_"&integer'image(matriz_i)&"x"&integer'image(matriz_j)&"_bits_"&integer'image(individuos)&"_pufs.txt";
 constant response_file_rpuf2:  string  := "./data/PUF_Response/CRPUF2_response_PUF_"&integer'image(matriz_i)&"x"&integer'image(matriz_j)&"_bits_"&integer'image(individuos)&"_pufs.txt"; 
 constant response_file_raw:	  string  := "./data/PUF_Response/RAW_response_PUF_"&integer'image(matriz_i)&"x"&integer'image(matriz_j)&"_bits_"&integer'image(individuos)&"_pufs.txt"; 
 
END resources;
