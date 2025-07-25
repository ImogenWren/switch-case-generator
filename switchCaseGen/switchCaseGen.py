








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
    "STATE_SERVO",
    "STATE_HOME",
    "STATE_DO_CAL",
    "STATE_SAMPLERATE",
    "STATE_PRINTRATE",
    "STATE_STARTSTREAM",
    "STATE_STOPSTREAM",
    "STATE_PUTSECRET",
    "STATE_GETSECRET",
    "STATE_SAVECAL",
    "STATE_GETCAL",
    "STATE_INFO",
    "STATE_HELP"
]


functions = [
"void sm_state_init(void);",
"void sm_state_wait(void);",
"void sm_state_servo(jsonStateData stateData);",
"void sm_state_home(void);",
"void sm_state_calibrate(void);",
"void sm_state_samplerate(jsonStateData stateData);",
"void sm_state_printrate(jsonStateData stateData);",
"void sm_state_start_stream(jsonStateData stateData);",
"void sm_state_stop_stream(void);",
"void sm_state_put_secret(jsonStateData stateData);",
"void sm_state_get_secret(void);",
"void sm_state_save_cal(jsonStateData stateData);",
"void sm_state_get_cal(void);",
"void sm_state_info(void);",
"void sm_state_help(void);"
               ]






cpp_switch = generate_switch_case(states, functions)
print(cpp_switch)
