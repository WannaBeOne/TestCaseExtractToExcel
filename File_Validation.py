filename = "login.side"
i_count = 0
line_cmd = " "
tuple_cmd = ('commands', 'id', 'command', 'target', 'targets', 'value', '}]')
tuple_len = len(tuple_cmd)
var_cmd = ""
cmd_index = 0
x = 0
file_var = open(filename, 'r')
print(f'"tuple length :" {tuple_len}')
for line in file_var:
    # print(line)
    # i_count = i_count + 1
    # print(i_count)
    # result_line = line.find("commands")
    # var_cmd = tuple_cmd[0]
#    print(var_cmd)
    for x in range(tuple_len):
        print(x)
        var_cmd = tuple_cmd[x]
        print(var_cmd)

        #if line.find(var_cmd) != -1:
            #i_count = i_count + 1
            #cmd_index = i_count
            #message_line = f'{line} + "line" + {i_count}'
            #if line_cmd == " ":
                #line_cmd = line
        #else:
                #line_cmd = line_cmd + '\n' + line
    #        #print(message_line)
            #print(line_cmd)

        #elif line.find("}],") != -1:
            #break

        #else:
            #i_count = i_count + 1
            #if i_count > cmd_index:
                #print(i_count)
                #if line.find(var_cmd) != -1:
                    #if line_cmd == "":
                        #line_cmd = line
        #else:
                        #line_cmd = line_cmd + '\n' + line
                    #break

        #       else:
        #if(line_cmd == ""):
                    #    line_cmd = line
                    #else:
                    #    line_cmd = line_cmd + '\n' + line
        #if (x + 1) == tuple_len:
            #break
        file_var.close()

#print(line_cmd)
