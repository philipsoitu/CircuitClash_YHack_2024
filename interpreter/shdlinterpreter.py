from itertools import product
from tabulate import tabulate
def runfunction(gatecode,variables,gateparams,line,gatestack,setvars,gateparamstypes):

    gateunset = set()
    gateset = set()
    operators = {"AND", "OR", "NOT","XOR"}
    parts = line.split(" ")

    op, operands = parts[0], parts[1:]
    parammatch = {key: value for key, value in zip(gateparams[op], operands)}


    if op in gatestack:
        raise Exception(f"Cannot Recursively call functions")
    gatestack.add(op)


    if len(gateparams[op]) == len(operands):
        for input in gateparamstypes[op]["input"] :
            if parammatch[input] not in setvars:
                print(input)
                raise Exception(f"Immutable")
            else: 
                gateset.add(input)
        for output in gateparamstypes[op]["output"]:
            if parammatch[output] in setvars:
                print(output)
                raise Exception("Immutable")
            else:
                gateunset.add(output)
        tempvariables = {}
        for params in set(parammatch):
            tempvariables[params] = variables[parammatch[params]]
        for gate_line in gatecode[op]:
            gate_parts = gate_line.split(" ")
            if gate_parts[0] in ["WIRE"]:

                tempvariables.setdefault(gate_parts[1], 0)
                gateunset.add(gate_parts[1])
            elif gate_parts[0] in ["INPUT", "OUTPUT"]:
                pass
            elif gate_parts[0] in operators:
                temp_op, temp_operands = gate_parts[0], gate_parts[1:]
                tempvariableset = set(tempvariables)
                print(operands)
                print(tempvariableset)
                if set(temp_operands).issubset(tempvariableset):
                    print(gate_line)
                    if temp_op == "AND":
                        if temp_operands[2] not in gateset:
                            tempvariables[temp_operands[2]] = tempvariables[temp_operands[0]] & tempvariables[temp_operands[1]]
                            gateset.add(temp_operands[2])
                        else: 
                            
                            raise Exception(f"Cannot change wire or input once set. \n Verify line {gate_line}")
                    elif temp_op == "OR":
                        if temp_operands[2] not in gateset:
                            tempvariables[temp_operands[2]] = tempvariables[temp_operands[0]] | tempvariables[temp_operands[1]]
                            gateset.add(temp_operands[2])
                        else: 

                            raise Exception(f"Cannot change wire or input once set. \n Verify line {gate_line}")
                    elif temp_op == "XOR":
                        if temp_operands[2] not in gateset:
                            tempvariables[temp_operands[2]] = tempvariables[temp_operands[0]] ^ tempvariables[temp_operands[1]]
                            gateset.add(temp_operands[2])

                        else: 
                            raise Exception(f"Cannot change wire or input once set. \n Verify line {gate_line}")
                    elif temp_op == "NOT":
                        # Applying bitwise NOT to variables[operands[0]] and making sure it's in [0,1]
                        if temp_operands[1] not in gateset:
                            tempvariables[temp_operands[1]] = ~tempvariables[temp_operands[0]] & 1
                            gateset.add(temp_operands[1])
                        else: 
                            
                            raise Exception(f"Cannot change wire or input once set. \n Verify line {gate_line}")
                else:
                    uncreatedvars = []
                    for operand in temp_operands:
                        if operand not in tempvariables:
                            uncreatedvars.append(operand)
                    raise Exception(f"Variable operands called before created. \n Verify line {gate_line}. Operand is {uncreatedvars}")
            elif gate_parts[0] in gatecode:
                print("ENTERING " + gate_line)
                runfunction(gatecode,tempvariables,gateparams,gate_line,gatestack,gateset,gateparamstypes)
                print("EXITING " + gate_line)

        for temps in tempvariables:
            if temps in parammatch:
                if parammatch[temps] in variables:
                    variables[parammatch[temps]] = tempvariables[temps]         
    else: 
        raise Exception(f"Gate parameters do no match with definition. \n Verify line {line}")
    gatestack.remove(op)
    


