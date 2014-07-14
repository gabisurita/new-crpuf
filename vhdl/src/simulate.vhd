-- TODO 
-- Define stability as global parameter
-- Joint For generate

library IEEE;
use IEEE.std_logic_1164.all;
use STD.textio.all;


use work.std_logic_textio.all;
use work.txt_util.all;
use work.resources.all;
use work.std_logic_arith.CONV_STD_LOGIC_VECTOR;


entity 	simulate is

end simulate;
 
architecture simulate_arch of simulate is
  signal a:    std_logic := '1';
  signal c:    std_logic ; 
  signal b:    std_logic ; 
  
  signal input_data:       std_logic_vector (1 to 2*matriz_i) ;   
  signal output_result:    std_logic_vector (1 to matriz_i) ;     
     
  
  TYPE time_vector IS ARRAY (1 to 2* matriz_i * (matriz_j)) OF integer;
  TYPE wire        IS ARRAY  ( 1 to matriz_i, 1 to matriz_j)   OF std_logic;
  
  signal x_wire: wire ;
  signal y_wire: wire ;
  signal w_wire: wire ;

  signal atraso_vector: time_vector:=(others=>0);
  
  
  --signals for setup output file print
  signal listen_output:    std_logic:='0' ; 
  signal enable_wr_file_output:    std_logic:='0' ; 
  
  signal number_of_simulation:    integer:=1 ; 


  signal timer_dog:    time:=1 ns; 
  
	signal watch_dog:    time:=now;
  
 
BEGIN  -- circuits of signal_trace
 
 
 linhas: for i in 1 to matriz_i generate
    colunas: for j in 1 to matriz_j generate	
	    w_wire (i,j) <= x_wire (i,j) xor y_wire (i,j);
     end generate colunas;   
end generate linhas;



-- Circuit Generate 

	for1:for j in 2 to matriz_j generate  
		for2:for i in 1 to matriz_i generate                                        	  -- for i = 1->4
			x_wire(i,j)		<= w_wire ((i + (matriz_i/2)) mod (matriz_i) + 1,j-1) 				after (atraso_vector((2*i + (j * matriz_i)) + 1)) * 1 fs;   --    wi+3
			y_wire(i,j)		<= w_wire ((i + ((matriz_i/2) - 1)) mod (matriz_i) + 1,j-1)   after (atraso_vector((2*i + (j * matriz_i)) + 2)) * 1 fs;   --    yi+3 = wi
    end generate for2;
	end generate for1;


-- Input/Output pins

--conecta o primeiro estagio aos pinos de entrada
	entrada: for i in 1 to matriz_i generate   	
	  x_wire (i , 1) <=    input_data (2*i-1) ;
	  y_wire (i , 1) <=    input_data (2*i) ;
	end generate entrada;

