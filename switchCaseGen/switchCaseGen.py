








def generate_switch_case(states, functions):
    if len(states) != len(functions):
        raise ValueError("Both lists must have the same length")

    switch_code = ""
    for state, function in zip(states, functions):
        function_name = function.split('(')[0].strip().split()[-1]  # Extract function name
        switch_code += f"    case {state}:\n        {function_name}();\n        break;\n"

    return switch_code


# Example usage:
states = [
    "STATE_INIT",
    "STATE_WAIT",
    "STATE_STOP",
    "STATE_START",
    "STATE_SET_SPEED_HZ",
    "STATE_SET_SPEED_RPM",
    "STATE_HOME",
    "STATE_CALIBRATE",
    "STATE_FREEWHEEL",
    "STATE_BRAKE",
    "STATE_GOTO",
    "STATE_SAMPLERATE",
    "STATE_STARTSTREAM",
    "STATE_STOPSTREAM",
    "STATE_PING",
    "STATE_HELP"
]


functions = [
"void sm_state_init(void);",
"void sm_state_wait(void);",
"void sm_state_stop(void);",
"void sm_state_start(void);",
"void sm_state_set_speed_hz(jsonStateData stateData);",
"void sm_state_set_speed_rpm(jsonStateData stateData);",
"void sm_state_home(void);",
"void sm_state_calibrate(void);",
"void sm_state_freewheel(void);",
"void sm_state_brake(void);",
"void sm_state_goto(jsonStateData stateData);",
"void sm_state_samplerate(jsonStateData stateData);",
"void sm_state_start_stream(jsonStateData stateData);",
"void sm_state_stop_stream(void);",
"void sm_state_ping(void);",
"void sm_state_help(void);"
               ]






cpp_switch = generate_switch_case(states, functions)
print(cpp_switch)
