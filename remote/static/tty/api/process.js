import { dispatchEvent } from '../helpers/events';
import { toggleInput } from '../helpers/dom';
export const startProcess = (terminal) => {
    const { settings: { host } } = terminal;
    toggleInput(terminal);
    terminal.isProcessRunning = true;
    dispatchEvent("onProcessStart" /* ON_PROCESS_START */, host);
};
export const stopProcess = (terminal) => {
    const { input, settings: { host } } = terminal;
    toggleInput(terminal, true);
    terminal.isProcessRunning = false;
    input.focus();
    dispatchEvent("onProcessStop" /* ON_PROCESS_END */, host);
};