--conecta o ultimo estagio aos pinos observados como saida
	saida: for i in 1 to matriz_i generate   	
	  output_result (i) <= w_wire (i , matriz_j);      
	end generate saida;


	read_file: process    -- read file_io.in (one time at start of simulation)
    file my_delay_file    : TEXT;-- open READ_MODE is "atrasos32bits.txt";--"atrasosDevadas.txt";
		file my_stimulus_file : TEXT;-- open READ_MODE is "stimulus.txt";


	  variable delays_file: string( 1 to 20); -- support only 5 decimal digits
	  
    variable my_line : LINE;
    variable my_input_line : LINE;
	  variable stimulus : STD_LOGIC_VECTOR (1 to 2*matriz_i);
	  variable intfromfile : integer;
	  variable mystring: string( 1 to 50*matriz_i*matriz_i*matriz_j); -- support only 2 decimal digits
	  variable string2: string( 1 to 20); -- support only 5 decimal digits
    variable stimulus_string:  string( 1 to 2 * matriz_i); -- support only 2 decimal digits
	  variable i: time:=100 ns;
	  variable x: integer:=1;
	  
	  variable simulacao: integer:=1;
	  variable indice, next_indice, inteiro:integer:=0;
	  variable valorreal:real:=0.0;
	           
	  variable indice_atraso_x, indice_atraso_y:integer:=0;	  
	  variable indice_i: natural;
	  variable deslocamento_nivel: integer;
	  variable temp: integer;  -- a variavel acima so funciona com uma abaixo dela????

    begin
			listen_output <='0'; 
      write(my_line, string'("Running and reading file"));
	  	writeline(output, my_line);
	
   		file_open(my_delay_file,"./data/RPUF_delays/atrasos_RPUF_"  & integer'image(matriz_i) & "x"&integer'image(matriz_j) & "_"&integer'image(individuos)&"_pufs_.txt",read_mode);	

  
			for x in 1 to individuos loop
				str_read(my_delay_file, mystring);  -- read			
				indice :=1;				
           -- disable print for output file
				input_data	<= conv_std_logic_vector(0, 2*matriz_i);  -- define initial value for circuit input     
		
				for var in 1 to 2* matriz_i * (matriz_j) loop -- 2* matriz_i * (matriz_j-1)
				
					next_indice:= str_nextchar (mystring, indice, ' ');				
					for var_zero in 1 to string2'length loop
						string2 (var_zero):= '0';
					end loop;
					for var_str in 1 to next_indice-indice loop
						string2 (string2'length - (next_indice-indice) +var_str):= mystring(indice + var_str-1);
					end loop;
						inteiro:=str_to_int(string2);
						atraso_vector (var)<= inteiro;						
						indice:=next_indice+1;						
				end loop;   -- end 

		
				number_of_simulation <=simulacao;
				simulacao:=simulacao+1;
		
		
				file_open(my_stimulus_file,"./data/Challenges/desafios_"& integer'image(number_of_vector)&"_C_"& integer'image(2*matriz_i) &"_bits.txt",read_mode);
				watch_dog <= now ;
					 
			--file_open(my_stimulus_file,"vetores10bits.txt",read_mode);
				enable_wr_file_output<='0';				
		
				 -- disable print for output file
				for x in 1 to number_of_vector loop  -- Amount challenge lines must be determined 
					
					
					str_read(my_stimulus_file, stimulus_string);  -- read 				   
					stimulus:=   to_std_logic_vector(stimulus_string);
					
					
					input_data	<= stimulus;
					timer_dog  <= now ;	
					listen_output <='1'; 						
					wait for 0.9*base_tempo;

					enable_wr_file_output <= '1';
					
					
					wait for 0.1*base_tempo;					
					enable_wr_file_output <= '0';
				 end loop;
				FILE_CLOSE(my_stimulus_file);	
			
			end loop;
			FILE_CLOSE(my_delay_file);        
			write(my_line, string'("########    Finish simulation at "));
			write(my_line, now);
			writeline(output, my_line);

				         
	    wait; 
	  end process read_file;


	prcs_and: process (output_result)
 		variable line_raw : LINE;
		file raw_output_file   : TEXT open WRITE_MODE is response_file_raw;
	  variable simulacao: integer:=0;

	      begin		
	         if (listen_output = '1') then	
		                          
	          if (simulacao/=number_of_simulation ) then -- Separa o resultado dos desafios com # numerodopuf			   
							write(line_raw, string'("#")); 
							write(line_raw, number_of_simulation); 				   
		          writeline(raw_output_file, line_raw); 
	          	
	          end if;
	          simulacao:=number_of_simulation;      
	        end if;
	        
--	        if (enable_wr_file_output = '1') then 
							write(line_raw, output_result);
						  write(line_raw, string'("  "));
							write(line_raw, (now - watch_dog));
	            writeline(raw_output_file, line_raw);	  
	--        end if;
    end process prcs_and;	


	
	prcs_or: process (output_result,enable_wr_file_output)
    variable my_line, my_line2,my_line3 : LINE;
    variable line_flipflop : LINE;
		variable line_ff_RPUF_2 : LINE;
		
		
		file flipflop_output_file   : TEXT open WRITE_MODE is response_file_rpuf1;--"APUF_32estagios.txt";
		file ff_RPUF_2_output_file : TEXT open WRITE_MODE is  response_file_rpuf2; 
  
    variable last_output_result:    std_logic_vector (1 to matriz_i) := conv_std_logic_vector(0, matriz_i) ;
    variable var_last_output_result:    std_logic_vector (1 to matriz_i) := conv_std_logic_vector(0, matriz_i) ;		
        --variable flipflop:    std_logic_vector (1 to (matriz_i*(matriz_i-1))/2) := conv_std_logic_vector(0, (matriz_i*(matriz_i-1))/2) ;  
				
		variable flipflop: std_logic_vector(1 to (matriz_i*(matriz_i-1))/2) := conv_std_logic_vector(0, (matriz_i*(matriz_i-1))/2);  


    variable ff_RPUF_2:    std_logic_vector (1 to matriz_i*(matriz_i-1)) := conv_std_logic_vector(0, matriz_i*(matriz_i-1)) ;  		
    variable simulacao: integer:=0;
		
		variable aux: integer := 0;	
				
		variable aux1: integer := 0;	
		variable aux2: integer := 0;	

        begin		
						aux1 := 0;
						
						aux2 := 0;
 		       	var_last_output_result:=output_result;
	                              
						if (simulacao/=number_of_simulation ) then -- Separa o resultado dos desafios com # 
							write(line_flipflop, string'("#")); 
							write(line_flipflop, number_of_simulation); 				   
							writeline(flipflop_output_file, line_flipflop); 

							write(line_ff_RPUF_2, string'("#")); 
							write(line_ff_RPUF_2, number_of_simulation); 				   
							writeline(ff_RPUF_2_output_file, line_ff_RPUF_2); 				   
						
		        end if;

              simulacao:=number_of_simulation;
					
   --         for i in 1 to matriz_i loop --
 							for i in 1 to matriz_i loop				
										--if (i=1) then  --*12   23   34   45   56   67   71

	                    	for ii in i+1 to matriz_i loop
	                    			aux1 := aux1 + 1;
--					                if last_output_result (i) /= var_last_output_result (i) then
						                 if last_output_result (i) /= var_last_output_result (i) then
														 if output_result (i) = '1' then  -- pega a borda de subida daquele sinal 
			                  			flipflop(aux1):= var_last_output_result(ii);
    		                 			end if;
    		                 			end if;
--	                    		end if;

												end loop;

                			
                  end loop;

                		
						 for i in 1 to matriz_i loop              		
                    for ii in 1 to matriz_i loop
                    	if ii /= i then
                    		aux2:= aux2 + 1;
				                if last_output_result (i) /= var_last_output_result (i) then
 
                			 	if output_result (i) = '1' then
                    			ff_RPUF_2(aux2):= var_last_output_result((ii));
                    		end if;
                    		end if;

											end if;                    							
	                    end loop;
                    end loop;
               
           --     	end if;
                    --    write(my_line, i); 
                   --     write(my_line, string'("-"));     
        --        end if;
             
        --     end loop; 

             last_output_result := var_last_output_result;
             
 --         else -- update
     --        last_output_result := var_last_output_result;
          
      
         	if (listen_output = '1') then	
       
          if (enable_wr_file_output = '1') then 
		      write(line_flipflop, flipflop);
              writeline(flipflop_output_file, line_flipflop);
            --  writeline(my_output_file, my_line);
			  
			  write(line_ff_RPUF_2, ff_RPUF_2);   
              writeline(ff_RPUF_2_output_file, line_ff_RPUF_2);
	        end if; 		  
          end if;

    end process prcs_or;


  
end architecture simulate_arch; -- end of simulate