def shdl_interpreter(shdl_code, input_values,output_vars):
    # Split the code into lines and initialize a dictionary for variable storage
    lines = shdl_code.strip().split("\n")
    variables = {**input_values}  # Initialize variables with input values
    unsetvars = set()
    setvars = set()
    for output_var in output_vars:
        variables[output_var] = 0
        unsetvars.add(output_var)
    for input_value in input_values:
        setvars.add(input_value)


    operators = {"AND", "OR", "NOT","XOR"}

    
    gatecode = {}
    gateparams = {}
    gateparamstypes = {}
    inGate = False
    gatename = ""
    # PreParse for Gates
    linecount = 1
    reducedlines = []
    for line in lines:
        parts = line.split()
        # Ensure parts is not empty
        if not parts:
            linecount+=1
            continue
        if parts[0] == "STARTGATE" and not inGate:
            inGate = True
            gatename = parts[1]
            gatecode[gatename] = []
            gateparams[gatename] = []
            if len(parts[2:]) % 2 == 0:

                params = parts[2:]
            
            else: 
                raise Exception("Invalid parameters")
            i = 0
            gateparamstypes[gatename] = {"input": [], "output": []}

            while i < len(params):
                if params[i] == "INPUT":
                    gatecode[gatename].append(params[i] + " " + params[i+1])
                    gateparamstypes[gatename]["input"].append(params[i+1])
                    gateparams[gatename].append(params[i+1])

                elif params[i] == "OUTPUT":
                    gatecode[gatename].append(params[i] + " " + params[i+1])
                    gateparamstypes[gatename]["output"].append(params[i+1])
                    gateparams[gatename].append(params[i+1])
                else:
                    raise Exception("INVALID INPUT PARAMETER TO FUNCTION")
                i+=2



                
        elif parts[0] == "ENDGATE" and inGate:
            inGate = False
        elif parts[0] == "MAKEGATE" and inGate:
            raise Exception(f"Cannot MAKEGATE Inside MAKEGATE. \n Verify line {linecount}")
        elif parts[0] == "ENDGATE" and not inGate:
            raise Exception(f"Cannot ENDGATE outside MAKEGATE. \n Verify line {linecount}")
        elif inGate:
            line = ""
            first = False
            for elements in parts:
                if first == False:
                    first = True
                    line+= (elements)
                else:
                    line+= (" " + elements)

            gatecode[gatename].append(line)

        else: 
            reducedlines.append(line)
        linecount+=1

    if inGate:
        raise Exception(f"Unclosed Gate")
    
    for gatelinescode in gatecode:
        print(gatelinescode)
        for each in gatecode[gatelinescode]:
            print(each)

    vardeclared = set()
    lines = reducedlines
    linecount = 0
    # Parse and execute each line

    for line in lines:

        parts = line.split()
        if not parts:
            linecount+=1
            continue # Skip empty lines or lines that don't split into parts
        if parts[0] in ["WIRE"]:
            variables.setdefault(parts[1], 0)
        elif parts[0] in ["INPUT", "OUTPUT"] and parts[1] not in set(variables):
            raise Exception(f"Cannot create input that is not predefined. \n Verify line {line}")
        elif parts[0] in operators:
            # Perform operations
            op, operands = parts[0], parts[1:]
            variableset = set(variables)
            if set(operands).issubset(variableset):
                if op == "AND":
                    if operands[2] not in setvars:
                        variables[operands[2]] = variables[operands[0]] & variables[operands[1]]
                        setvars.add(operands[2])
                    else: 
                        raise Exception("Cannot change wire or input once set")
                elif op == "OR":
                    if operands[2] not in setvars:
                        variables[operands[2]] = variables[operands[0]] | variables[operands[1]]
                        setvars.add(operands[2])
                    else: 
                        raise Exception("Cannot change wire or input once set")
                elif op == "XOR":
                    if operands[2] not in setvars:
                        variables[operands[2]] = variables[operands[0]] ^ variables[operands[1]]
                        setvars.add(operands[2])

                    else: 
                        raise Exception("Cannot change wire or input once set")
                elif op == "NOT":
                    # Applying bitwise NOT to variables[operands[0]] and making sure it's in [0,1]
                    if operands[1] not in setvars:
                        variables[operands[1]] = ~variables[operands[0]] & 1
                        setvars.add(operands[1])
                    else: 
                        raise Exception("Cannot change wire or input once set")
            else:
                uncreatedvars = []
                for operand in operands:
                    if operand not in variableset:
                        uncreatedvars.append(operands)
                raise Exception(f"Variable operands called before created. \n Verify line {linecount}: \n {line}") 
        elif parts[0] in gatecode:
            gatestack = set()
            print("ENTERING " + line)
            runfunction(gatecode,variables,gateparams,line,gatestack,setvars,gateparamstypes)
            print("EXITING " + line)


        linecount+=1
    # Extract and return the results for outputs only
    outputs = {k: v for k, v in variables.items() if (k in output_vars or k in input_values)}
    return outputs

def shdltruthtable(shdl_code):
    #inputoutputparse
    lines = shdl_code.strip().split("\n")
    inputvars = []
    outputvars = []
    for line in lines:
        parts = line.split()
        if not parts:
            continue
        if parts[0] in ["INPUT"]:
            inputvars.append(parts[1])
        elif parts[0] in ["OUTPUT"]:
            outputvars.append(parts[1])
        # Generate all possible input combinations
    num_inputs = len(inputvars)
    input_combinations = list(product([0, 1], repeat=num_inputs))
    truth_table = [dict(zip(inputvars, combination)) for combination in input_combinations]
    for idx,rows in enumerate(truth_table):
        result = shdl_interpreter(shdl_code, rows, outputvars)
        truth_table[idx]= {**truth_table[idx],**result}
    combinedlist = inputvars + outputvars
    table_data = [[row[var] for var in combinedlist] for row in truth_table]
    print(tabulate(table_data, headers=combinedlist, tablefmt='pretty'))


            


# Define the SHDL code
shdl_code = """
INPUT A
INPUT B
OUTPUT S
OUTPUT C
WIRE T1
WIRE T2

STARTGATE MYXOR INPUT X INPUT Y OUTPUT Z

    WIRE T1
    WIRE T2
    WIRE T3

    OR X Y T1
    AND X Y T2
    NOT T2 T3
    AND T1 T3 Z

ENDGATE

STARTGATE ADDER INPUT X INPUT Y OUTPUT Z OUTPUT I
    
    MYXOR X Y Z
    AND X Y I

ENDGATE

ADDER A B S C

"""

shdltruthtable(shdl_code)


