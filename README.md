# switch-case-generator
 Generate a C++ style switch case structure from a list of state names and the list of functions each state calls

## Example Inputs
```
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
```

## Output:
```
case STATE_INIT:
        sm_state_init();
        break;
    case STATE_WAIT:
        sm_state_wait();
        break;
    case STATE_STOP:
        sm_state_stop();
        break;
    case STATE_START:
        sm_state_start();
        break;
    case STATE_SET_SPEED_HZ:
        sm_state_set_speed_hz();
        break;
    case STATE_SET_SPEED_RPM:
        sm_state_set_speed_rpm();
        break;
    case STATE_HOME:
        sm_state_home();
        break;
    case STATE_CALIBRATE:
        sm_state_calibrate();
        break;
    case STATE_FREEWHEEL:
        sm_state_freewheel();
        break;
    case STATE_BRAKE:
        sm_state_brake();
        break;
    case STATE_GOTO:
        sm_state_goto();
        break;
    case STATE_SAMPLERATE:
        sm_state_samplerate();
        break;
    case STATE_STARTSTREAM:
        sm_state_start_stream();
        break;
    case STATE_STOPSTREAM:
        sm_state_stop_stream();
        break;
    case STATE_PING:
        sm_state_ping();
        break;
    case STATE_HELP:
        sm_state_help();
        break;

```
