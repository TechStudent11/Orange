def _input(args, variables):
    val = args[0]
    input_val = input(val)

    if len(args) == 2:
        variables[args[1].lstrip("'").lstrip('"').rstrip("'").rstrip('"')] = input_val
