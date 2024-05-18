# Operations
P3 handles most changes to the world and its elements through *operations*.
An operation is a 20 bytes wide struct, where the first u32 denotes the operation's type, and the following 16 bytes contain the operation's arguments.

## Scheduling
While the game executes operation handlers directly sometimes, usually operations are scheduled by inserting them into the *pending operations* queue in the static `operations` struct at `006DF2F0`:
```
00000000 operations      struc ; (sizeof=0x948, mappedto_126)
[...]
00000048 field_48_pending_operations operation_switch_input_container ?
0000046C field_46C       dd ?
00000470 field_470_pending_operations_in_use dd ?
00000474 field_474_current_operations operation_switch_input_container ?
[...]
```
The `operation_switch_input_container` struct contains an array of 53 operations.
The function `schedule_operation` at `0x00543F10` inserts an operation at the next free position, creating a new `operation_switch_input_container` and appending it to the last full one if necessary.

## Execution
The function `execute_operations` at `0x00546870` removes up to 53 operations from `operations` and executes them.

## Debugging
The following IDC script adds scripted breakpoints to the executing and scheduling functions, allowing the investigation of P3's operation behavior:
```
static handle_operation_switch() {
    auto ptr = GetRegValue("esi");
    auto operationSwitchInput = OperationSwitchInput(ptr);
    // Ignore noisy operations
    if (operationSwitchInput.opcode() == 0x94) {
        return 0;
    }
    if (operationSwitchInput.opcode() == 0x24) {
        return 0;
    }
    if (operationSwitchInput.opcode() == 0x7B) {
        return 0;
    }
    
    Message(operationSwitchInput.toString());

    return 0;
}

static handle_insert_into_pending_operations_wrapper() {
    auto ptr = GetRegValue("eax");
    auto operationSwitchInput = OperationSwitchInput(ptr);
    // Ignore noisy operations
    if (operationSwitchInput.opcode() == 0x94) {
        return 0; // weird thing
    }

    Message("handle_insert_into_pending_operations_wrapper %s", operationSwitchInput.toString());

    return 0;
}

static main() {
    auto bp = AddBpt(0x0053576B);
    SetBptCnd(0x0053576B, "handle_operation_switch()");
    auto bp2 = AddBpt(0x0054AABD);
    SetBptCnd(0x0054AABD, "handle_insert_into_pending_operations_wrapper()");
}
```
